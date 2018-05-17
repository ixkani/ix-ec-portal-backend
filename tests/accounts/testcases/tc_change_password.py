from rest_framework.test import APITestCase

from portalbackend.lendapi.accounts.models import ForgotPasswordRequest, Company, User
from portalbackend.validator.errormapping import ErrorMessage
from tests.constants import ResponseCodeConstant, UserConstant, TestConstants, CompanyConstant, ContactConstant, \
    URLConstant, ResponseMessageConstant
from tests.utils import TestUtils


class _001_EmailValidationTestCase(APITestCase):
    """
     Tests the EmailValidation View
    """

    def setUp(self):
        self.superuser = TestUtils._create_superuser()
        self.login = TestUtils._admin_login(self.client)
        TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        TestUtils._create_companymeta(1)
        TestUtils._create_user("ut_user001", 1)
        self.user = User.objects.get(username="ut_user001")
        self.company = Company.objects.get(id=1)
        global token

    def test_001_create_forgot_password_request_success(self):
        """
        Requesting with Valid email Id
        """
        data = {
            "email": self.user.email
        }
        code, response = TestUtils._post(self.client, URLConstant.EmailValidation,
                                         data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.EMAIL_SEND))

    def test_002_create_forgot_password_request_invalid_email_failure(self):
        """
        Requesting with Invalid email ID
        """

        data = {
            "email": TestConstants.INVALID_EMAIL
        }
        code, response = TestUtils._post(self.client, URLConstant.EmailValidation,
                                         data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.VALIDATION_ERROR))

    def test_003_create_forgot_password_request_not_existing_email_failure(self):
        """
        Requesting with valid email ID but not exists
        """

        data = {
            "email": ContactConstant.DEFAULT_CONTACT_EMAIL
        }
        code, response = TestUtils._post(self.client, URLConstant.EmailValidation,
                                         data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.EMAIL_NOT_FOUND))

    def test_004_create_forgot_password_request_without_email_failure(self):
        """
        Requesting with empty email ID
        """

        data = {
        }
        code, response = TestUtils._post(self.client, URLConstant.EmailValidation,
                                         data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_005_create_forgot_password_request_multiple_user_failure(self):
        """
        Requesting with Valid email Id configured to Multiple users
        """
        data = {
            "email": self.user.email
        }
        TestUtils._create_user("ut_user002", 1)
        code, response = TestUtils._post(self.client, URLConstant.EmailValidation,
                                         data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.MULTIPLE_EMAIL_FOUND))


class _002_ForgotPasswordTestCase(APITestCase):
    """
     Tests the ForgotPassword View
    """

    def setUp(self):
        self.superuser = TestUtils._create_superuser()
        self.login = TestUtils._admin_login(self.client)
        TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        TestUtils._create_companymeta(1)
        TestUtils._create_user("ut_user001", 1)
        self.user = User.objects.get(username="ut_user001")
        self.company = Company.objects.get(id=1)

    def test_001_get_check_change_password_token_success(self):
        """
        Requesting with valid token
        """
        data = {
            "email": self.user.email
        }
        TestUtils._post(self.client, URLConstant.EmailValidation,
                        data)

        token = ForgotPasswordRequest.objects.get(user=self.user).token

        code, response = TestUtils._get_with_args(self.client, URLConstant.ForgotPassword,
                                                  token)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.TOKEN_VALID))

    def test_002_get_check_change_password_with_invalid_token_failure(self):
        """
        Requesting with invalid token
        """
        code, response = TestUtils._get_with_args(self.client, URLConstant.ForgotPassword,
                                                  TestConstants.INVALID_TOKEN)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.TOKEN_EXPIRED))

    def test_003_get_check_change_password_with_empty_failure(self):
        """
        Requesting with Empty token
        """
        code, response = TestUtils._get_with_args(self.client, URLConstant.ForgotPassword, '_')
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.TOKEN_EXPIRED))

    def test_004_post_change_password_valid_details_success(self):
        """
        Requesting with valid password and reenter password
        """
        data = {
            "email": self.user.email
        }
        TestUtils._post(self.client, URLConstant.EmailValidation,
                        data)

        token = ForgotPasswordRequest.objects.get(user=self.user).token

        data = {
            "password": UserConstant.USER_PASSWORD,
            "reenter_password": UserConstant.USER_PASSWORD
        }

        code, response = TestUtils._post_with_args(self.client, URLConstant.ForgotPassword,
                                                   token, data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.PASSWORD_RESET_SUCCESSFUL))

    def test_005_post_change_password_invalid_password_failure(self):
        """
        Requesting with invalid password and reenter password
        """
        data = {
            "email": self.user.email
        }
        TestUtils._post(self.client, URLConstant.EmailValidation,
                        data)

        token = ForgotPasswordRequest.objects.get(user=self.user).token

        data = {
            "password": TestConstants.INVALID_PASSWORD,
            "reenter_password": UserConstant.USER_PASSWORD
        }

        code, response = TestUtils._post_with_args(self.client, URLConstant.ForgotPassword,
                                                   token, data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.VALIDATION_ERROR))

    def test_006_post_change_password_invalid_reenter_password_failure(self):
        """
        Requesting with valid password and invalid reenter password
        """
        data = {
            "email": self.user.email
        }
        TestUtils._post(self.client, URLConstant.EmailValidation,
                        data)

        token = ForgotPasswordRequest.objects.get(user=self.user).token

        data = {
            "password": UserConstant.USER_PASSWORD,
            "reenter_password": TestConstants.INVALID_PASSWORD
        }

        code, response = TestUtils._post_with_args(self.client, URLConstant.ForgotPassword,
                                                   token, data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.VALIDATION_ERROR))

    def test_007_post_change_password_empty_details_failure(self):
        """
        Requesting with empty password and reenter password
        """
        data = {
            "email": self.user.email
        }
        TestUtils._post(self.client, URLConstant.EmailValidation,
                        data)

        token = ForgotPasswordRequest.objects.get(user=self.user).token

        data = {
            "password": '',
            "reenter_password": UserConstant.USER_PASSWORD
        }

        code, response = TestUtils._post_with_args(self.client, URLConstant.ForgotPassword,
                                                   token, data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.VALIDATION_ERROR))


class _003_ChangePasswordTestCase(APITestCase):
    """
    Tests the ChangePassword View
    """

    def setUp(self):
        self.superuser = TestUtils._create_superuser()
        TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        TestUtils._create_companymeta(1)
        self.key = ''

    def test_001_change_password_internal_server_error(self):
        """
        Change password without user id Internal server error
        """
        self.data = {
            "passcode": {
                "password": UserConstant.ADMIN_PASSWORD,
                "reenter_password": UserConstant.ADMIN_PASSWORD
            }
        }
        code, response = TestUtils._post(self.client, URLConstant.ChangePassword, self.data)
        self.assertEquals(code, ResponseCodeConstant.INTERNAL_SERVER_ERROR_500)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.INTERNAL_SERVER_ERROR))

    def test_002_change_password_success(self):
        """
        Change password with valid data
        """
        TestUtils._create_user("ut_user001", 1)
        self.login = TestUtils._user_login(self.client, "ut_user001")
        self.user = User.objects.get(username="ut_user001")
        self.data = {
            "id": self.user.id,
            "passcode": {
                "password": UserConstant.ADMIN_PASSWORD,
                "reenter_password": UserConstant.ADMIN_PASSWORD
            }
        }
        code, response = TestUtils._post(self.client, URLConstant.ChangePassword, self.data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.PASSWORD_RESET_SUCCESSFUL))

    def test_003_change_password_invalid_failure(self):
        """
        Change password with invalid data
        """
        self.data = {
            "passcode": {
                "password": UserConstant.ADMIN_PASSWORD,
                "reenter_password": TestConstants.INVALID_PASSWORD
            }
        }
        code, response = TestUtils._post(self.client, URLConstant.ChangePassword, self.data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.VALIDATION_ERROR))
