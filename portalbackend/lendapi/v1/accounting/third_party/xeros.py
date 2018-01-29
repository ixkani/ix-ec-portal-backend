import os
from django.utils import timezone
from rest_framework import status
from django.shortcuts import redirect
from xero import Xero
from xero.auth import PublicCredentials
from xero.exceptions import XeroException

from portalbackend import settings
from portalbackend.lendapi.accounting.models import LoginInfo, AccountingOauth2, TrialBalance, CoA
from portalbackend.lendapi.accounts.models import Company
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

            account_type = secret_keys['accounting_type']

            # Check verify the company account tool
            if account_type != Company.XERO:
                return Utils.dispatch_failure(request, 'XERO_CONFIGURATION_NOT_FOUND')

            consumer_key = secret_keys['auth_key']
            consumer_secret = secret_keys['secret_key']

            global credentials
            try:
                call_back_uri = settings.XERO_CALL_BACK_URI + "/" + company

                # call_back_url = 'http://localhost/oauth'
                credentials = PublicCredentials(consumer_key, consumer_secret, callback_uri=call_back_uri)

                # Save generated credentials details to persistent storage
                for key, value in credentials.state.items():
                    OAUTH_PERSISTENT_SERVER_STORAGE.update({key: value})

                LoginInfo.objects.create(company_id=company, status=LoginInfo.IN_PROGRESS, created=timezone.now())

            except Exception as e:
                error = ["%s" % e]
                return Utils.dispatch_failure(request, 'XERO_CONNECTION_FAILED', error)

        except Exception as e:
            error = ["%s" % e]
            return Utils.dispatch_failure(request, 'XERO_CONNECTION_FAILED', error)
        return Utils.redirect_response(credentials.url)

    def auth_code_handler(self, request, pk=None):
        """
        Handle Auth Code of xero
        :param request: GET Request
        :param pk: Company ID
        :return: Response
        """
        try:
            auth_verifier_uri = settings.XERO_AUTH_VERIFIER_URI
            oauth_verifier = request.GET.get('oauth_verifier')
            # Get xero auth access information form xero connection
            stored_values = OAUTH_PERSISTENT_SERVER_STORAGE

            if len(stored_values) == 0:
                return Utils.dispatch_failure(request, 'NO_TOKEN_AUTHENTICATION')

            credentials = PublicCredentials(consumer_key=stored_values['consumer_key'],
                                            consumer_secret=stored_values['consumer_secret'],
                                            callback_uri=stored_values['callback_uri'],
                                            verified=stored_values['verified'],
                                            oauth_token=stored_values['oauth_token'],
                                            oauth_token_secret=stored_values['oauth_token_secret'],
                                            oauth_expires_at=stored_values['oauth_expires_at'],
                                            oauth_authorization_expires_at=stored_values[
                                                'oauth_authorization_expires_at'],
                                            )
            if credentials.expired():
                return Utils.dispatch_failure(request, 'XERO_CONNECTION_EXPIRED')

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
            return Utils.dispatch_success(request, 'TOKEN_ALREADY_VALIDATED')

        auth_redirect_url = settings.QBO_AUTH_REDIRECT_URL
        return redirect(auth_redirect_url)
        # return Utils.dispatch_success(request, stored_values)

    def trail_balance(self, id, request):
        """
        Get Trail Balance From online
        :param company: Company Id
        :return: Response
        """
        try:
            company = AccountsUtils.get_company(id)
            # Get xero auth access information form xero connection

            auth = {}
            auth_info = AccountingOauth2.objects.filter(company_id=id).values('accessToken', 'accessSecretKey',
                                                                              'tokenAcitvatedOn', 'tokenExpiryON')
            if len(auth_info) == 0:
                return Utils.dispatch_failure(request, 'NO_TOKEN_AUTHENTICATION')

            auth['oauth_token'] = auth_info[0]['accessToken']
            auth['oauth_token_secret'] = auth_info[0]['accessSecretKey']
            auth['oauth_authorization_expires_at'] = Utils.format_expiry_duration(auth_info[0]['tokenAcitvatedOn'])
            auth['oauth_expires_at'] = Utils.format_expiry_duration(auth_info[0]['tokenExpiryON'])
            access_key = Utils.get_access_keys(id)
            auth['consumer_key'] = access_key['auth_key']
            auth['consumer_secret'] = access_key['secret_key']
            auth['verified'] = True
            auth['callback_uri'] = 'http://localhost:8000/lend/v1/xero/authCodeHandler/'

            for key, value in auth_info[0].items():
                OAUTH_PERSISTENT_SERVER_STORAGE.update({key: value})
            stored_values = OAUTH_PERSISTENT_SERVER_STORAGE

            if len(stored_values) == 0:
                return Utils.dispatch_failure(request, "NO_TOKEN_AUTHENTICATION")

            credentials = PublicCredentials(**auth)

            if credentials.expired():
                return Utils.dispatch_failure(request, "XERO_CONNECTION_EXPIRED")

            if credentials is None:
                return Utils.dispatch_failure(request, "REFRESH_TOKEN_NOT_FOUND")


            # Enable the access for accessing the reports from xero logged in account.
            xero = Xero(credentials)
            # cm = CompanyMeta.objects.filter(company_id=pk).first()
            trialbalance = xero.reports.get('TrialBalance', params={})


            try:
                XeroAccountings.save_trial_balance(company, trialbalance[0])
                return Utils.dispatch_success(request, "TRIAL_BALANCE_RECEIVED_SUCCESS")
            except Exception as e:
                error = ["%s" % e]
                return Utils.dispatch_failure(request, 'DATA_PARSING_ISSUE', error)

        except Exception as e:
            return Utils.dispatch_failure(request, "INTERNAL_SERVER_ERROR")

    def save_trial_balance(company, response):

        period=response["ReportDate"]
        if " " in period:
            period = period.split(" ")
        else:
            period = period.split("-")

        temp = period[0]
        period[0] = period[2]
        period[2] = temp
        months = dict(January=1, February=2, March=3, April=4, May=5, June=6, July=7, August=8, September=9, October=10,
                      November=11, December=12)
        period[1] = str(months[period[1]])
        period = Utils.format_period(' '.join(period))


        currency = 'CAD'  # TODO: need to get currency from any where in xero
        for row in response["Rows"]:
            if row["RowType"] == "Header":
                headers = [column for column in row["Cells"]]

            if row["RowType"] == "Section":
                i = 0
                for child_row in row["Rows"]:
                    d = {}
                    i = i + 1
                    d['Id'] = i
                    d[headers[0]["Value"]] = child_row["Cells"][0]["Value"]
                    d[headers[1]["Value"]] = float(child_row["Cells"][1]["Value"]) if child_row["Cells"][1][
                                                                                          "Value"] != "" else 0
                    d[headers[2]["Value"]] = float(child_row["Cells"][2]["Value"]) if child_row["Cells"][2][
                                                                                          "Value"] != "" else 0
                    print(d)
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
            # Get xero auth access information form xero connection
            auth = {}
            auth_info = AccountingOauth2.objects.filter(company_id=id).values('accessToken', 'accessSecretKey',
                                                                              'tokenAcitvatedOn', 'tokenExpiryON')
            if len(auth_info) == 0:
                return Utils.dispatch_failure(request, 'NO_TOKEN_AUTHENTICATION')

            auth['oauth_token'] = auth_info[0]['accessToken']
            auth['oauth_token_secret'] = auth_info[0]['accessSecretKey']
            auth['oauth_authorization_expires_at'] = Utils.format_expiry_duration(auth_info[0]['tokenAcitvatedOn'])
            auth['oauth_expires_at'] = Utils.format_expiry_duration(auth_info[0]['tokenExpiryON'])

            access_key = Utils.get_access_keys(id)
            auth['consumer_key'] = access_key['auth_key']
            auth['consumer_secret'] = access_key['secret_key']
            auth['verified'] = True
            auth['callback_uri'] = 'http://localhost:8000/lend/v1/xero/authCodeHandler/'

            for key, value in auth_info[0].items():
                OAUTH_PERSISTENT_SERVER_STORAGE.update({key: value})
            stored_values = OAUTH_PERSISTENT_SERVER_STORAGE

            if len(stored_values) == 0:
                return Utils.dispatch_failure(request, "NO_TOKEN_AUTHENTICATION")


            credentials = PublicCredentials(**auth)
            if credentials.expired():
                return Utils.dispatch_failure(request, 'XERO_CONNECTION_EXPIRED')

            # Enable the access for accessing the reports from xero logged in account.
            xero = Xero(credentials)
            # Resave our verified credentials
            # stored_values = bind_auth_info(credentials, pk)

        except XeroException as e:
            return Utils.dispatch_failure(request, "INTERNAL_SERVER_ERROR")
        try:
            chartofaccounts = xero.accounts.all()
            XeroAccountings.save_chart_of_accounts(company, chartofaccounts)
            return Utils.dispatch_success(request,"COA_FETECHED_SUCCESSFULLY")
        except Exception as e:
            error = ["%s" % e]
            return Utils.dispatch_failure(request, 'DATA_PARSING_ISSUE', error)

    def save_chart_of_accounts(company, response):

        coas = []
        currency = 'CAD'
        account_type = response[0]["BankAccountType"]
        for account in response:

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
        # TODO Token validation need to be created
        pass
