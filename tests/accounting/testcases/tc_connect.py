from rest_framework.test import APITestCase

from portalbackend.lendapi.accounts.models import Company

from tests.constants import ResponseCodeConstant, CompanyConstant, TestConstants
from tests.utils import TestUtils


class _001_ConnectionTestCase(APITestCase):
    """
    Tests the Connection View
    """

    def setUp(self):
        self.userid = ''
        self.superuser = TestUtils._create_superuser()
        self.company = TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        TestUtils._create_companymeta(self.company.id)
        self.user = TestUtils._create_user('ut_user001', self.company.id)
        self.login = TestUtils._admin_login(self.client)

    def test_001_connect_company_success(self):
        """
        Creating connection for given company
        """
        TestUtils._create_accounting_configuration(Company.QUICKBOOKS)
        self.data = {
            "company": self.company.id
        }
        response = self.client.get('/lend/v1/connect/', self.data, format='json', secure=TestConstants.SECURE_CONNECTION,
                               HTTP_HOST=TestConstants.HOST_URL)
        code = response.status_code
        self.assertEqual(code, ResponseCodeConstant.REDIRECT_302)

    def test_002_connect_company_without_company_id(self):
        """
        Creating connection for not existing company
        """
        TestUtils._create_accounting_configuration(Company.QUICKBOOKS)
        self.data = {
        }
        response = self.client.get('/lend/v1/connect/', self.data, format='json', secure=TestConstants.SECURE_CONNECTION,
                               HTTP_HOST=TestConstants.HOST_URL)
        code = response.status_code
        self.assertEqual(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_003_connect_company_without_accounting_configuration(self):
        """
        Creating connection for given company without accounting configuration
        """
        self.data = {
        }
        response = self.client.get('/lend/v1/connect/', self.data, format='json', secure=TestConstants.SECURE_CONNECTION,
                               HTTP_HOST=TestConstants.HOST_URL)
        code = response.status_code

        self.assertEqual(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
