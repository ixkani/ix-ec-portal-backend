from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from requests import get
from rest_framework import status
from rest_framework.response import Response

try:
    import urllib.parse as urlparse
    import urllib.parse as urllib
except ImportError:
    from urlparse import urlparse
from portalbackend import settings
from django.utils import timezone
from portalbackend.validator.errormapping import ErrorMessage


import os
from celery import group
import datetime
import time
from portalbackend.lendapi.v1.accounting.utils import Utils
from portalbackend.lendapi.accounts.models import CompanyMeta
from portalbackend.lendapi.v1.accounting import getDiscoveryDocument
from portalbackend.lendapi.accounting.models import  LoginInfo, AccountingOauth2, TrialBalance, CoA
from portalbackend.lendapi.v1.accounting.serializers import CoASerializer
from portalbackend.lendapi.v1.accounting.tasks import qbo_trial_balance_for_period

from portalbackend.lendapi.accounts.utils import AccountsUtils
from portalbackend.lendapi.accounting.utils import AccountingUtils

class QuickBooks(object):
    """create task for company provided in state, set status to in progress"""

    def connect(self, request, company_id):
        """
           Connects a company to quickbooks
           company must be included in the querystring /?company=<id>
           :param company_id:
           :return: Redirect url of QuickBook
        """
        if not getDiscoveryDocument:
            # todo: need to clarify this scenario occurs or not and handle corect redirct urls
            auth_cancel_url = settings.QBO_AUTH_CANCEL_URL
            return redirect(auth_cancel_url)
        url = getDiscoveryDocument.auth_endpoint
        params = {'scope': settings.ACCOUNTING_SCOPE, 'redirect_uri': settings.REDIRECT_URI,
                  'response_type': 'code', 'state': company_id, 'client_id': settings.CLIENT_ID}
        url += '?' + urllib.urlencode(params)
        LoginInfo.objects.create(company_id=company_id, status=LoginInfo.IN_PROGRESS, created=timezone.now())
        return redirect(url)


    def auth_code_handler(self,request,pk=None):
        """
            Handles the authentication Code from quickbooks redirect
            :param pk: Company ID
            :param request:
            :return:
        """
        try:
            state = request.GET.get('state', None)
            error = request.GET.get('error', None)
            auth_cancel_url = settings.QBO_AUTH_CANCEL_URL
            print('############ auth code handerl state ', state)

            if error == 'access_denied':
                print('############ auth code handerl access deined ', error)
                return redirect(auth_cancel_url)
            if state is None:
                return redirect(auth_cancel_url)

            auth_code = request.GET.get('code', None)
            print('############ auth code handerl code ', auth_code)
            if auth_code is None:
                return redirect(auth_cancel_url)

            company = AccountsUtils.get_company(state)
            bearer = Utils.get_bearer_token(auth_code)
            realmId = request.GET.get('realmId', None)
            AccountingUtils.updateAccountingSession(company, bearer.accessToken, bearer.refreshToken, realmId)
            qb_status = LoginInfo.objects.filter(company=company, status=LoginInfo.IN_PROGRESS,
                                                 created__range=[timezone.now() - datetime.timedelta(minutes=10),
                                                                 timezone.now()]).first()
            qb_status.status = LoginInfo.COMPLETED

            # todo: change this env variable for production
            #qbo_auth_redirect_url = os.environ.get('QBO_AUTH_REDIRECT_URL')
            auth_redirect_url = settings.QBO_AUTH_REDIRECT_URL

            #auth_redirect_url = os.environ.get ('QBO_AUTH_REDIRECT_URL','http://ec2-52-207-28-114.compute-1.amazonaws.com/IX/coa-match/quickbooks')

            return redirect(auth_redirect_url)

            #return Utils.dispatch_success(request,"successfully authenticated")
        except Exception as e:
            # todo: need to clarify this scenario occurs or not and handle corect redirct urls
            auth_cancel_url = settings.QBO_AUTH_CANCEL_URL
            return redirect(auth_cancel_url)
            # message = "TOKEN_ALREADY_VALIDATED"
            # return Utils.dispatch_success(request,message)

    def disconnect(self, pk, request):
        """
        Disconnect the QuickBooks
        :param pk: Company ID
        :return: Response
        """
        company = AccountsUtils.get_company(pk)

        credentials = AccountingUtils.get_credentials_by_company(company)
        try:
            revoke_response = Utils.revoke_token(credentials.accessToken)
            if "Token is incorrect" in revoke_response:
                return Utils.dispatch_failure(request, "NO_TOKEN_AUTHENTICATION")
            return Utils.dispatch_success(request, "REVOKE_SUCCESSFULL")

        except Exception as e:
            print(e)
            return Utils.dispatch_failure(request, "NO_TOKEN_AUTHENTICATION")

    def refresh(self, pk, request):
        """
        Refresh the token
        :param pk: Company ID
        :return: Response
        """
        try:
            company = AccountsUtils.get_company(pk)
            credentials = AccountingUtils.get_credentials_by_company(company)
            refresh_token = credentials.refreshToken

            if refresh_token is None:
                return Utils.dispatch_failure(request, 'NO_TOKEN_AUTHENTICATION')
            bearer = Utils.get_bearer_token_from_refresh_token(refresh_token)

            if isinstance(bearer, str):
                return Utils.dispatch_success(request, bearer)
            else:

                token_info = AccountingOauth2.objects.filter(company=company).first()
                AccountingUtils.updateAccountingSession(company, bearer.accessToken,
                                                        bearer.refreshToken, token_info.realmId)
                return Utils.dispatch_success(request, "CREDENTIALS_UPDATED")
        except Exception as e:
            return Utils.dispatch_failure(request, 'NO_TOKEN_AUTHENTICATION')

    def trail_balance(self,pk, request):
        """
        Get the trail balance profile from Quick Books
        :param pk: company: Company ID
        :return: Response of trail balance
        """
        try:
            meta = CompanyMeta.objects.filter(company_id=pk).first()

            if meta.monthly_reporting_current_period:
                st = time.time()

                # this will grab the trial balance for the companymeta.monthly_reporting_current_period
                # plus 23 more months worth of history.
                job = group(qbo_trial_balance_for_period.s(pk, i) for i in range(0, 23))
                result = job.apply_async()
            else:
                return Utils.dispatch_failure(request,'MISSING_MONTHLY_REPORTING_CURRENT_PERIOD')

            # note: this bit of code basically turns this into a synchronous call, this is intended behaviour for now
            #       todo: phase 2 we need to add sockets for better communication with UI
            while not result.ready():
                continue

            print('##### CELERY get TB now takes {:.2f}s'.format(time.time() - st))
            return Utils.dispatch_success(request,'TRIAL_BALANCE_RECEIVED_SUCCESS')
        except Exception as e:
            return Utils.dispatch_failure (request,'INTERNAL_SERVER_ERROR')

    def save_trial_balance(company, response):
        """
        Parses the quickbooks JSON Response of the trial balance
        follows the format provided here https://developer.intuit.com/docs/api/accounting/trial%20balance
        :param company:
        :param response:
        :return: trial_balances
        """
        period = Utils.format_period(response["Header"]["EndPeriod"])

        currency = response["Header"]["Currency"]
        headers = [column["ColTitle"] if column["ColTitle"] != "" else column["ColType"] for
                   column in response["Columns"]["Column"]]
        entries = []

        if response["Rows"]:
            for row in response["Rows"]["Row"]:
                d = {}

                if 'ColData' in row:

                    for i in range(len(row["ColData"])):
                        d[headers[i]] = row["ColData"][i]["value"]
                        if i == 0:
                            d['id'] = row["ColData"][i]["id"]

                    d['Debit'] = float(d["Debit"]) if d["Debit"] != "" else 0
                    d['Credit'] = float(d["Credit"]) if d["Credit"] != "" else 0

                    rows_affected = TrialBalance.objects.filter(company=company,
                                                                gl_account_id=d["id"],
                                                                period=period).update(debit=d["Debit"],
                                                                                      credit=d["Credit"],
                                                                                      gl_account_name=d["Account"])
                    if rows_affected == 0:
                        entry = TrialBalance(company=company, gl_account_name=d["Account"],
                                             debit=d["Debit"], credit=d["Credit"],
                                             period=period, currency=currency,
                                             gl_account_id=d["id"])

                        entries.append(entry)

                else:
                    print("Dont process the row")

        #TrialBalance.objects.bulk_create(entries)

        return entries

    def chart_of_accounts(self,company,request):
        """
        Get the chart of account profile from Quick Books
        :param company: Company ID
        :return: Response
        """
        try:
            company = AccountsUtils.get_company(company)
            cm = CompanyMeta.objects.filter(company_id=company).first()

            credentials = AccountingUtils.get_credentials_by_company(company)

            if not credentials:
                return Utils.dispatch_failure(request,"NO_TOKEN_AUTHENTICATION")

            chart_of_accounts_response, status_code = Utils.get_chart_of_accounts(credentials.accessToken,
                                                                                  credentials.realmId)

            if status_code >= 400:
                print("First Failure")
                bearer = Utils.get_bearer_token_from_refresh_token(credentials.refreshToken)

                new_credentials = AccountingUtils.updateAccountingSession(company, bearer.accessToken,
                                                                          bearer.refreshToken, credentials.realmId)

                chart_of_accounts_response, status_code = Utils.get_chart_of_accounts(new_credentials.accessToken,
                                                                                      new_credentials.realmId)
                if status_code >= 400:
                    return Utils.dispatch_failure(request,"NO_TOKEN_AUTHENTICATION")


            coas = QuickBooks.save_chart_of_accounts(company, chart_of_accounts_response)

            cm.chartofaccounts_last_refresh_date = datetime.datetime.now()
            cm.save()

            serializer = CoASerializer(coas, many=True)

            return Utils.dispatch_success(request,"COA_FETECHED_SUCCESSFULLY")
        except Exception as e:
            return Utils.dispatch_failure (request,'INTERNAL_SERVER_ERROR')

    def save_chart_of_accounts(company, response):
        """
        Parses the Chart of accounts Json Response into CoA Objects to save into database
        follows the format provided here https://developer.intuit.com/docs/api/accounting/account
        :param company: the company object being referenced
        :param response: the json response object
        :return:
        """
        """
                Parses the Chart of accounts Json Response into CoA Objects to save into database
                follows the format provided here https://developer.intuit.com/docs/api/accounting/account
                :param company: the company object being referenced
                :param response: the json response object
                :return:
                """
        coas = []
        for account in response["QueryResponse"]["Account"]:
            exists = CoA.objects.filter(company=company, gl_account_id=account["Id"]).first()
            if exists:
                exists.gl_account_name = account["Name"]
                exists.gl_account_currency = account["CurrencyRef"]["value"]
                exists.gl_account_id = account["Id"]
                exists.gl_account_bal = account["CurrentBalance"]
                exists.save()
                # doesn't return coa that already existed in the system
                # coas.append(exists)
            else:
                coa = CoA(company=company, gl_account_type=account["AccountType"],
                          gl_account_name=account["Name"], gl_account_currency=account["CurrencyRef"]["value"],
                          gl_account_id=account["Id"], gl_account_bal=account["CurrentBalance"])
                coa.save()
                coas.append(coa)
        return coas

    def is_token_valid(self,pk,request):
        """
        Check the validity of Token
        :param pk: Company ID
        :return: Response of validation
        """
        try:
            company = AccountsUtils.get_company(pk)
            credentials = AccountingOauth2.objects.filter(company=company).first()
            if credentials:
                sample_response, status_code = Utils.get_company_info(credentials.accessToken, credentials.realmId)
                if status_code >= 400:
                    bearer = get(credentials.refreshToken)
                    new_credentials = AccountingUtils.updateAccountingSession(company, bearer.accessToken,
                                                                              bearer.refreshToken, credentials.realmId)
                    sample_response, status_code = Utils.get_company_info(new_credentials.accessToken,
                                                                          new_credentials.realmId)
                    if status_code >= 400:
                        return Utils.dispatch_failure(request,'NO_TOKEN_AUTHENTICATION')
                return Utils.dispatch_success(request,"AUTHENTICATED_SUCCESSFULLY")
            return Utils.dispatch_failure (request,'NO_TOKEN_AUTHENTICATION')
        except Exception as e:
            return Utils.dispatch_failure(request,'NO_TOKEN_AUTHENTICATION')
