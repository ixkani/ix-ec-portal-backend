from rest_framework.test import APITestCase

from portalbackend.lendapi.accounts.models import User
from portalbackend.validator.errormapping import ErrorMessage
from tests.constants import ResponseCodeConstant, TestConstants, CompanyConstant, URLConstant
from tests.utils import TestUtils


class _001_TwoFactorAuthenticationDetailsTestCase(APITestCase):
    """
     Tests the 2FA View
    """

    def setUp(self):
        self.superuser = TestUtils._create_superuser()
        TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        TestUtils._create_companymeta(1)
        TestUtils._create_user("ut_user001", 1)
        self.user = User.objects.get(username="ut_user001")
        self.key = ''
        self.login = TestUtils._user_login(self.client, "ut_user001")

    def test_001_get_twofactor_success(self):
        """
        Requesting two factor auth key
        """
        code, response = TestUtils._get(self.client, URLConstant.TwoFactorAuthenticationDetails)
        self.key = response["result"]["secret_code"]

        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_key_success(response, 'secret_code'))

    def test_002_post_twofactor_success(self):
        """
        Checking with valid TOTP
        """
        self.user.tfa_secret_code = self.key
        self.user.save()
        data = {
            "code": TestUtils._get_Totp(self.key)
        }
        code, response = TestUtils._post(self.client, URLConstant.TwoFactorAuthenticationDetails, data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)

    def test_003_post_twofactor_invalidtotp_failure(self):
        """
        Checking with invalid TOTP
        """
        data = {
            "code": TestConstants.INVALID_TOTP
        }
        self.user.tfa_secret_code = self.key
        self.user.save()
        code, response = TestUtils._post(self.client, URLConstant.TwoFactorAuthenticationDetails, data)
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.VALIDATION_ERROR))

    def test_004_post_twofactor_empty_totp_failure(self):
        """
        Checking eith empty TOTP
        """
        data = {
            "code": 0
        }
        self.user.tfa_secret_code = self.key
        self.user.save()
        code, response = TestUtils._post(self.client, URLConstant.TwoFactorAuthenticationDetails, data)
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.VALIDATION_ERROR))

    def test_005_post_twofactor_INTERNAL_SERVER_ERROR_500_failure(self):  # new
        """
        2FA empty code internal server error
        """
        data = {
            "code": ''
        }
        self.user.tfa_secret_code = self.key
        self.user.save()
        code, response = TestUtils._post(self.client, URLConstant.TwoFactorAuthenticationDetails, data)
        self.assertEqual(code, ResponseCodeConstant.INTERNAL_SERVER_ERROR_500)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.INTERNAL_SERVER_ERROR))

    def test_006_update_twofactor_flags_success(self):
        """
        Update the tfa enabled and setup completed flag
        """
        data = {
            "is_tfa_enabled": False,
            "is_tfa_setup_completed": False
        }
        code, response = TestUtils._put(self.client, URLConstant.TwoFactorAuthenticationDetails, data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)

    def test_007_update_twofactor_flags_internal_server_error_failure(self):  # new
        """
        Update the tfa enabled and setup completed flag with invalid data
        """
        data = {
            "is_tfa_enabled": "YES",
            "is_tfa_setup_completed": "YES"
        }
        code, response = TestUtils._put(self.client, URLConstant.TwoFactorAuthenticationDetails, data)
        self.assertEqual(code, ResponseCodeConstant.INTERNAL_SERVER_ERROR_500)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.INTERNAL_SERVER_ERROR))
