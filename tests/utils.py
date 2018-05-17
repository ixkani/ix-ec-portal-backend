import csv
import datetime
import json

import os
import pyotp
import re

from coreapi.utils import File
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import force_authenticate

from portalbackend.lendapi.accounting.models import AccountingOauth2, DefaultAccountTagMapping, \
    FinancialStatementEntryTag
from portalbackend.lendapi.accounts.models import User, Company, CompanyMeta, ScheduledMaintenance, Contact, \
    EspressoContact, AccountingConfiguration, FiscalYearEnd
from portalbackend.lendapi.reporting.models import MonthlyReport, QuestionCategory, Question, Answer
from portalbackend.lendapi.v1.accounting.utils import Utils
from portalbackend.lendapi.v1.accounting.views import ChartOfAccounts, TrialBalanceView
from portalbackend.lendapi.v1.accounts.views import UserList, UserDetail, LoginView
from django.utils.timezone import utc
from django.test.client import RequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile
from tests.constants import TestConstants, CompanyConstant, UserConstant, ContactConstant, AccountingConstant


class TestUtils(object):

    @staticmethod
    def _admin_login(client):
        username = UserConstant.ADMIN_USERNAME
        password = UserConstant.ADMIN_PASSWORD
        client.login(username=username, password=password)

    @staticmethod
    def _user_login(client, username):
        client.logout()
        client.login(username=username, password=UserConstant.USER_PASSWORD)

    @staticmethod
    def _create_superuser():
        username = UserConstant.ADMIN_USERNAME
        password = UserConstant.ADMIN_PASSWORD
        email = UserConstant.ADMIN_EMAIL
        user = User.objects.create_superuser(username, email, password)
        user.save()
        return user

    @staticmethod
    def _create_user(username, company_id):
        company = Company.objects.filter(id=company_id).first()
        user = User.objects.create_user(username, UserConstant.USER_EMAIL, UserConstant.USER_PASSWORD)
        user.company = company
        user.save()
        return user

    @staticmethod
    @override_settings(APPEND_SLASH=True)
    def _post(client, string, data):
        response = client.post(reverse(string), data, format='json', secure=TestConstants.SECURE_CONNECTION,
                               HTTP_HOST=TestConstants.HOST_URL)
        return response.status_code, response.data

    @staticmethod
    def _post_with_args(client, string, args, data):
        if type(args) is list:
            response = client.post(reverse(string, args=args), data,format='json', secure=TestConstants.SECURE_CONNECTION,
                               HTTP_HOST=TestConstants.HOST_URL)
        else:
            response = client.post(reverse(string, args=[args]), data,format='json', secure=TestConstants.SECURE_CONNECTION,
                               HTTP_HOST=TestConstants.HOST_URL)
        return response.status_code, response.data

    @staticmethod
    def _get(client, string, ):
        response = client.get(reverse(string))
        return response.status_code, response.data

    @staticmethod
    def _get_with_args(client, string, args):
        if type(args) is list:
            response = client.get(reverse(string, args=args),format='json', secure=TestConstants.SECURE_CONNECTION,
                               HTTP_HOST=TestConstants.HOST_URL)
        else:
            response = client.get(reverse(string, args=[args]),format='json', secure=TestConstants.SECURE_CONNECTION,
                               HTTP_HOST=TestConstants.HOST_URL)
        return response.status_code, response.data

    @staticmethod
    def _get_with_args_and_query(client, string, args, data):
        if type(args) is list:
            response = client.get(reverse(string, args=args), data,format='json', secure=TestConstants.SECURE_CONNECTION,
                               HTTP_HOST=TestConstants.HOST_URL)
        else:
            response = client.get(reverse(string, args=[args]), data,format='json', secure=TestConstants.SECURE_CONNECTION,
                               HTTP_HOST=TestConstants.HOST_URL)
        return response.status_code, response.data

    @staticmethod
    def _put(client, string, data):
        response = client.put(reverse(string), data,format='json', secure=TestConstants.SECURE_CONNECTION,
                               HTTP_HOST=TestConstants.HOST_URL)
        return response.status_code, response.data

    @staticmethod
    def _put_with_args(client, string, args, data):
        if type(args) is list:
            response = client.put(reverse(string, args=args), data,format='json', secure=TestConstants.SECURE_CONNECTION,
                               HTTP_HOST=TestConstants.HOST_URL)
        else:
            response = client.put(reverse(string, args=[args]), data,format='json', secure=TestConstants.SECURE_CONNECTION,
                               HTTP_HOST=TestConstants.HOST_URL)
        return response.status_code, response.data

    @staticmethod
    def _delete(client, string, args):
        if type(args) is list:
            response = client.delete(reverse(string, args=args),format='json', secure=TestConstants.SECURE_CONNECTION,
                               HTTP_HOST=TestConstants.HOST_URL)
        else:
            response = client.delete(reverse(string, args=[args]),format='json', secure=TestConstants.SECURE_CONNECTION,
                               HTTP_HOST=TestConstants.HOST_URL)
        return response.status_code, response.data

    @staticmethod
    def _file_upload_csv( string, args, file_name,account):

        base_path = os.path.dirname(os.path.realpath(__file__))
        base_path += '/accounting/testcases/sample_data/'

        data = open(base_path + file_name, 'rb')

        data = SimpleUploadedFile(content = data.read(),name = data.name,content_type='multipart/form-data')

        factory = RequestFactory()
        user = User.objects.get(username=UserConstant.ADMIN_USERNAME)

        if account is AccountingConstant.CHART_OF_ACCOUNTS:
            view = ChartOfAccounts.as_view()
        else :
            view = TrialBalanceView.as_view()

        content_type = 'multipart/form-data'
        headers= {
            'HTTP_HOST': TestConstants.HOST_URL,
            'HTTP_CONTENT_TYPE': content_type,
            'HTTP_CONTENT_DISPOSITION': 'attachment; filename='+file_name}

        request = factory.post(reverse(string, args=[args]),{'file': data},secure = True,
                               **headers)

        force_authenticate(request, user=user)
        response = view(request, args)

        return response.status_code, response.data


    @staticmethod
    def _create_company(id, name):
        company = Company.objects.create(id=id, name=name, external_id=CompanyConstant.DEFAULT_COMPANY_EXTERNALID,
                                         website=CompanyConstant.DEFAULT_COMPANY_WEBSITE,
                                         employee_count=CompanyConstant.DEFAULT_COMPANY_EMPLOYEE_COUNT)
        company.save()
        return company

    @staticmethod
    def _create_companymeta(id):
        company_meta = CompanyMeta.objects.get(company_id=id)
        company_meta.monthly_reporting_current_period = CompanyConstant.COMPANY_CURRENT_REPORT_PERIOD
        company_meta.monthly_reporting_next_period = CompanyConstant.COMPANY_NEXT_REPORT_PERIOD
        company_meta.save()
        return company_meta

    @staticmethod
    def _create_contact(id):
        company = Company.objects.get(id=1)
        contact = Contact.objects.create(
            company=company,
            first_name=ContactConstant.DEFAULT_CONTACT_FIRST_NAME,
            external_id=ContactConstant.DEFAULT_CONTACT_EXTERNALID,
            last_name=ContactConstant.DEFAULT_CONTACT_LAST_NAME,
            email=ContactConstant.DEFAULT_CONTACT_EMAIL,
            title=ContactConstant.DEFAULT_CONTACT_TITLE
        )
        contact.save()

    @staticmethod
    def _create_espresso_contact(id, cid):
        company = Company.objects.get(id=id)
        contact = Contact.objects.get(id=cid)
        espresso_contact = EspressoContact.objects.create(company=company, contact=contact)
        espresso_contact.save()

    @staticmethod
    def _create_scheduled_maintenance():
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        scheduled_maintenance = ScheduledMaintenance.objects.create(
            message="Sever under Maintaince",
            start_time=now,
            end_time=now + datetime.timedelta(hours=1),
            is_active=True
        )
        scheduled_maintenance.save()

    @staticmethod
    def _create_accounting_configuration(type):
        if type == AccountingConfiguration.QUICKBOOKS:
            client_id = "Q0W1osEOriGM0rwlt7ZBE2ArpDAuczZyDxUmQyx6neVBbU4lkI"
            client_secret = "RPHtn6oWjCsQuwYyi5j0Jh2M8hl93LsYk934pR81"
        else:
            client_id = "KHEGRFHVARTOKMGELZ9DYQFOGK1DCH"
            client_secret = "5JXM0W7K9HDAKOWQJLNNVRA2ZWSY40"

        accounting_configuration = AccountingConfiguration.objects.create(
            accounting_type=type,
            client_id=client_id,
            client_secret=client_secret,
            is_active=True
        )
        accounting_configuration.save()

    @staticmethod
    def _create_default_mapping():
        base_path = os.path.dirname(os.path.realpath(__file__))
        filename = base_path + '/accounting/testcases/sample_data/default_tag_mapping.csv'
        with open(filename, newline='') as csvfile:
            reader = list(csv.reader(csvfile, delimiter=',', quotechar='|'))
            for row in reader[1:]:
                tag = DefaultAccountTagMapping.objects.create(
                    software=row[1],
                    account_category=row[2],
                    default_map_id=row[3],
                    default_map_name=row[4],
                )
                tag.save()

    @staticmethod
    def _delete_default_mapping():
        tag = DefaultAccountTagMapping.objects.all()
        tag.delete()

    @staticmethod
    def _create_finacial_tag_mapping():
        base_path = os.path.dirname(os.path.realpath(__file__))
        filename = base_path + '/accounting/testcases/sample_data/finacial_tag_mapping.csv'
        with open(filename, newline='') as csvfile:
            reader = list(csv.reader(csvfile, delimiter=',', quotechar='|'))
            for row in reader[1:]:
                tag = FinancialStatementEntryTag.objects.create(
                    tag_id=row[1],
                    name=row[7],
                    short_label=row[2],
                    description=row[3],
                    tag_category=row[4],
                    abstract=row[5].lower() == 'true',
                    formula=row[6],
                    sort_order=row[8],
                    tag_group=row[11],
                    is_total_row=row[9].lower() == 'true',
                    all_sight_name=row[10],
                )
                tag.save()

    @staticmethod
    def _delete_question_data():
        QuestionCategory.objects.all().delete()
        Question.objects.all().delete()

    @staticmethod
    def _create_question_catagory():
        base_path = os.path.dirname(os.path.realpath(__file__))
        filename = base_path + '/reporting/testcases/sample_data/question_catagory.csv'
        with open(filename, newline='') as csvfile:
            reader = list(csv.reader(csvfile, delimiter=',', quotechar='|'))
            for row in reader[1:]:
                entry = QuestionCategory.objects.create(
                    id = row[0],
                    group_name=row[1],
                    is_active=row[2].lower() == 'true',
                    purpose=row[3]
                )
                entry.save()

    @staticmethod
    def _create_question(company):
        base_path = os.path.dirname(os.path.realpath(__file__))
        filename = base_path + '/reporting/testcases/sample_data/question.csv'
        with open(filename, newline='') as csvfile:
            reader = list(csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True))
            for row in reader[1:]:
                question = Question.objects.create(
                    next_question_if=row[1],
                    question_text=row[2],
                    question_choices=row[3] if row[3] != '' else '{}',
                    short_tag=row[4],
                    answer_data_type=row[5],
                    answer_validation_regex=row[6],
                    ask_order=row[7],
                    show_on_ui=row[8].lower() == 'true',
                    common_to_all_companies=row[9].lower() == 'true',
                    company=company,
                    next_question_id=row[11],
                    question_category_id=row[12],
                )
                question.save()

    @staticmethod
    def _create_fiscal_year(company):
        prev_year = FiscalYearEnd.objects.create(
            company=company,
            fye_start_date=CompanyConstant.PREV_FISCAL_YEAR_START_DATE,
            fye_end_date=CompanyConstant.PREV_FISCAL_YEAR_END_DATE,
            label=CompanyConstant.PREV_FISCAl_YEAR_LABEL,
            is_active=False,
        )
        prev_year.save()
        this_year = FiscalYearEnd.objects.create(
            company=company,
            fye_start_date=CompanyConstant.CUR_FISCAL_YEAR_START_DATE,
            fye_end_date=CompanyConstant.CUR_FISCAL_YEAR_END_DATE,
            label=CompanyConstant.CUR_FISCAl_YEAR_LABEL,
            is_active=True,
        )
        this_year.save()

    @staticmethod
    def _create_monthly_report(company):
        report = MonthlyReport.objects.create(
            company=company,
            status=MonthlyReport.IN_PROGRESS,
            period_ending=datetime.date(2016, 10, 31),
            due_date=datetime.date(2016, 10, 31)
        )
        report.save()
        return report

    @staticmethod
    def _create_answer(question,company,report,answer):
        TestUtils._create_question_catagory()
        TestUtils._create_question(company)
        test_answer = Answer.objects.create(
            question = Question.objects.all().first(),
            company = company,
            monthly_report = report ,
            answer = answer,
        )
        test_answer.save()
        return test_answer

    @staticmethod
    def _check_ledger_values(response):
        b_s = response['result']['Model']['Financials']['BalanceSheet'][0]

        total_cur_assets = b_s['1499'] == b_s['1000'] + b_s['1100'] + b_s['1150'] + b_s['1200']
        total_assets = b_s['1999'] == b_s['1499'] + b_s['1500'] + b_s['1600'] + b_s['1700']
        total_cur_liabilities = b_s['2199'] == b_s['2000'] + b_s['2050'] + b_s['2100'] + b_s['2150']
        total_liabilities = b_s['2999'] == b_s['2199'] + b_s['2500'] + b_s['2600'] + b_s['2700'] + b_s['2800'] + b_s[
            '2900']
        total_equity = b_s['3998'] == b_s['3000'] + b_s['3100'] + b_s['3200'] + b_s['3900'] + b_s['3997']
        total_liabilities_and_equity = b_s['3999'] == b_s['3998'] + b_s['2999']

        balance_sheet = total_cur_assets and total_assets and total_cur_liabilities and total_liabilities and total_equity and total_liabilities_and_equity

        i_s = response['result']['Model']['Financials']['IncomeStatement'][0]

        total_revenues = i_s['4900'] == i_s['4000'] + i_s['4500']
        gross_profit = i_s['5999'] == i_s['4900'] - i_s['5000']
        EBITDA = i_s['6699'] == i_s['5999'] - i_s['6695']
        net_income = i_s['6900'] == i_s['6699'] - i_s['6710'] - i_s['6720'] - i_s['6730'] - i_s['6740']

        income_statement = total_revenues and gross_profit and EBITDA and net_income

        return balance_sheet and income_statement

    @staticmethod
    def _check_credit_debit_values(response):
        b_s = response['result']['Model']['Financials']['BalanceSheet'][0]
        return abs(b_s['1999'] - b_s['3999']) < TestConstants.UNBALANCED_THRESHOLD

    @staticmethod
    def _delete_company_meta(company_id):
        meta = CompanyMeta.objects.get(company_id=company_id)
        meta.delete()

    @staticmethod
    def _update_scheduled_maintenance(is_active):
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        scheduled_maintenance = ScheduledMaintenance.objects.all()[0]
        scheduled_maintenance.end_time = now
        scheduled_maintenance.is_active = is_active
        scheduled_maintenance.save()

    @staticmethod
    def _delete_scheduled_maintenance():
        scheduled_maintenance = ScheduledMaintenance.objects.all()[0]
        scheduled_maintenance.delete()

    @staticmethod
    def _get_Totp(code):
        return pyotp.TOTP(code).now()

    @staticmethod
    def _check_response_message(response, message):
        return response['message'] == message

    @staticmethod
    def _check_response_detail(response, message):
        return response['detail'] == message

    @staticmethod
    def _check_response_value(response, key, value):
        return response['result'][key] == value

    @staticmethod
    def _check_response_key_success(response, key):
        return key in response['result']

    @staticmethod
    def _check_response_key_error(response, key):
        return key in response['errors']

    @staticmethod
    def _retrieve_redirect_response_url(response):
        """
        parses 302 response object.
        Returns redirect url, parsed by regex.
        """
        new_url = re.search(
            "(?P<url>https?://[^\s]+)",
            str(response)).group("url")
        return new_url[:-2]
