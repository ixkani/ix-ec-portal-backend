import os
import json

from rest_framework.test import APITestCase

from portalbackend.lendapi.accounting.models import CoA
from portalbackend.lendapi.accounts.models import Company
from portalbackend.validator.errormapping import ErrorMessage

from tests.utils import TestUtils
from tests.constants import ResponseCodeConstant, TestConstants, CompanyConstant, ResponseMessageConstant, URLConstant, \
    AccountingConstant


class _001_ChartofAccountsTestCase(APITestCase):
    """
    Tests the ChartofAccounts View
    """

    def setUp(self):
        self.userid = ''
        self.superuser = TestUtils._create_superuser()
        self.company = TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        TestUtils._create_companymeta(self.company.id)
        self.user = TestUtils._create_user('ut_user001', self.company.id)
        self.login = TestUtils._admin_login(self.client)
        TestUtils._create_accounting_configuration(Company.QUICKBOOKS)
        base_path = os.path.dirname(os.path.realpath(__file__))
        with open(base_path + '/sample_data/coa_sample_data.json') as file:
            self.csv_data = json.load(file)
        TestUtils._create_default_mapping()
        TestUtils._create_finacial_tag_mapping()

    def test_001_create_coa_manual_post_success(self):
        """
        Create the chart of accounts with valid data
        """
        self.data = self.csv_data
        code, response = TestUtils._post_with_args(self.client, URLConstant.ChartOfAccounts, self.company.id, self.data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(CoA.objects.filter(company=self.company).count() > 0)
        self.assertTrue(CoA.objects.filter(company=self.company, gl_account_name="Cost of Goods Sold").count() > 0)
        self.assertTrue(CoA.objects.filter(company=self.company, gl_account_name="Visa Credit Card").count() > 0)

    def test_002_create_coa_manual_post_invalid_company_failure(self):
        """
        Create the chart of accounts with valid data with not existing company id
        """
        self.data = self.csv_data
        code, response = TestUtils._post_with_args(self.client, URLConstant.ChartOfAccounts, TestConstants.INVALID_ID,
                                                   self.data)
        self.assertEqual(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.RESOURCE_NOT_FOUND))

    def test_003_create_coa_manual_post_without_data_failure(self):
        """
        Create the chart of accounts with without data
        """
        self.data = {}
        code, response = TestUtils._post_with_args(self.client, URLConstant.ChartOfAccounts, self.company.id, self.data)
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.DATA_PARSING_ISSUE))

    def test_004_create_coa_manual_post_success(self):
        """
        Create the chart of accounts with existing data
        """
        self.data = self.csv_data
        TestUtils._post_with_args(self.client, URLConstant.ChartOfAccounts, self.company.id, self.data)
        code, response = TestUtils._post_with_args(self.client, URLConstant.ChartOfAccounts, self.company.id, self.data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.NO_DATA_CHANGES))
        self.assertTrue(CoA.objects.filter(company=self.company).count() > 0)
        self.assertTrue(CoA.objects.filter(company=self.company, gl_account_name="Cost of Goods Sold").count() > 0)
        self.assertTrue(CoA.objects.filter(company=self.company, gl_account_name="Visa Credit Card").count() > 0)

    def test_005_coa_csv_upload_qbo_success(self):
        """
        Create the chart of accounts for quickbooks using CSV
        """
        code, response = TestUtils._file_upload_csv(URLConstant.ChartOfAccounts, self.company.id, 'QB-sampleCOAcsv.CSV',
                                                    AccountingConstant.CHART_OF_ACCOUNTS)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(CoA.objects.filter(company=self.company).count() > 0)

    def test_005_coa_csv_upload_qbo_invalid_file_format_failure(self):
        """
        Create the chart of accounts for quickbooks using invalid file format
        """
        code, response = TestUtils._file_upload_csv(URLConstant.ChartOfAccounts, self.company.id,
                                                    'coa_sample_data.json', AccountingConstant.CHART_OF_ACCOUNTS)
        self.assertEqual(code, ResponseCodeConstant.INVALID_FILE_FORMAT)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.INVALID_FILE_FORMAT))

    def test_006_coa_csv_upload_sage_success(self):
        """
        Create the chart of accounts for sage using CSV
        """
        self.company.accounting_type = Company.SAGE
        self.company.save()
        code, response = TestUtils._file_upload_csv(URLConstant.ChartOfAccounts, self.company.id, 'SAGE-sampleCOA.csv',
                                                    AccountingConstant.CHART_OF_ACCOUNTS)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(CoA.objects.filter(company=self.company).count() > 0)

    def test_007_delete_coa_success(self):
        """
        deletes the chart of accounts with existing data
        """
        self.data = self.csv_data
        TestUtils._post_with_args(self.client, URLConstant.ChartOfAccounts, self.company.id, self.data)

        code, response = TestUtils._delete(self.client, URLConstant.ChartOfAccounts, self.company.id)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.DELETED_SUCCESSFULLY))

    def test_008_delete_coa_no_data_available_failure(self):
        """
        deletes the chart of accounts with no data available
        """

        code, response = TestUtils._delete(self.client, URLConstant.ChartOfAccounts, self.company.id)
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.OBJECT_RESOURCE_NOT_FOUND))

    def test_009_delete_coa_invalid_company_failure(self):
        """
        deletes the chart of accounts with invalid company
        """

        code, response = TestUtils._delete(self.client, URLConstant.ChartOfAccounts, TestConstants.INVALID_ID)
        self.assertEqual(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.RESOURCE_NOT_FOUND))
