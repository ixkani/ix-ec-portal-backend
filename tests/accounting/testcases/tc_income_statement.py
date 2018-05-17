import os
import json

from rest_framework.test import APITestCase

from portalbackend.lendapi.reporting.models import FinancialStatementEntry
from portalbackend.validator.errormapping import ErrorMessage

from tests.utils import TestUtils
from tests.constants import ResponseCodeConstant, TestConstants, CompanyConstant, URLConstant



class _001_IncomeStatementTestCase(APITestCase):
    """
    Tests the IncomeStatement View
    """

    def setUp(self):
        self.superuser = TestUtils._create_superuser()

        self.company = TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        TestUtils._create_companymeta(self.company.id)

        self.user = TestUtils._create_user('ut_user001', self.company.id)

        self.login = TestUtils._admin_login(self.client)

        base_path = os.path.dirname(os.path.realpath(__file__))

        with open(base_path + '/sample_data/coa_sample_data.json') as file:
            self.coa_data = json.load(file)

        with open(base_path + '/sample_data/tb_sample_data.json') as file:
            self.tb_data = json.load(file)

        with open(base_path + '/sample_data/income_statement_sample_data.json') as file:
            self.is_data = json.load(file)

        TestUtils._create_default_mapping()
        TestUtils._create_finacial_tag_mapping()

        TestUtils._create_fiscal_year(self.company)
        TestUtils._post_with_args(self.client, URLConstant.ChartOfAccounts, self.company.id, self.coa_data)
        TestUtils._get_with_args(self.client, URLConstant.CoaMapView, self.company.id)
        TestUtils._post_with_args(self.client, URLConstant.TrialBalanceView, self.company.id, self.tb_data)

    def test_001_get_income_statement_success(self):
        """
        Getting all the income statement data without date parameter
        """

        TestUtils._get_with_args(self.client, URLConstant.Statement, self.company.id)
        code, response = TestUtils._get_with_args(self.client, URLConstant.IncomeStatementView, self.company.id)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)

    def test_002_get_income_statement_with_period_query_success(self):
        """
        Getting all the income statement data with date parameter
        """
        self.data = {
            "start_date": CompanyConstant.COMPANY_CURRENT_REPORT_PERIOD,
            "end_date": CompanyConstant.COMPANY_NEXT_REPORT_PERIOD,
        }

        TestUtils._get_with_args(self.client, URLConstant.Statement, self.company.id)
        code, response = TestUtils._get_with_args_and_query(self.client, URLConstant.IncomeStatementView,
                                                            self.company.id, self.data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)

    def test_003_get_income_statement_with_period_query_end_date_success(self):
        """
        Getting all the income statement data with end date only
        """
        self.data = {
            "end_date": CompanyConstant.COMPANY_CURRENT_REPORT_PERIOD,
        }

        TestUtils._get_with_args(self.client, URLConstant.Statement, self.company.id)
        code, response = TestUtils._get_with_args_and_query(self.client, URLConstant.IncomeStatementView,
                                                            self.company.id, self.data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)

    def test_004_get_income_statement_with_period_query_without_end_date_failure(self):
        """
        Getting all the income statement data without end date
        """
        self.data = {
            "start_date": CompanyConstant.COMPANY_CURRENT_REPORT_PERIOD
        }

        TestUtils._get_with_args(self.client, URLConstant.Statement, self.company.id)
        code, response = TestUtils._get_with_args_and_query(self.client, URLConstant.IncomeStatementView,
                                                            self.company.id, self.data)
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.MISSING_END_DATE))

    def test_005_get_income_statement_with_period_query_no_data_success(self):
        """
        Getting all the income statement data with date parameter without data
        """
        self.data = {
            "start_date": CompanyConstant.COMPANY_CURRENT_REPORT_PERIOD,
            "end_date": CompanyConstant.COMPANY_NEXT_REPORT_PERIOD,
        }

        code, response = TestUtils._get_with_args_and_query(self.client, URLConstant.IncomeStatementView,
                                                            self.company.id, self.data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.DATA_NOT_FOUND))

    def test_006_create_is_manual_post_success(self):
        """
        Create the Income statement with valid data
        """
        self.data = self.is_data

        code, response = TestUtils._post_with_args(self.client, URLConstant.IncomeStatementView, self.company.id,
                                                   self.data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(FinancialStatementEntry.objects.filter(company=self.company,
                                                               statement_type=FinancialStatementEntry.INCOME_STATEMENT).count() > 0)
        self.assertTrue(FinancialStatementEntry.objects.filter(company=self.company,
                                                               statement_type=FinancialStatementEntry.INCOME_STATEMENT,
                                                               entry_name='EBITDA').count() > 0)
        self.assertTrue(FinancialStatementEntry.objects.filter(company=self.company,
                                                               statement_type=FinancialStatementEntry.INCOME_STATEMENT,
                                                               entry_name='Gross Profit').count() > 0)
        self.assertTrue(FinancialStatementEntry.objects.filter(company=self.company,
                                                               statement_type=FinancialStatementEntry.INCOME_STATEMENT,
                                                               entry_name='Cost of Goods Sold').count() > 0)

    def test_007_create_is_manual_no_data_changes(self):
        """
        Create the Income statement with no data changes
        """
        self.data = self.is_data

        TestUtils._post_with_args(self.client, URLConstant.IncomeStatementView, self.company.id,
                                  self.data)
        code, response = TestUtils._post_with_args(self.client, URLConstant.IncomeStatementView, self.company.id,
                                                   self.data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.NO_DATA_CHANGES))

    def test_008_create_is_manual_post_invalid_company_failure(self):
        """
        Create the Income statement with valid data with invalid company
        """
        self.data = self.is_data
        code, response = TestUtils._post_with_args(self.client, URLConstant.IncomeStatementView,
                                                   TestConstants.INVALID_ID,
                                                   self.data)
        self.assertEqual(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.RESOURCE_NOT_FOUND))

    def test_009_create_is_manual_post_empty_value_success(self):
        """
        Create the Income statement with empty data
        """
        self.data = {}
        code, response = TestUtils._post_with_args(self.client, URLConstant.IncomeStatementView, self.company.id,
                                                   self.data)
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.DATA_PARSING_ISSUE))

    def test_010_delete_is_data_success(self):
        """
        delete the Income statement with data
        """
        self.data = self.is_data

        TestUtils._post_with_args(self.client, URLConstant.IncomeStatementView, self.company.id,
                                  self.data)
        code, response = TestUtils._delete(self.client, URLConstant.IncomeStatementView, self.company.id)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.DELETED_SUCCESSFULLY))

    def test_011_delete_is_data_without_data_success(self):
        """
        delete the Income statement without data
        """

        code, response = TestUtils._delete(self.client, URLConstant.IncomeStatementView, self.company.id)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.DATA_NOT_FOUND))

    def test_012_delete_is_data_unauthorized_access_failure(self):
        """
        delete the Income statement with unauthorized access
        """
        self.client.logout()
        self.login = TestUtils._user_login(self.client, "ut_user001")
        code, response = TestUtils._delete(self.client, URLConstant.IncomeStatementView, self.company.id)
        self.assertEquals(code, ResponseCodeConstant.UNAUTHORIZED_ACCESS_401)
        TestUtils._check_response_message(response, ErrorMessage.UNAUTHORIZED_ACCESS)
