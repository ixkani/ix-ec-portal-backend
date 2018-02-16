import os
import time

import re
from celery import group
from django.utils import timezone
from rest_framework import status
from django.shortcuts import redirect
from xero import Xero
from xero.auth import PublicCredentials,PartnerCredentials,PrivateCredentials
from xero.exceptions import XeroException, XeroBadRequest

from portalbackend import settings
from portalbackend.lendapi.accounting.models import LoginInfo, AccountingOauth2, TrialBalance, CoA
from portalbackend.lendapi.accounts.models import Company,CompanyMeta,AccountingConfiguration
from portalbackend.lendapi.accounts.utils import AccountsUtils
from portalbackend.lendapi.v1.accounting.utils import Utils
from portalbackend.lendapi.accounting.utils import AccountingUtils


OAUTH_PERSISTENT_SERVER_STORAGE = {}


class XeroAccountings(object):
    def connect(self, request, company):
        """
           Connects a company to Xero
           company must be included in the querystring /?company=<id>
        """
        try:
            secret_keys = Utils.get_access_keys(company)

            consumer_key = secret_keys.auth_key
            consumer_secret = secret_keys.secret_key

            global credentials
            call_back_uri = settings.XERO_CALL_BACK_URI + "/" + company

            # call_back_url = 'http://localhost/oauth'
            if AccountingConfiguration.PRIVATE == secret_keys.xero_accounting_type:
                credentials = PrivateCredentials(consumer_key=consumer_key,rsa_key=consumer_secret)
                OAUTH_PERSISTENT_SERVER_STORAGE.update({'consumer_key':credentials.consumer_key})
                OAUTH_PERSISTENT_SERVER_STORAGE.update({'rsa_key':credentials.rsa_key})
                url = call_back_uri
            else:
                credentials = PublicCredentials(consumer_key, consumer_secret, callback_uri=call_back_uri)
                # Save generated credentials details to persistent storage
                for key, value in credentials.state.items():
                    OAUTH_PERSISTENT_SERVER_STORAGE.update({key: value})

                LoginInfo.objects.create(company_id=company, status=LoginInfo.IN_PROGRESS, created=timezone.now())
                url = credentials.url

        except Exception as e:
            auth_cancel_url = settings.QBO_AUTH_CANCEL_URL
            Utils.send_company_misconfig(company,e)
            return redirect(auth_cancel_url + '/error')
        return Utils.redirect_response(url)

    def auth_code_handler(self, request, pk=None):
        """
        Handle Auth Code of xero
        :param request: GET Request
        :param pk: Company ID
        :return: Response
        """
        try:
            # Get xero auth access information form xero connection
            stored_values = OAUTH_PERSISTENT_SERVER_STORAGE


            if len(stored_values) == 0:
                return Utils.dispatch_failure(request, 'NO_TOKEN_AUTHENTICATION')

            secret_keys = Utils.get_access_keys(pk)
            if AccountingConfiguration.PRIVATE == secret_keys.xero_accounting_type:
                exists = AccountingOauth2.objects.filter(company=pk).first()
                if not exists:
                    auth = AccountingOauth2(accessToken=stored_values['consumer_key'],
                                            accessSecretKey=stored_values['rsa_key'],
                                        company_id=pk)
                    auth.save()
                else:
                    exists.accessToken = stored_values['consumer_key']
                    exists.accessSecretKey = stored_values['rsa_key']
                    exists.save()
            else:
                auth_verifier_uri = settings.XERO_AUTH_VERIFIER_URI
                oauth_verifier = request.GET.get('oauth_verifier')
                credentials = Utils.get_xero_public_credentials(stored_values)

                if credentials.expired():
                    return Utils.dispatch_failure(request, 'NO_TOKEN_AUTHENTICATION')

                # Verify the auth verifier for establish the connection

                credentials.verify(oauth_verifier)
                # Resave our verified credentials
                for key, value in credentials.state.items():
                    OAUTH_PERSISTENT_SERVER_STORAGE.update({key: value})

                stored_values = OAUTH_PERSISTENT_SERVER_STORAGE
                exists = AccountingOauth2.objects.filter(company=pk).first()

                if exists:
                    exists.accessToken = stored_values['oauth_token']
                    exists.realmId = oauth_verifier
                    exists.accessSecretKey = stored_values['oauth_token_secret']
                    exists.tokenAcitvatedOn = stored_values['oauth_expires_at']
                    exists.tokenExpiryON = stored_values['oauth_authorization_expires_at']
                    exists.save()
                else:
                    auth = AccountingOauth2(accessToken=stored_values['oauth_token'],
                                            refreshToken='',
                                            realmId=oauth_verifier,
                                            accessSecretKey=stored_values['oauth_token_secret'],
                                            tokenAcitvatedOn=stored_values['oauth_expires_at'],
                                            tokenExpiryON=stored_values['oauth_authorization_expires_at'],
                                            company_id=pk)
                    auth.save()
                # auth_redirect_url = os.environ.get ('QBO_AUTH_REDIRECT_URL',
                #                                        'http://localhost:4200/coa-match/quickbooks')

                # auth_redirect_url = os.environ.get ('QBO_AUTH_REDIRECT_URL','http://ec2-52-207-28-114.compute-1.amazonaws.com/ix/coa-match/quickbooks')

                # return redirect(auth_redirect_url)

        except Exception as e:
            auth_cancel_url = settings.QBO_AUTH_CANCEL_URL
            Utils.send_company_misconfig(pk, e)
            return redirect(auth_cancel_url + '/error')
            #return Utils.dispatch_success(request, 'TOKEN_ALREADY_VALIDATED')

        auth_redirect_url = settings.XERO_AUTH_REDIRECT_URL
        return redirect(auth_redirect_url)
        # return Utils.dispatch_success(request, stored_values)

    def trail_balance(self, pk, request):
        """
        Get Trail Balance From online
        :param company: Company Id
        :return: Response
        """
        try:
            # Checking Token Authentication available
            auth_info = AccountingOauth2.objects.filter(company_id=pk).values('accessToken', 'accessSecretKey',
                                                                             'tokenAcitvatedOn', 'tokenExpiryON')
            secret_keys = Utils.get_access_keys(pk)
            if len(auth_info) == 0:
                return Utils.dispatch_failure(request, "NO_TOKEN_AUTHENTICATION")

            for key, value in auth_info[0].items():
                OAUTH_PERSISTENT_SERVER_STORAGE.update({key: value})
            stored_values = OAUTH_PERSISTENT_SERVER_STORAGE

            if len(stored_values) == 0:
                return Utils.dispatch_failure(request, "NO_TOKEN_AUTHENTICATION")


            # Checking Xero Connection Authentication available
            auth = Utils.get_xero_auth(pk)

            if AccountingConfiguration.PRIVATE == secret_keys.xero_accounting_type:
                credentials = PrivateCredentials(**auth)
            else:
                credentials = PublicCredentials(**auth)

                if credentials.expired() or credentials is None:
                    return Utils.dispatch_failure(request, "NO_TOKEN_AUTHENTICATION")

            try:
                xero = Xero(credentials)
                xero.reports.get('TrialBalance')

            except XeroException as e:
                if AccountingConfiguration.PRIVATE == secret_keys.xero_accounting_type:
                    error = ["%s" % e]
                    return Utils.dispatch_failure(request, 'XERO_CONNECTION_ERROR', error)
                else:
                    return Utils.dispatch_failure(request, "NO_TOKEN_AUTHENTICATION")
            try:
                meta = CompanyMeta.objects.filter(company_id=pk).first()
                if meta.monthly_reporting_current_period:
                    st = time.time()
                    from portalbackend.lendapi.v1.accounting.tasks import trial_balance_for_period
                    job = group(trial_balance_for_period.s(pk, i) for i in range(0, 23))
                    result = job.apply_async()
                else:
                    return Utils.dispatch_failure(request, 'MISSING_MONTHLY_REPORTING_CURRENT_PERIOD')

                while not result.ready():
                    continue
                return Utils.dispatch_success(request, 'TRIAL_BALANCE_RECEIVED_SUCCESS')
            except Exception as e:
                error = ["%s" % e]
                return Utils.dispatch_failure(request, 'DATA_PARSING_ISSUE', error)
        except Exception as e:
            return Utils.dispatch_failure(request, "INTERNAL_SERVER_ERROR")

    def save_trial_balance(company, response):

        period = response["ReportTitles"][2]
        months = dict(January=1, February=2, March=3, April=4, May=5, June=6, July=7, August=8, September=9, October=10,
                      November=11, December=12)
        period = period.split(' ')
        period = period[2:]
        period[1] = str(months[period[1]])
        temp = period[0]
        period[0] = period[2]
        period[2] = temp
        print(period)
        period = Utils.format_period(' '.join(period))


        currency = 'CAD'  # TODO: need to get currency from any where in xero
        gl_account_id = 0
        for row in response["Rows"]:
            if row["RowType"] == "Header":
                headers = [column for column in row["Cells"]]

            if row["RowType"] == "Section":
                for child_row in row["Rows"]:
                    d = {}
                    d[headers[0]["Value"]] = child_row["Cells"][0]["Value"]
                    d[headers[1]["Value"]] = float(child_row["Cells"][1]["Value"]) if child_row["Cells"][1][
                                                                                          "Value"] != "" else 0
                    d[headers[2]["Value"]] = float(child_row["Cells"][2]["Value"]) if child_row["Cells"][2][
                                                                                   "Value"] != "" else 0
                    try:
                        id = re.search(r"\(([0-9]+)\)", d["Account"])
                        d['Id'] = id.group(1)
                    except Exception:
                        continue

                    exists = TrialBalance.objects.filter(company=company, gl_account_id=d["Id"],
                                                         period=period).first()

                    if exists:
                        exists.debit, exists.credit = d["Debit"], d["Credit"]
                        exists.gl_account_name = d["Account"]
                        exists.save()
                    else:
                        trial = TrialBalance(company=company, gl_account_name=d["Account"],
                                             debit=d["Debit"], credit=d["Credit"],
                                             period=period, currency=currency,
                                             gl_account_id=d["Id"])
                        trial.save()
        return

    def chart_of_accounts(self,id,request):
        """
        Get Chart of Accounts From online
        :param company: Company ID
        :return: Response
        """

        try:
            # login_status = Utils.get_login_status(company)
            # if login_status != LoginInfo.IN_PROGRESS:
            #     message = "Login Authentication Failed"
            #     return Utils.dispatch_failure(request,message)
            company = AccountsUtils.get_company(id)
            secret_keys = Utils.get_access_keys(id)
            # Get xero auth access information form xero connection
            auth_info = AccountingOauth2.objects.filter(company_id=id).values('accessToken', 'accessSecretKey',
                                                                                  'tokenAcitvatedOn', 'tokenExpiryON')
            if len(auth_info) == 0:
                return Utils.dispatch_failure(request, 'NO_TOKEN_AUTHENTICATION')

            for key, value in auth_info[0].items():
                OAUTH_PERSISTENT_SERVER_STORAGE.update({key: value})
            stored_values = OAUTH_PERSISTENT_SERVER_STORAGE

            if len(stored_values) == 0:
                return Utils.dispatch_failure(request, "NO_TOKEN_AUTHENTICATION")

            auth = Utils.get_xero_auth(id)


            if AccountingConfiguration.PRIVATE == secret_keys.xero_accounting_type:
                credentials = PrivateCredentials(**auth)
            else:
                credentials = PublicCredentials(**auth)

                if credentials.expired():
                    return Utils.dispatch_failure(request, 'NO_TOKEN_AUTHENTICATION')

            # Enable the access for accessing the reports from xero logged in account.
            xero = Xero(credentials)
            # Resave our verified credentials
            # stored_values = bind_auth_info(credentials, pk)

        except XeroException as e:
            if AccountingConfiguration.PRIVATE == secret_keys.xero_accounting_type:
                error = ["%s" % e]
                return Utils.dispatch_failure(request, 'XERO_CONNECTION_ERROR', error)
            else:
                return Utils.dispatch_failure(request, "NO_TOKEN_AUTHENTICATION")
        try:
            chartofaccounts = xero.accounts.all()
            XeroAccountings.save_chart_of_accounts(company, chartofaccounts)
            return Utils.dispatch_success(request,"COA_FETECHED_SUCCESSFULLY")
        except XeroException as e:
            if AccountingConfiguration.PRIVATE == secret_keys.xero_accounting_type:
                error = ["%s" % e]
                return Utils.dispatch_failure(request, 'XERO_CONNECTION_ERROR', error)
            else:
                return Utils.dispatch_failure(request, "NO_TOKEN_AUTHENTICATION")
        except Exception as e:
            error = ["%s" % e]
            return Utils.dispatch_failure(request, 'DATA_PARSING_ISSUE', error)

    def save_chart_of_accounts(company, response):
        coas = []
        print(response)
        currency = "CAD"
        #account_type = response[0]["BankAccountType"]
        for account in response:
            if "Code" not in account:
                continue
            account_type = account["Type"]
            account_code = account["Code"]
            account_name = account["Name"]
            exists = CoA.objects.filter(company=company, gl_account_id=account_code).first()
            if exists:
                exists.gl_account_name = account_name
                exists.gl_account_currency = currency
                exists.gl_account_id = account_code
                exists.gl_account_bal = 0
                exists.save()
            # doesn't return coa that already existed in the system
            # coas.append(exists)
            else:
                coa = CoA(company=company, gl_account_type=account_type,
                          gl_account_name=account_name, gl_account_currency=currency,
                          gl_account_id=account_code, gl_account_bal=0)
                coa.save()
                coas.append(coa)
        return coas

    def disconnect(self,pk,request):
        """
        Disconnect for xero
        :param pk: Company ID
        :return: Response
        """
        # TODO Disconnect need to be created
        pass

    def refresh(self,pk,request):
        """
        Refresh for xero
        :param pk: Company ID
        :return: Response
        """
        # TODO Refresh need to be created
        pass

    def is_token_valid(self,pk,request):
        """
        Check token valid for xero
        :param pk: Company ID
        :return: Response
        """

        pass
