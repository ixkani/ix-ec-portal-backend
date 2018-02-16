import base64
import calendar
import copy
import datetime
import json
import logging
import os
import random
import re
import uuid
from datetime import timedelta

import requests
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.http import HttpResponse
from django.utils.timezone import utc
from rest_framework import status
from rest_framework.response import Response

from portalbackend import settings
from portalbackend.lendapi.accounting.models import Bearer, LoginInfo
# token can either be an accessToken or a refreshToken
from portalbackend.lendapi.accounting.utils import AccountingUtils
from portalbackend.lendapi.accounts.models import Company, EspressoContact, User, Contact, CompanyMeta, FiscalYearEnd, \
    AccountingConfiguration
from portalbackend.lendapi.accounts.utils import AccountsUtils
from portalbackend.lendapi.constants import MONTHLY_REPORT_KEY_ERROR_EMAIL_SUBJECT, \
    COMAPANY_META_EMAIL_BODY, COMAPANY_META_EMAIL_SUBJECT, MONTHLY_REPORT_KEY_ERROR_ADMIN_EMAIL_BODY, \
    MONTHLY_REPORT_KEY_ERROR_USER_EMAIL_BODY, COMAPANY_CURRENT_REPORT_PERIOD_EMAIL_SUBJECT, \
    COMAPANY_CURRENT_REPORT_PERIOD_EMAIL_BODY, ERROR_TAG_EMAIL_ADMIN_BODY, \
    ERROR_TAG_EMAIL_USER_BODY, COMPANY_META_NOT_FOUND_EMAIL_ADMIN, \
    COMPANY_PERIOD_NOT_FOUND_EMAIL_ADMIN, COMPANY_MISCONFIG_EMAIL_ADMIN, COMPANY_MISCONFIG_EMAIL_SUBJECT, \
    COMPANY_MISCONFIG_EMAIL_BODY
from portalbackend.lendapi.v1.accounting import getDiscoveryDocument
from portalbackend.lendapi.v1.accounting.serializers import CompanyDetailSerializer, LoginInfoSerializer
from portalbackend.lendapi.v1.accounts.serializers import CompanySerializer
from portalbackend.settings import BASE_DIR, EMAIL_ENABLED
from portalbackend.validator.errorcodemapping import ErrorCode
from portalbackend.validator.errormapping import ErrorMessage
from portalbackend.validator.headercodemapping import HeaderErrorCode
from xero.auth import PublicCredentials,PrivateCredentials


class Utils(object):
    """
    Collection of utility functions used within the views
    """

    @staticmethod
    # todo: the logic in this function needs to be fixed
    def validate_query(request, dateformat=False):
        """
        Validates a date range query request appended to url
        :param request:
        :param dateformat: this optional parameter specifies whether the function should return datetime.date objects
                            of the specified dates so it can be used in the query. Default False
        :return:
        """
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        validation = re.compile(r'\d{4}-\d{2}-\d{2}')

        if start_date and end_date:
            # Matches the YYYY-MM-DD in numbers
            if validation.match(start_date) and validation.match(end_date):
                try:
                    datetime.datetime.strptime(start_date, '%Y-%m-%d')
                    datetime.datetime.strptime(end_date, '%Y-%m-%d')
                except ValueError:
                    return '', ['ERROR', 'INVALID_DATE']

                query = '?start_date=' + start_date + '&end_date=' + end_date
                # Return the datetime.date objects
                if dateformat:
                    start = Utils.format_period(start_date, False)
                    end = Utils.format_period(end_date, False)
                    print('dates sent in are ', start, end)
                    return query, [start, end]
                return query
            else:
                return '', ['ERROR', 'INVALID_DATE']
        elif end_date:
            # Matches the YYYY-MM-DD in numbers
            if validation.match(end_date):
                try:
                    datetime.datetime.strptime(end_date, '%Y-%m-%d')
                except ValueError:
                    return '', ['ERROR', 'INVALID_END_DATE']
                query = '?end_date=' + end_date
                # Return the datetime.date objects
                if dateformat:
                    end = Utils.format_period(end_date, False)
                    return query, [end]
                return query
            else:
                return '', ['ERROR', 'INVALID_END_DATE']
        elif start_date and not end_date:
            return '', ['ERROR', 'MISSING_END_DATE']

        elif not start_date and not end_date:
            return '', None

        return ''

    @staticmethod
    def get_accounting_type(company_id):
        """
        Get Accounting type
        :param company_id: Company ID
        :return: accounting type
        """
        try:
            is_exist = Company.objects.filter(id=company_id).count()
            if is_exist == 0:
                return "NONE"
            keys = Company.objects.filter(id=company_id).values('accounting_type')
            secret_keys = keys[0]
            accounting_type = secret_keys['accounting_type']
            return accounting_type
        except IndexError:
            return "NONE"

    '''@staticmethod
    def dispatch_failure(message, code=status.HTTP_400_BAD_REQUEST):
        """
        This method for dispatch failure the response
        :param message:
        :param code:
        :return:
        """

        return Response(data={"status": "failed", "message": message}, status=code)'''

    '''@staticmethod
    def dispatch_failure(message, code=status.HTTP_400_BAD_REQUEST):
        """
        This method for dispatch failure the response
        :param message:
        :param code:
        :return:
        """
        errors = {}
        errors['status'] = 'failed'
        errors['message'] = message

        return Response (data=errors, status=code)'''

    @staticmethod
    def record_log(request, data, code):
        try:
            formatter = "\n%(asctime)s ] ----------| LOG STATUS - %(levelname)s\n" \
                        "%(asctime)s ] ----------| REMOTE ADDRESS - %(remote_address)s\n" \
                        "%(asctime)s ] ----------| API STATUS - %(api_status)s\n" \
                        "%(asctime)s ] ----------| RESPONSE CODE - %(response_code)s\n" \
                        "%(asctime)s ] ----------| REQUEST METHOD - %(request_method)s\n" \
                        "%(asctime)s ] ----------| URL - %(request_url)s\n" \
                        "***************************************************************************\n" \
                        "%(asctime)s ] ----------| RESPONSE\n" \
                        "%(message)s \n" \
                        "----------------------------------------------------------------------------"
            extra_args = {
                "remote_address": request.META['REMOTE_ADDR'],
                "request_url": request.get_full_path(),
                "request_method": request.method,
                "api_status": data['status'].upper(),
                "response_code": code,
            }
            if code is status.HTTP_200_OK:
                data = data['status']

            logger = logging.getLogger(__name__)
            hdlr = logging.FileHandler(
                os.path.join(BASE_DIR, 'logs/error_{}.log'.format(datetime.datetime.now().strftime("%Y_%m_%d"))))

            if (logger.hasHandlers()):
                logger.handlers.clear()

            hdlr.setFormatter(logging.Formatter(formatter))
            logger.addHandler(hdlr)
            logger.setLevel(logging.INFO)

            if code is status.HTTP_200_OK:
                logger.info(json.dumps(data, indent=4, separators=(',', ': ')), extra=extra_args)
            else:
                logger.error(json.dumps(data, indent=4, separators=(',', ': ')), extra=extra_args)

        except Exception as e:
            pass
        return

    @staticmethod
    def dispatch_failure(request, identifier, response=None, code=status.HTTP_400_BAD_REQUEST):
        if hasattr(HeaderErrorCode, identifier):
            code = getattr(HeaderErrorCode, identifier)

        if hasattr(ErrorCode, identifier):
            error_code = getattr(ErrorCode, identifier)
        else:
            error_code = code

        error_message = getattr(ErrorMessage, identifier)
        errors = {}
        if response is None:
            errors['status'] = 'failed'
            errors['code'] = error_code
            errors['message'] = error_message
        else:
            errors['status'] = 'failed'
            errors['code'] = error_code
            errors['message'] = error_message
            errors['errors'] = response


        Utils.record_log(request, errors, code)
        return Response(data=errors, status=code)

    @staticmethod
    def dispatch_notification(request, message, string="", code=status.HTTP_400_BAD_REQUEST):
        '''
        This method for dispatch the success response
        :param response:
        :param code:
        :return:
        '''

        if hasattr(HeaderErrorCode, message):
            code = getattr(HeaderErrorCode, message)

        notification_message = getattr(ErrorMessage, message)

        if hasattr(ErrorCode, message):
           error_code = getattr(ErrorCode, message)

        Utils.record_log(request, message, code)
        return Response(data={'status': 'info', 'message': notification_message + string, "code": error_code},
                        status=code)

    @staticmethod
    def dispatch_success(request, response, code=status.HTTP_200_OK):
        '''
        This method for dispatch the success response
        :param response:
        :param code:
        :return:
        '''
        if isinstance(response, list) or isinstance(response, dict):
            data = {'status': 'success', 'result': response}

        else:
            message = getattr(ErrorMessage, response)
            data = {'status': 'success', 'message': message}

        Utils.record_log(request, data, code)
        return Response(data=data, status=code)

    @staticmethod
    def format_period(period, monthend=True):
        """
        Converts a date into a datetime object of the last day of the month
        :param period: the datestring formatted "YYYY-MM-DD"
        :param monthend: Whether to format the date to monthend, default is true
        :return: datetime.date object
        """
        months = dict(January=1, February=2, March=3, April=4, May=5, June=6, July=7, August=8, September=9, October=10,
                      November=11, December=12)

        # if len(period.split(" ")) > 0:
        #    period = period.split(" ")
        # else:

        if " " in period:
            period = period.split(" ")
        else:
            period = period.split("-")

        if isinstance(int(period[1]), int):
            if monthend:
                month, year = period[1], period[0]
                dt = datetime.date(year=int(year), month=int(month), day=calendar.monthrange(int(year), int(month))[1])
                return dt
            year, month, day = int(period[0]), int(period[1]), int(period[2])
            dt = datetime.date(year, month, day)
        else:
            if monthend:
                month, year = months[period[1]], period[0]
                dt = datetime.date(year=int(year), month=int(month), day=calendar.monthrange(int(year), int(month))[1])
                return dt
            year, month, day = int(period[0]), int(months[period[1]]), int(period[2])
            dt = datetime.date(year, month, day)
        return dt

    @staticmethod
    def format_expiry_duration(duration):
        """
        Converts a date into a datetime object
        :param duration:
        :return: datetime.datetime object
        """
        duration = duration.split(" ")
        date = duration[0].split("-")
        year, month, date = date[0], date[1], date[2]
        time = duration[1].split(":")
        hours, minutes = time[0], time[1]
        time_seconds = time[2].split(".")
        seconds, micro = time_seconds[0], time_seconds[1]
        return datetime.datetime(int(year), int(month), int(date), int(hours), int(minutes), int(seconds), int(micro))

    @staticmethod
    def get_access_keys(id):
        '''
        Get the Access Key for accounting system
        :param id: Company ID
        :return: Access Key of accounting system
        '''
        company = Company.objects.filter(id=id).first()
        return AccountingConfiguration.objects.filter(accounting_type=company.accounting_type,
                                                          is_active=True).first()


    @staticmethod
    def check_company_exists(id):
        '''
        Check the company key exists
        :param id: Company ID
        :return: Company Existance
        '''

        valid = True
        message = ""
        is_exists = Company.objects.filter(id=id).count()
        if is_exists == 0:
            valid = False
            message = 'RESOURCE_NOT_FOUND'
            return valid, message
        return valid, message

    @staticmethod
    def check_contact_exists(company, contact):
        valid = True
        message = ""
        is_contact_exists = Contact.objects.filter(id=contact, company=company).count()
        if is_contact_exists == 0:
            valid = False
            message = "RESOURCE_NOT_FOUND"
            return valid, message
        return valid, message

    @staticmethod
    def check_espressocontact_exists(company, contact):
        valid = True
        message = ""
        is_contact_exists = EspressoContact.objects.filter(contact=contact, company=company).count()
        if is_contact_exists == 0:
            valid = False
            message = "RESOURCE_NOT_FOUND"
            return valid, message
        return valid, message

    @staticmethod
    def check_user_exists(userid):
        valid = True
        message = ""
        is_user_exists = User.objects.filter(id=userid).count()
        if is_user_exists == 0:
            valid = False
            message = 'RESOURCE_NOT_FOUND'
            return valid, message
        return valid, message

    @staticmethod
    def revoke_token(token):
        revoke_endpoint = getDiscoveryDocument.revoke_endpoint
        auth_header = 'Basic ' + Utils.string_to_base64(settings.CLIENT_ID + ':' + settings.CLIENT_SECRET)
        headers = {'Accept': 'application/json', 'content-type': 'application/json', 'Authorization': auth_header}
        payload = {'token': token}
        r = requests.post(revoke_endpoint, json=payload, headers=headers)

        if r.status_code >= 500:
            return ErrorMessage.INTERNAL_SERVER_ERROR
        elif r.status_code >= 400:
            return 'Token is incorrect.'
        else:
            return 'Revoke successful'

    @staticmethod
    def get_bearer_token(auth_code):
        token_endpoint = getDiscoveryDocument.token_endpoint
        print('######### get bearer token token_endpoint ', token_endpoint)

        auth_header = 'Basic ' + Utils.string_to_base64(settings.CLIENT_ID + ':' + settings.CLIENT_SECRET)
        headers = {'Accept': 'application/json', 'content-type': 'application/x-www-form-urlencoded',
                   'Authorization': auth_header}

        payload = {
            'code': auth_code,
            'redirect_uri': settings.REDIRECT_URI,
            'grant_type': 'authorization_code'
        }
        print(payload)
        r = requests.post(token_endpoint, data=payload, headers=headers)

        if r.status_code != 200:
            print('######### get Bearer Token ', r.status_code, ' ', r.text)
            return r.text

        bearer_raw = json.loads(r.text)

        if 'id_token' in bearer_raw:
            idToken = idToken = bearer_raw['id_token']
        else:
            idToken = None

        return Bearer(bearer_raw['x_refresh_token_expires_in'], bearer_raw['access_token'], bearer_raw['token_type'],
                      bearer_raw['refresh_token'], bearer_raw['expires_in'], idToken=idToken)

    @staticmethod
    def get_bearer_token_from_refresh_token(refresh_Token):
        token_endpoint = getDiscoveryDocument.token_endpoint
        auth_header = 'Basic ' + Utils.string_to_base64(settings.CLIENT_ID + ':' + settings.CLIENT_SECRET)
        headers = {'Accept': 'application/json', 'content-type': 'application/x-www-form-urlencoded',
                   'Authorization': auth_header}
        payload = {
            'refresh_token': refresh_Token,
            'grant_type': 'refresh_token'
        }
        r = requests.post(token_endpoint, data=payload, headers=headers)
        bearer_raw = json.loads(r.text)

        if 'id_token' in bearer_raw:
            idToken = bearer_raw['id_token']
        else:
            idToken = None
        if 'error' in bearer_raw:
            return "failure"
        return Bearer(bearer_raw['x_refresh_token_expires_in'], bearer_raw['access_token'], bearer_raw['token_type'],
                      bearer_raw['refresh_token'], bearer_raw['expires_in'], idToken=idToken)

    @staticmethod
    def get_user_profile(access_token):
        auth_header = 'Bearer ' + str(access_token)
        headers = {'Accept': 'application/json', 'Authorization': auth_header,
                   'accept': 'application/json'}
        r = requests.get(settings.SANDBOX_PROFILE_URL, headers=headers)
        status_code = r.status_code
        response = json.loads(r.text)
        return response, status_code

    @staticmethod
    def get_company_info(access_token, realmId):
        route = '/v3/company/{0}/companyinfo/{0}'.format(realmId)
        auth_header = 'Bearer ' + str(access_token)
        headers = {'Authorization': auth_header,
                   'accept': 'application/json'}
        r = requests.get(settings.SANDBOX_QBO_BASEURL + route, headers=headers)
        status_code = r.status_code
        try:
            response = json.loads(r.text)
        except json.JSONDecodeError:
            response = None
        return response, status_code

    @staticmethod
    def get_trial_balance(access_token, realmId, query=''):
        route = '/v3/company/{}/reports/TrialBalance'.format(realmId) + query
        auth_header = 'Bearer ' + str(access_token)
        headers = {'Authorization': auth_header,
                   'accept': 'application/json'}

        r = requests.get(settings.SANDBOX_QBO_BASEURL + route, headers=headers)
        status_code = r.status_code
        try:
            response = json.loads(r.text)
        except json.JSONDecodeError:
            response = None

        return response, status_code

    @staticmethod
    def get_balance_sheet(access_token, realmId, query=''):
        route = '/v3/company/{}/reports/BalanceSheet'.format(realmId) + query
        auth_header = 'Bearer ' + str(access_token)
        headers = {'Authorization': auth_header,
                   'accept': 'application/json'}
        r = requests.get(settings.SANDBOX_QBO_BASEURL + route, headers=headers)
        status_code = r.status_code
        try:
            response = json.loads(r.text)
        except json.JSONDecodeError:
            response = None
        return response, status_code

    @staticmethod
    def getAccountList(access_token, realmId, query=''):
        route = '/v3/company/{}/reports/AccountList'.format(realmId) + query
        auth_header = 'Bearer ' + str(access_token)
        headers = {'Authorization': auth_header,
                   'accept': 'application/json'}
        r = requests.get(settings.SANDBOX_QBO_BASEURL + route, headers=headers)
        status_code = r.status_code
        try:
            response = json.loads(r.text)
        except json.JSONDecodeError:
            response = None

        return response, status_code

    @staticmethod
    def get_chart_of_accounts(access_token, realmId):
        route = '/v3/company/{}/query?query=select * from Account where Active IN (true,false) MAXRESULTS 1000'.format(realmId)
        auth_header = 'Bearer ' + access_token
        headers = {'Authorization': auth_header,
                   'accept': 'application/json', 'Content-type': 'application/json'}
        r = requests.get(settings.SANDBOX_QBO_BASEURL + route, headers=headers)
        status_code = r.status_code
        print(r.text)
        try:
            response = json.loads(r.text)
        except json.JSONDecodeError:
            response = None
        # print(response)
        return response, status_code

    @staticmethod
    def get_xero_auth(pk):
        auth_info = AccountingUtils.get_credentials_by_company(pk)
        auth={}
        secret_keys = Utils.get_access_keys(pk)
        if AccountingConfiguration.PRIVATE == secret_keys.xero_accounting_type:
            auth['consumer_key']= auth_info.accessToken
            auth['rsa_key'] = auth_info.accessSecretKey
        else:
            auth['oauth_token'] = auth_info.accessToken
            auth['oauth_token_secret'] = auth_info.accessSecretKey
            auth['oauth_authorization_expires_at'] = Utils.format_expiry_duration(auth_info.tokenAcitvatedOn)
            auth['oauth_expires_at'] = Utils.format_expiry_duration(auth_info.tokenExpiryON)
            access_key = Utils.get_access_keys(pk)
            auth['consumer_key'] = access_key.auth_key
            auth['consumer_secret'] = access_key.secret_key
            auth['verified'] = True
            auth['callback_uri'] = settings.XERO_CALL_BACK_URI

        return auth

    @staticmethod
    def refresh_xero_auth_token(pk):
        secret_keys = Utils.get_access_keys(pk)
        consumer_key = secret_keys.auth_key
        consumer_secret = secret_keys.secret_key
        credentials = PublicCredentials(consumer_key, consumer_secret)

        return



        # TODO: FISCAL YEAR CHANGE
    @staticmethod
    def get_curr_prior_fiscal_year_end(company):
        """
        Returns the current, and previous fiscal year end entries for the company. This info will be used to break
        up the trial balance into fiscal year blocks for the call to generate statements

        :param company:
        :return: dictionary of fiscal year end entries key'd as current and prior
        """

        current_and_prior_fye = {}
        # reverse sort, so the prior fiscal year end always comes next, after the current
        fiscal_year_end_list = FiscalYearEnd.objects.filter(company=company).order_by('-fye_start_date')

        print('^^^^^^^^^ got fye list')
        for index, fye in enumerate(fiscal_year_end_list):
            print('^^^^^^^^^^^^ index is ', index)
            if fye.is_active:
                print('^^^^^^^^^^^^^ setting current and prior when index is ', index)
                current_and_prior_fye["current"] = fye
                current_and_prior_fye["prior"] = fiscal_year_end_list[index + 1]
                break

        print("^^^^^^^^^ current is ", current_and_prior_fye["current"].fye_start_date, " to ",
              current_and_prior_fye["current"].fye_end_date)

        print("^^^^^^^^^ previous is ", current_and_prior_fye["prior"].fye_start_date, " to ",
              current_and_prior_fye["prior"].fye_end_date)

        return current_and_prior_fye

    # TODO: FISCAL YEAR CHANGE
    @staticmethod
    def spilt_input_to_chunk(data, fye_dict):
        print('^^^^^^^^^ splitting the data WHAT!')
        current_fiscal_year_tb = []
        previous_fiscal_year_tb = []

        for tb in data["Model"]["Financials"]["CustomerTrialBalance"]:
            year, month = tb["Period"].split('-')
            tbperiod = datetime.date(year=int(year), month=int(month), day=calendar.monthrange(int(year), int(month))[1])

            if tbperiod >= fye_dict["current"].fye_start_date and tbperiod <= fye_dict["current"].fye_end_date:
                print('### Current ### Adding ', tbperiod)
                current_fiscal_year_tb.append(tb)

            if tbperiod >= fye_dict["prior"].fye_start_date and tbperiod <= fye_dict["prior"].fye_end_date:
                print('### Previous ### Adding ', tbperiod)
                previous_fiscal_year_tb.append(tb)

        current_fiscal_year_data = copy.deepcopy(data)
        previous_fiscal_year_data = copy.deepcopy(data)

        current_fiscal_year_data["Model"]["Financials"]["CustomerTrialBalance"] = current_fiscal_year_tb
        previous_fiscal_year_data["Model"]["Financials"]["CustomerTrialBalance"] = previous_fiscal_year_tb
        return [current_fiscal_year_data, previous_fiscal_year_data]

    # for decoding ID Token
    @staticmethod
    def incorrect_padding(s):
        return (s + '=' * (4 - len(s) % 4))

    @staticmethod
    def string_to_base64(s):
        return base64.b64encode(bytes(s, 'utf-8')).decode()

    """
        Returns a securely generated random string.
        Source from the django.utils.crypto module.
    """

    @staticmethod
    def get_random_string(length,
                          allowed_chars='abcdefghijklmnopqrstuvwxyz'
                                        'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
        return ''.join(random.choice(allowed_chars) for i in range(length))

    """
        Create a random secret key.
        Source from the django.utils.crypto module.
    """

    @staticmethod
    def get_secret_key(self):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        return Utils.get_random_string(40, chars)

    @staticmethod
    def get_CSRF_token(request):
        token = request.session.get('csrfToken', None)
        if token is None:
            token = Utils.get_secret_key()
            request.session['csrfToken'] = token
        return token

    @staticmethod
    def redirect_response(url, params=False):
        '''
        This method for bind the status code and header information
        :param url:
        :return:
        '''
        if params:
            res = HttpResponse(url, status=301)
        else:
            res = HttpResponse(url, status=302)
        res['Location'] = url
        return res

    @staticmethod
    def get_company_details(id):
        """
        Gets a Company instance by ID
        """
        company = Company.objects.get(id=id)
        serializer = CompanySerializer(company, context={})
        return Response(serializer.data)

    @staticmethod
    def check_company_exist(id):
        """
        Check if company exist
        :return: return the company state
        """
        company = Company.objects.get(id=id)
        serializer = CompanyDetailSerializer(company)
        return Response(serializer.data)

    @staticmethod
    def get_login_status(id):
        """
        Get Login status
        :return: login status
        """
        company = AccountsUtils.get_company(id)
        login_status = AccountingUtils.get_status_object(company)
        if not login_status:
            return None
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        if login_status.created < (now - timedelta(minutes=5)):
            login_status.status = LoginInfo.FAILED
            login_status.save()
            print(LoginInfoSerializer(login_status).data)
        return Response(LoginInfoSerializer(login_status).data)

    @staticmethod
    def validate_email_address(email):
        """
        This method validates whether the input is an email address or not.
        """

        try:
            validate_email(email)
            return True
        except ValidationError:
            return False

    @staticmethod
    def send_mail(email, subject, body, html_message=None):
        try:
            if EMAIL_ENABLED:
                send_mail(
                    from_email=settings.EMAIL_HOST_USER,
                    subject=subject,
                    message=body,
                    recipient_list=email,
                    fail_silently=False,
                    html_message=html_message,
                )
                print("Mail Sent")
            else:
                print("EMAIL_ENABLED :", EMAIL_ENABLED)
        except Exception as e:
            print(e)
            print("Mail Fail to Sent")

    @staticmethod
    def generate_unique_token():
        return str(uuid.uuid4().hex)

    @staticmethod
    def send_error_tags(company, user, error_tags, response):
        user_mail = user.email
        admin_mail = settings.ADMIN_EMAIL
        company_data = Company.objects.get(pk=company)
        meta = CompanyMeta.objects.get(company=company)

        error_tags_table = ""
        json_body = json.dumps(response, indent=4, separators=(',', ': '), sort_keys=True)

        for tags in error_tags:
            error_tags_table += "<br>%s" % tags

        admin_html_body = ERROR_TAG_EMAIL_ADMIN_BODY % (
                          MONTHLY_REPORT_KEY_ERROR_ADMIN_EMAIL_BODY,
                          company_data.name, company_data.id, company_data.accounting_type,
                          meta.monthly_reporting_current_period, meta.monthly_reporting_next_period, error_tags_table,
                          json_body)

        user_html_body = ERROR_TAG_EMAIL_USER_BODY % (
                             user.username.title(),MONTHLY_REPORT_KEY_ERROR_USER_EMAIL_BODY,
                             company_data.name, company_data.accounting_type,
                             meta.monthly_reporting_current_period, meta.monthly_reporting_next_period,
                             error_tags_table)

        subject = MONTHLY_REPORT_KEY_ERROR_EMAIL_SUBJECT

        Utils.send_mail(email=[user_mail, ], body='', subject=subject, html_message=user_html_body)

        Utils.send_mail(email=[admin_mail, ], body='', subject=subject, html_message=admin_html_body)

        return

    @staticmethod
    def send_company_meta(user, choice):
        admin_mail = settings.ADMIN_EMAIL
        user_data = User.objects.filter(id=user.id).first()
        company = user_data.company_id
        company_data = Company.objects.get(pk=company)

        if choice is "META":
            html_body = COMPANY_META_NOT_FOUND_EMAIL_ADMIN % (
                            COMAPANY_META_EMAIL_BODY, company_data.name, company_data.id,
                            company_data.accounting_type)
            subject = COMAPANY_META_EMAIL_SUBJECT + company_data.name
            Utils.send_mail(email=[admin_mail, ], body='', subject=subject, html_message=html_body)

        elif choice is "PERIOD":
            html_body = COMPANY_PERIOD_NOT_FOUND_EMAIL_ADMIN % (
                            COMAPANY_CURRENT_REPORT_PERIOD_EMAIL_BODY, company_data.name, company_data.id,
                            company_data.accounting_type)
            subject = COMAPANY_CURRENT_REPORT_PERIOD_EMAIL_SUBJECT + company_data.name
            Utils.send_mail(email=[admin_mail, ], body='', subject=subject, html_message=html_body)

        return
    @staticmethod
    def send_company_misconfig(company, error):
        admin_mail = settings.ADMIN_EMAIL
        company_data = Company.objects.get(pk=company)
        html_body = COMPANY_MISCONFIG_EMAIL_ADMIN % (
                    COMPANY_MISCONFIG_EMAIL_BODY, company_data.name, company_data.id,
                    company_data.accounting_type,error)
        subject = COMPANY_MISCONFIG_EMAIL_SUBJECT + company_data.name
        Utils.send_mail(email=[admin_mail, ], body='', subject=subject, html_message=html_body)
        return

    @staticmethod
    def get_xero_public_credentials(stored_values):
        return PublicCredentials(consumer_key=stored_values['consumer_key'],
                      consumer_secret=stored_values['consumer_secret'],
                      callback_uri=stored_values['callback_uri'],
                      verified=stored_values['verified'],
                      oauth_token=stored_values['oauth_token'],
                      oauth_token_secret=stored_values['oauth_token_secret'],
                      oauth_expires_at=stored_values['oauth_expires_at'],
                      oauth_authorization_expires_at=stored_values[
                          'oauth_authorization_expires_at'],
                      )
    @staticmethod
    def get_xero_credentials(pk,**auth):
        secret_keys = Utils.get_access_keys(pk)
        if AccountingConfiguration.PRIVATE == secret_keys.xero_accounting_type:
            return PrivateCredentials(**auth)
        else:
            return PublicCredentials(**auth)