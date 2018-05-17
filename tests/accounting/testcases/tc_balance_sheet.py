import os
import json

from rest_framework.test import APITestCase

from tests.utils import TestUtils
from tests.constants import ResponseCodeConstant, TestConstants, CompanyConstant, URLConstant

from portalbackend.lendapi.reporting.models import FinancialStatementEntry
from portalbackend.validator.errormapping import ErrorMessage


class _001_BalanceSheetTestCase(APITestCase):
    """
    Tests the BalanceSheet View
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

        with open(base_path + '/sample_data/balance_sheet_sample_data.json') as file:
            self.is_data = json.load(file)

        TestUtils._create_default_mapping()
        TestUtils._create_finacial_tag_mapping()

        TestUtils._create_fiscal_year(self.company)

        TestUtils._post_with_args(self.client, URLConstant.ChartOfAccounts, self.company.id, self.coa_data)
        TestUtils._get_with_args(self.client, URLConstant.CoaMapView, self.company.id)
        TestUtils._post_with_args(self.client, URLConstant.TrialBalanceView, self.company.id, self.tb_data)

    def test_001_get_balance_sheet_success(self):
        """
        Getting all the balance sheet data without date limit
        """

        TestUtils._get_with_args(self.client, URLConstant.Statement, self.company.id)
        code, response = TestUtils._get_with_args(self.client, URLConstant.BalanceSheetView, self.company.id)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)

    def test_002_get_balance_sheet_with_period_query_success(self):
        """
        Getting all balance sheet the data with date parameter
        """
        self.data = {
            "start_date": CompanyConstant.COMPANY_CURRENT_REPORT_PERIOD,
            "end_date": CompanyConstant.COMPANY_NEXT_REPORT_PERIOD,
        }

        TestUtils._get_with_args(self.client, URLConstant.Statement, self.company.id)
        code, response = TestUtils._get_with_args_and_query(self.client, URLConstant.BalanceSheetView,
                                                            self.company.id, self.data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)

    def test_003_get_balance_sheet_with_period_query_end_date_success(self):
        """
        Getting all the balance sheet data with end date only
        """
        self.data = {
            "end_date": CompanyConstant.COMPANY_CURRENT_REPORT_PERIOD,
        }

        TestUtils._get_with_args(self.client, URLConstant.Statement, self.company.id)
        code, response = TestUtils._get_with_args_and_query(self.client, URLConstant.BalanceSheetView,
                                                            self.company.id, self.data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)

    def test_004_get_balance_sheet_with_period_query_without_end_date_failure(self):
        """
        Getting all the balance sheet data without end date
        """
        self.data = {
            "start_date": CompanyConstant.COMPANY_CURRENT_REPORT_PERIOD
        }

        TestUtils._get_with_args(self.client, URLConstant.Statement, self.company.id)
        code, response = TestUtils._get_with_args_and_query(self.client, URLConstant.BalanceSheetView,
                                                            self.company.id, self.data)
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.MISSING_END_DATE))

    def test_005_get_balance_sheet_with_period_query_no_data_success(self):
        """
        Getting all the balance sheet data with date parameter and without data
        """
        self.data = {
            "start_date": CompanyConstant.COMPANY_CURRENT_REPORT_PERIOD,
            "end_date": CompanyConstant.COMPANY_NEXT_REPORT_PERIOD,
        }

        code, response = TestUtils._get_with_args_and_query(self.client, URLConstant.BalanceSheetView,
                                                            self.company.id, self.data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.DATA_NOT_FOUND))

    def test_006_create_bs_manual_post_success(self):
        """
        Create the Balance sheet with valid data
        """
        self.data = self.is_data

        code, response = TestUtils._post_with_args(self.client, URLConstant.BalanceSheetView, self.company.id,
                                                   self.data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(FinancialStatementEntry.objects.filter(company=self.company,
                                                               statement_type=FinancialStatementEntry.BALANCE_SHEET).count() > 0)
        self.assertTrue(FinancialStatementEntry.objects.filter(company=self.company,
                                                               statement_type=FinancialStatementEntry.BALANCE_SHEET,
                                                               entry_name='Other Liabilities').count() > 0)
        self.assertTrue(FinancialStatementEntry.objects.filter(company=self.company,
                                                               statement_type=FinancialStatementEntry.BALANCE_SHEET,
                                                               entry_name='Accounts Payable and Accrued Liabilities').count() > 0)
        self.assertTrue(FinancialStatementEntry.objects.filter(company=self.company,
                                                               statement_type=FinancialStatementEntry.BALANCE_SHEET,
                                                               entry_name='Accounts Receivables').count() > 0)

    def test_006_create_bs_manual_no_data_changes(self):
        """
        Create the Balance sheet with no data changes
        """
        self.data = self.is_data

        TestUtils._post_with_args(self.client, URLConstant.BalanceSheetView, self.company.id,
                                  self.data)
        code, response = TestUtils._post_with_args(self.client, URLConstant.BalanceSheetView, self.company.id,
                                                   self.data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.NO_DATA_CHANGES))

    def test_007_create_bs_manual_post_invalid_company_failure(self):
        """
        Create the Balance sheet with valid data and invalid company
        """
        self.data = self.is_data
        code, response = TestUtils._post_with_args(self.client, URLConstant.BalanceSheetView,
                                                   TestConstants.INVALID_ID,
                                                   self.data)
        self.assertEqual(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.RESOURCE_NOT_FOUND))

    def test_008_create_bs_manual_post_empty_value_success(self):
        """
        Create the Balance sheet with empty value
        """
        self.data = {}
        code, response = TestUtils._post_with_args(self.client, URLConstant.BalanceSheetView, self.company.id,
                                                   self.data)
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.DATA_PARSING_ISSUE))

    def test_009_delete_bs_data_success(self):
        """
        Delete the Balance sheet with data
        """
        self.data = self.is_data

        TestUtils._post_with_args(self.client, URLConstant.BalanceSheetView, self.company.id,
                                  self.data)
        code, response = TestUtils._delete(self.client, URLConstant.BalanceSheetView, self.company.id)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.DELETED_SUCCESSFULLY))

    def test_010_delete_bs_data_without_data_success(self):
        """
        Delete the Balance sheet without data
        """

        code, response = TestUtils._delete(self.client, URLConstant.BalanceSheetView, self.company.id)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.DATA_NOT_FOUND))

    def test_011_delete_bs_data_unauthorized_access_failure(self):
        """
        Delete the Balance sheet without unauthorized access
        """
        self.client.logout()
        self.login = TestUtils._user_login(self.client, "ut_user001")
        code, response = TestUtils._delete(self.client, URLConstant.BalanceSheetView, self.company.id)
        self.assertEquals(code, ResponseCodeConstant.UNAUTHORIZED_ACCESS_401)
        TestUtils._check_response_message(response, ErrorMessage.UNAUTHORIZED_ACCESS)
