import os
import json

from rest_framework.test import APITestCase

from portalbackend.lendapi.accounting.models import TrialBalance
from portalbackend.lendapi.accounts.models import Company
from portalbackend.validator.errormapping import ErrorMessage

from tests.utils import TestUtils
from tests.constants import ResponseCodeConstant, TestConstants, CompanyConstant, URLConstant, \
    AccountingConstant


class _001_TrailBalanceTestCase(APITestCase):
    """
    Tests the Trail Balance View
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
        with open(base_path + '/sample_data/tb_sample_data.json') as file:
            self.tb_data = json.load(file)
        TestUtils._create_default_mapping()
        TestUtils._create_finacial_tag_mapping()

    def test_001_tb_csv_upload_qbo_success(self):
        """
        Create the Trail balance for quickbooks using CSV
        """
        code, response = TestUtils._file_upload_csv(URLConstant.TrialBalanceView, self.company.id,
                                                    'QB_TrialBalance.csv',
                                                    AccountingConstant.TRIAL_BALANCE)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TrialBalance.objects.filter(company=self.company).count() > 0)

    def test_002_tb_csv_upload_sage_success(self):
        """
        Create the Trail balance for sage using CSV
        """
        self.company.accounting_type = Company.SAGE
        self.company.save()
        code, response = TestUtils._file_upload_csv(URLConstant.TrialBalanceView, self.company.id, 'Sage-sampleTB.csv',
                                                    AccountingConstant.TRIAL_BALANCE)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TrialBalance.objects.filter(company=self.company).count() > 0)

    def test_003_tb_csv_upload_qbo_invalid_date_failure(self):
        """
        Create the Trail balance for quickbooks using CSV with invalid date
        """
        code, response = TestUtils._file_upload_csv(URLConstant.TrialBalanceView, self.company.id,
                                                    'QB_TrialBalance_invalid_date.csv',
                                                    AccountingConstant.TRIAL_BALANCE)
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.INVALID_TB_DATE))

    def test_004_tb_csv_upload_qbo_invalid_file_format_failure(self):
        """
        Create the Trail balance for quickbooks using CSV with invalid file format
        """
        code, response = TestUtils._file_upload_csv(URLConstant.TrialBalanceView, self.company.id,
                                                    'tb_sample_data.json',
                                                    AccountingConstant.TRIAL_BALANCE)
        self.assertEqual(code, ResponseCodeConstant.INVALID_FILE_FORMAT)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.INVALID_FILE_FORMAT))

    def test_005_create_tb_manual_post_success(self):
        """
        Create the Trial Balance with valid data
        """
        self.data = self.tb_data
        code, response = TestUtils._post_with_args(self.client, URLConstant.TrialBalanceView, self.company.id,
                                                   self.data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TrialBalance.objects.filter(company=self.company).count() > 0)
        self.assertTrue(TrialBalance.objects.filter(company=self.company, gl_account_name="Chequing").count() > 0)
        self.assertTrue(
            TrialBalance.objects.filter(company=self.company, gl_account_name="Accounts Receivable").count() > 0)

    def test_006_create_tb_manual_post_invalid_company_failure(self):
        """
        Create the Trial Balance with valid data and not existing company id
        """
        self.data = self.tb_data
        code, response = TestUtils._post_with_args(self.client, URLConstant.TrialBalanceView, TestConstants.INVALID_ID,
                                                   self.data)
        self.assertEqual(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.RESOURCE_NOT_FOUND))

    def test_007_create_tb_manual_post_without_data_failure(self):
        """
        Create the Trial Balance with without data
        """
        self.data = {}
        code, response = TestUtils._post_with_args(self.client, URLConstant.TrialBalanceView, self.company.id,
                                                   self.data)
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.DATA_PARSING_ISSUE))

    def test_008_delete_tb_success(self):
        """
        Deletes the Trial Balance
        """
        self.data = self.tb_data
        TestUtils._post_with_args(self.client, URLConstant.TrialBalanceView, self.company.id, self.data)

        code, response = TestUtils._delete(self.client, URLConstant.TrialBalanceView, self.company.id)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.DELETED_SUCCESSFULLY))

    def test_009_delete_tb_no_data_available_failure(self):
        """
        Deletes the Trial Balance with no data available
        """

        code, response = TestUtils._delete(self.client, URLConstant.TrialBalanceView, self.company.id)
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.OBJECT_RESOURCE_NOT_FOUND))

    def test_010_delete_tb_invalid_company_failure(self):
        """
        Deletes the Trial Balance with invalid company
        """

        code, response = TestUtils._delete(self.client, URLConstant.TrialBalanceView, TestConstants.INVALID_ID)
        self.assertEqual(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.RESOURCE_NOT_FOUND))
