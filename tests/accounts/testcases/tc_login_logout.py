from rest_framework.test import APITestCase

from portalbackend.validator.errormapping import ErrorMessage
from tests.constants import ResponseCodeConstant, CompanyConstant, TestConstants, UserConstant, URLConstant
from tests.utils import TestUtils


class _001_LoginViewTestCase(APITestCase):
    """
       Tests the Login View
    """

    def setUp(self):
        self.superuser = TestUtils._create_superuser()
        TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        TestUtils._create_companymeta(1)
        TestUtils._create_user("ut_user001", 1)

    def test_001_post_valid_login_success(self):
        """
        Login with valid user name and Password
        """
        data = {'username': "ut_user001",
                'password': UserConstant.USER_PASSWORD
                }
        code, response = TestUtils._post(self.client, URLConstant.LoginView, data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_key_success(response, 'username'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'email'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'company'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'email'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'first_name'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'last_name'))

    def test_002_post_invalid_login_username_failure(self):
        """
        Login with invalid user name and valid Password
        """
        data = {'username': TestConstants.INVALID_USERNAME,
                'password': UserConstant.USER_PASSWORD
                }
        code, response = TestUtils._post(self.client, URLConstant.LoginView, data)
        self.assertEquals(code, ResponseCodeConstant.UNAUTHORIZED_ACCESS_401)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.UNAUTHORIZED_ACCESS))

    def test_003_post_invalid_login_password_success(self):
        """
        Login with valid user name and invalid Password
        """
        data = {'username': "ut_user001",
                'password': TestConstants.INVALID_PASSWORD
                }
        code, response = TestUtils._post(self.client, URLConstant.LoginView, data)
        self.assertEquals(code, ResponseCodeConstant.UNAUTHORIZED_ACCESS_401)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.UNAUTHORIZED_ACCESS))

    def test_004_post_invalid_login_values_failure(self):
        """
        Login with invalid user name and Password
        """
        data = {'username': TestConstants.INVALID_USERNAME,
                'password': TestConstants.INVALID_PASSWORD
                }
        code, response = TestUtils._post(self.client, URLConstant.LoginView, data)
        self.assertEquals(code, ResponseCodeConstant.UNAUTHORIZED_ACCESS_401)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.UNAUTHORIZED_ACCESS))

    def test_005_post_empty_login_values_failure(self):
        """
        Login with empty user name and Password
        """
        data = {'username': '',
                'password': ''
                }
        code, response = TestUtils._post(self.client, URLConstant.LoginView, data)
        self.assertEquals(code, ResponseCodeConstant.UNAUTHORIZED_ACCESS_401)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.UNAUTHORIZED_ACCESS))


class _002_LogoutTestCase(APITestCase):
    """
       Tests the Login View
    """

    def setUp(self):
        self.superuser = TestUtils._create_superuser()
        TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        TestUtils._create_companymeta(1)
        TestUtils._create_user("ut_user001", 1)

    def test_001_get_logout_success(self):
        """
        Logout currently Logged in user
        """
        self.login = TestUtils._user_login(self.client, 'ut_user001')
        code, response = TestUtils._get(self.client, URLConstant.LogoutView)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
