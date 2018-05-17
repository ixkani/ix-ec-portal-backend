import os
import json

from rest_framework.test import APITestCase

from portalbackend.validator.errormapping import ErrorMessage
from tests.constants import ResponseCodeConstant, CompanyConstant, URLConstant
from tests.utils import TestUtils


class _001_GenerateStatementTestCase(APITestCase):
    """
    Tests the GenerateStatement View
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

        with open(base_path + '/sample_data/tb_unbalanced_sample_data.json') as file:
            self.tb_unbalanced_data = json.load(file)

        TestUtils._create_default_mapping()
        TestUtils._create_finacial_tag_mapping()

    def test_001_get_generate_statement_success(self):
        """
        Generating statement with existing coa,coa-map,trial balance
        """
        TestUtils._create_fiscal_year(self.company)
        TestUtils._post_with_args(self.client, URLConstant.ChartOfAccounts, self.company.id, self.coa_data)
        TestUtils._get_with_args(self.client, URLConstant.CoaMapView, self.company.id)
        TestUtils._post_with_args(self.client, URLConstant.TrialBalanceView, self.company.id, self.tb_data)
        code, response = TestUtils._get_with_args(self.client, URLConstant.Statement, self.company.id)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_ledger_values(response))

    def test_002_get_generate_statement_unbalanced_tb_failure(self):
        """
        Generating statement with unbalanced trial balance
        """
        TestUtils._create_fiscal_year(self.company)
        TestUtils._post_with_args(self.client, URLConstant.ChartOfAccounts, self.company.id, self.coa_data)
        TestUtils._get_with_args(self.client, URLConstant.CoaMapView, self.company.id)
        TestUtils._post_with_args(self.client, URLConstant.TrialBalanceView, self.company.id, self.tb_unbalanced_data)
        code, response = TestUtils._get_with_args(self.client, URLConstant.Statement, self.company.id)
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.CREDIT_DEBIT_UNEQUALS))

    def test_003_get_generate_statement_assets_equal_equity_liability_success(self):
        """
        Generating statement with coa,coa-map,trial balance to check assets and l&e equal
        """
        TestUtils._create_fiscal_year(self.company)
        TestUtils._post_with_args(self.client, URLConstant.ChartOfAccounts, self.company.id, self.coa_data)
        TestUtils._get_with_args(self.client, URLConstant.CoaMapView, self.company.id)
        TestUtils._post_with_args(self.client, URLConstant.TrialBalanceView, self.company.id, self.tb_data)
        code, response = TestUtils._get_with_args(self.client, URLConstant.Statement, self.company.id)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_credit_debit_values(response))

    def test_004_get_generate_statement_map_without_fiscal_year_failure(self):
        """
        Generating statement without fiscal year configuration
        """
        TestUtils._post_with_args(self.client, URLConstant.ChartOfAccounts, self.company.id, self.coa_data)
        TestUtils._get_with_args(self.client, URLConstant.CoaMapView, self.company.id)
        TestUtils._post_with_args(self.client, URLConstant.TrialBalanceView, self.company.id, self.tb_data)
        code, response = TestUtils._get_with_args(self.client, URLConstant.Statement, self.company.id)
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.FISCAL_YEAR_MISSING))

    def test_005_get_generate_statement_map_without_data_success(self):
        """
        Generating statement without coa,coa-map,trial balance
        """
        TestUtils._create_fiscal_year(self.company)
        code, response = TestUtils._get_with_args(self.client, URLConstant.Statement, self.company.id)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertEqual(len(response['result']['Model']['Financials']['BalanceSheet']), 0)
        self.assertEqual(len(response['result']['Model']['Financials']['IncomeStatement']), 0)
