import json
from django.contrib.auth.models import User
# from django.urls import reverse
from rest_framework import status
# from django.test import TestCase, Client, RequestFactory
from .models import User, Company, CompanyMeta, Contact, ForgotPasswordRequest
from rest_framework.test import APIRequestFactory, force_authenticate, APITestCase

from portalbackend.lendapi.v1.accounts.views import UserList, UserDetail, LoginView
from tests.constants import TestConstants, UserConstant, CompanyConstant, ResponseCodeConstant, ContactConstant

from tests.utils import TestUtils
from portalbackend.validator.errormapping import ErrorMessage


class _001_UserListTestCase(APITestCase):
    """
    Tests the UserList View
    """

    def setUp(self):
        self.userid = ''
        self.superuser = TestUtils._create_superuser()
        TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        TestUtils._create_companymeta(1)
        self.login = TestUtils._admin_login(self.client)

    def test_001_create_user_success(self):
        """
        Creating user with all information (test user for further testing)
        :return:
        :rtype:
        """
        self.data = {'username': 'ut_user001', 'password': 'Espresso@1', 'email': 'ut_user001@unittesting.com',
                     'first_name': 'Unit', 'last_name': 'Testing', 'company': 1}
        code, response = TestUtils._post(self.client, 'user-list', self.data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_002_create_user_existing_username_failure(self):
        """
        Creating user with already exisitng user name
        :return:
        :rtype:
        """
        self.data = {'username': 'ut_user001', 'password': 'Espresso@1', 'email': 'ut_user001@unittesting.com',
                     'first_name': 'Unit', 'last_name': 'Testing', 'company': 1}
        TestUtils._post(self.client, 'user-list', self.data)
        self.data = {'username': 'ut_user001', 'password': 'Espresso@1', 'email': 'ut_user001@unittesting.com',
                     'first_name': 'Unit', 'last_name': 'Testing', 'company': 1}
        code, response = TestUtils._post(self.client, 'user-list', self.data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)

    def test_003_create_user_failure(self):
        """
        Creating user with empty information
        :return:
        :rtype:
        """
        self.data = {}
        code, response = TestUtils._post(self.client, 'user-list', self.data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)

    def test_004_create_user_missing_password_failure(self):
        """
        Creating user without some required information.
        :return:
        :rtype:
        """
        self.data = {'username': 'ut_user002', 'email': 'ut_user002@unittesting.com',
                     'first_name': 'Unit', 'last_name': 'Testing002', 'company': 1}
        code, response = TestUtils._post(self.client, 'user-list', self.data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)

    def test_005_create_user_invalid_data_failure(self):
        """
        Creating user with invalid data
        ( invalid email id,Maximum/Min Length for username, firstname, lastname)
        :return:
        :rtype:
        """
        self.data = {'username': 'ut_user002', 'email': 'ut_user002g.com',
                     'first_name': 'u', 'last_name': 'T', 'company': 1, 'password': 'Espresso@1'}
        code, response = TestUtils._post(self.client, 'user-list', self.data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)

    def test_006_get_user_list_success(self):
        """
        Get and verify the all list of users.
        :return:
        :rtype:
        """
        code, response = TestUtils._get(self.client, 'user-list')
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_007_get_user_list_with_normal_login_failure(self):
        """
        Get user call verify by user unauthorized access.
        :return:
        :rtype:
        """
        TestUtils._create_user("ut_user001", 1)
        self.login = TestUtils._user_login(self.client, 'ut_user001')
        code, response = TestUtils._get(self.client, 'user-list')
        self.assertEquals(code, ResponseCodeConstant.UNAUTHORIZED_ACCESS_401)

    def test_008_get_user_internal_server_error_failure(self):
        """
        Get user call verify by user unauthorized access.
        :return:
        :rtype:
        """
        TestUtils._create_user("ut_user001", TestConstants.INVALID_ID)
        code, response = TestUtils._get(self.client, 'user-list')
        self.assertEquals(code, ResponseCodeConstant.INTERNAL_SERVER_ERROR)

    def test_009_post_user_internal_server_error_failure(self):
        """
        Get user call verify by user unauthorized access.
        :return:
        :rtype:
        """
        self.data = {'username': 'ut_user001', 'password': 'Espresso@1', 'email': 'ut_user001@unittesting.com',
                     'first_name': 'Unit'}
        code, response = TestUtils._post(self.client, 'user-list', self.data)
        self.assertEquals(code, ResponseCodeConstant.INTERNAL_SERVER_ERROR)


class _002_MeTestCase(APITestCase):

    def setUp(self):
        self.superuser = TestUtils._create_superuser()
        self.login = TestUtils._admin_login(self.client)
        TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        TestUtils._create_companymeta(1)

    def test_001_get_admin_user_success(self):
        """
        Getting self user information  (admin)
        :return:
        :rtype:
        """
        code, response = TestUtils._get(self.client, 'me')
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_002_get_normal_user_success(self):
        """
        Getting self information  (non admin user)
        :return:
        :rtype:
        """
        self.client.logout()
        self.user = TestUtils._create_user("ut_user001", 1)
        self.login = TestUtils._user_login(self.client, "ut_user001")
        code, response = TestUtils._get(self.client, 'me')
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_003_get_user_without_login_failure(self):
        """
        Getting self information  (non admin user)
        :return:
        :rtype:
        """
        self.client.logout()
        code, response = TestUtils._get(self.client, 'me')
        self.assertEquals(code, ResponseCodeConstant.UNAUTHORIZED_ACCESS_401)

    def test_004_get_user_company_meta_not_available_failure(self):
        """
        Getting self information  (non admin user)
        :return:
        :rtype:
        """
        TestUtils._create_company(2, CompanyConstant.COMPANY_NAME_001)
        self.client.logout()
        self.user = TestUtils._create_user("ut_user002", 2)
        self.login = TestUtils._user_login(self.client, "ut_user002")
        TestUtils._delete_company_meta(2)
        code, response = TestUtils._get(self.client, 'me')
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)

    def test_005_get_user_internal_server_error_failure(self):
        """
        Getting self information  (non admin user)
        :return:
        :rtype:
        """
        self.client.logout()
        self.user = TestUtils._create_user("ut_user002", TestConstants.INVALID_ID)
        self.login = TestUtils._user_login(self.client, "ut_user002")
        code, response = TestUtils._get(self.client, 'me')
        self.assertEquals(code, ResponseCodeConstant.INTERNAL_SERVER_ERROR)


class _003_UserDetailsTestCase(APITestCase):
    """
     Tests the UserDetail View
    """

    def setUp(self):
        self.superuser = TestUtils._create_superuser()
        self.login = TestUtils._admin_login(self.client)
        TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        TestUtils._create_companymeta(1)
        TestUtils._create_user("ut_user001", 1)
        self.user = User.objects.get(username="ut_user001")

    def test_001_get_user_success(self):
        """
        Getting information with existing admin user id
        :return:
        :rtype:
        """
        code, response = TestUtils._get_with_args(self.client, 'user-detail', self.user.id)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_002_get_invalid_user_id_failure(self):
        """
        Getting information with not existing user id
        :return:
        :rtype:
        """
        code, response = TestUtils._get_with_args(self.client, 'user-detail', TestConstants.INVALID_ID)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_003_get_user_normal_user_success(self):
        """
        Getting information with user login
        :return:
        :rtype:
        """
        self.client.logout()
        self.login = TestUtils._user_login(self.client, "ut_user001")
        code, response = TestUtils._get_with_args(self.client, 'user-detail', self.user.id)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_004_get_user_without_login_failure(self):
        """
        Getting information without logged in
        :return:
        :rtype:
        """
        self.client.logout()
        code, response = TestUtils._get_with_args(self.client, 'user-detail', self.user.id)
        self.assertEquals(code, ResponseCodeConstant.UNAUTHORIZED_ACCESS_401)

    def test_005_get_user_unauthorized_access_failure(self):
        """
        Getting information with user login
        :return:
        :rtype:
        """
        self.client.logout()
        TestUtils._create_user("ut_user002", 2)
        self.login = TestUtils._user_login(self.client, "ut_user002")
        code, response = TestUtils._get_with_args(self.client, 'user-detail', self.user.id)
        self.assertEquals(code, ResponseCodeConstant.UNAUTHORIZED_ACCESS_401)

    def test_006_get_user_internal_server_error_failure(self):
        """
        Getting self information  (non admin user)
        :return:
        :rtype:
        """
        self.client.logout()
        self.user = TestUtils._create_user("ut_user002", TestConstants.INVALID_ID)
        self.login = TestUtils._user_login(self.client, "ut_user002")
        code, response = TestUtils._get_with_args(self.client, 'user-detail', self.user.id)
        self.assertEquals(code, ResponseCodeConstant.INTERNAL_SERVER_ERROR)

    def test_007_update_user_success(self):
        """
        Updating all information with existing user id
        :return:
        :rtype:
        """
        data = {'username': 'ut_user001', 'password': 'Espresso#1', 'email': 'ut_user001@unittesting.com',
                'first_name': 'Unit', 'last_name': 'Testing001'}

        code, response = TestUtils._put_with_args(self.client, 'user-detail', self.user.id, data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_008_update_user_invalid_user_failure(self):
        """
        Updating all information with existing user id
        :return:
        :rtype:
        """
        data = {'username': 'ut_user001', 'password': 'Espresso#1', 'email': 'ut_user001@unittesting.com',
                'first_name': 'Unit', 'last_name': 'Testing001'}

        code, response = TestUtils._put_with_args(self.client, 'user-detail', TestConstants.INVALID_ID, data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_009_update_user_empty_value_failure(self):
        """
        Updating all information with existing user id
        :return:
        :rtype:
        """
        data = {'username': '', 'password': 'Espresso#1', 'email': 'ut_user001@unittesting.com',
                'first_name': 'Unit', 'last_name': 'Testing001'}

        code, response = TestUtils._put_with_args(self.client, 'user-detail', self.user.id, data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)

    def test_010_update_user_empty_value_invalid_user_failure(self):
        """
        Updating all information with existing user id
        :return:
        :rtype:
        """
        data = {'username': '', 'password': 'Espresso#1', 'email': 'ut_user001@unittesting.com',
                'first_name': 'Unit', 'last_name': 'Testing001'}

        code, response = TestUtils._put_with_args(self.client, 'user-detail', TestConstants.INVALID_ID, data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_011_update_user_valid_info_success(self):
        """
        Updating valid information with existing user id
        :return:
        :rtype:
        """
        data = {'last_name': 'Testing'}

        code, response = TestUtils._put_with_args(self.client, 'user-detail', self.user.id, data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_012_update_user_valid_info_invalid_user_failure(self):
        """
        Updating valid information with not existing user id
        :return:
        :rtype:
        """
        data = {'last_name': 'Testing'}

        code, response = TestUtils._put_with_args(self.client, 'user-detail', TestConstants.INVALID_ID, data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_013_update_user_invalid_value_failure(self):
        """
        Updating all information with existing user id
        :return:
        :rtype:
        """
        data = {'email': 'ut_usting.com'}

        code, response = TestUtils._put_with_args(self.client, 'user-detail', self.user.id, data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)

    def test_014_update_user_unauthorized_access_failure(self):
        """
        Getting information with user login
        :return:
        :rtype:
        """
        data = {'email': 'ut_usting@espresso.com'}
        self.client.logout()
        TestUtils._create_user("ut_user002", 2)
        self.login = TestUtils._user_login(self.client, "ut_user002")
        code, response = TestUtils._put_with_args(self.client, 'user-detail', self.user.id, data)
        self.assertEquals(code, ResponseCodeConstant.UNAUTHORIZED_ACCESS_401)

    def test_015_update_user_internal_server_error_failure(self):
        """
        Getting self information  (non admin user)
        :return:
        :rtype:
        """
        data = {'email': 'ut_usting@espresso.com'}
        self.client.logout()
        self.user = TestUtils._create_user("ut_user002", TestConstants.INVALID_ID)
        self.login = TestUtils._user_login(self.client, "ut_user002")
        code, response = TestUtils._put_with_args(self.client, 'user-detail', self.user.id, data)
        self.assertEquals(code, ResponseCodeConstant.INTERNAL_SERVER_ERROR)

    def test_016_delete_user_success(self):
        """
        Delete with existing user id
        :return:
        :rtype:
        """
        code, response = TestUtils._delete(self.client, 'user-detail', self.user.id)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_017_delete_user_invalid_user_failure(self):
        """
        Delete with existing user id
        :return:
        :rtype:
        """
        code, response = TestUtils._delete(self.client, 'user-detail', TestConstants.INVALID_ID)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_018_delete_unauthorized_access_failure(self):
        """
        Delete with existing user id
        :return:
        :rtype:
        """
        self.client.logout()
        self.user = TestUtils._create_user("ut_user002", 1)
        self.login = TestUtils._user_login(self.client, "ut_user002")
        code, response = TestUtils._delete(self.client, 'user-detail', self.user.id)
        self.assertEquals(code, ResponseCodeConstant.UNAUTHORIZED_ACCESS_401)


class _004_LoginViewTestCase(APITestCase):
    """
       Tests the Login View
    """

    def setUp(self):
        self.superuser = TestUtils._create_superuser()
        TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        TestUtils._create_companymeta(1)
        TestUtils._create_user("ut_user001", 1)

    def test_001_post_valid_login_success(self):
        data = {'username': "ut_user001",
                'password': UserConstant.USER_PASSWORD
                }
        code, response = TestUtils._post(self.client, 'login', data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_002_post_valid_login_success(self):
        data = {'username': TestConstants.INVALID_USERNAME,
                'password': UserConstant.USER_PASSWORD
                }
        code, response = TestUtils._post(self.client, 'login', data)
        self.assertEquals(code, ResponseCodeConstant.UNAUTHORIZED_ACCESS_401)

    def test_003_post_invalid_login_password_success(self):
        data = {'username': "ut_user001",
                'password': TestConstants.INVALID_PASSWORD
                }
        code, response = TestUtils._post(self.client, 'login', data)
        self.assertEquals(code, ResponseCodeConstant.UNAUTHORIZED_ACCESS_401)

    def test_004_post_invalid_login_values_failure(self):
        data = {'username': TestConstants.INVALID_USERNAME,
                'password': TestConstants.INVALID_PASSWORD
                }
        code, response = TestUtils._post(self.client, 'login', data)
        self.assertEquals(code, ResponseCodeConstant.UNAUTHORIZED_ACCESS_401)

    def test_005_post_empty_login_values_failure(self):
        data = {'username': '',
                'password': ''
                }
        code, response = TestUtils._post(self.client, 'login', data)
        self.assertEquals(code, ResponseCodeConstant.UNAUTHORIZED_ACCESS_401)


class _005_ScheduledMaintenanceDetailsTestCase(APITestCase):
    def setUp(self):
        TestUtils._create_scheduled_maintenance()

    def test_001_schedule_mainatince_on_success(self):
        """
        Scheduled Maintaince is Turned ON
        :return:
        :rtype:
        """
        code, response = TestUtils._get(self.client, 'scheduled-maintenance')
        self.assertEqual(response["result"]["is_under_maintenance"], True)

    def test_002_schedule_mainatince_off_failure(self):
        """
        Scheduled Maintaince is Turned OFF
        :return:
        :rtype:
        """
        TestUtils._update_scheduled_maintenance()
        code, response = TestUtils._get(self.client, 'scheduled-maintenance')
        self.assertEqual(response["result"]["is_under_maintenance"], False)


class _006_TwoFactorAuthenticationDetailsTestCase(APITestCase):
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
        To turn on Two factor authentication On
        :return:
        :rtype:
        """
        code, response = TestUtils._get(self.client, 'twofactor-auth')
        self.key = response["result"]["secret_code"]
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)

    def test_002_post_twofactor_success(self):
        """
        check 2FA
        :return:
        :rtype:
        """
        data = {
            "code": TestUtils._get_Totp(self.key)
        }
        self.user.tfa_secret_code = self.key
        self.user.save()
        code, response = TestUtils._post(self.client, 'twofactor-auth', data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)

    def test_003_post_twofactor_invalidtotp_failure(self):
        """
        check 2FA
        :return:
        :rtype:
        """
        data = {
            "code": TestConstants.INVALID_TOTP
        }
        self.user.tfa_secret_code = self.key
        self.user.save()
        code, response = TestUtils._post(self.client, 'twofactor-auth', data)
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)

    def test_004_post_twofactor_emptytotp_failure(self):
        """
        check 2FA
        :return:
        :rtype:
        """
        data = {
            "code": 0
        }
        self.user.tfa_secret_code = self.key
        self.user.save()
        code, response = TestUtils._post(self.client, 'twofactor-auth', data)
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)

    def test_005_update_twofactor_flags_success(self):
        """
        updates 2FA
        :return:
        :rtype:
        """
        data = {
            "is_tfa_enabled": False,
            "is_tfa_setup_completed": False
        }
        code, response = TestUtils._put(self.client, 'twofactor-auth', data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)


class _007_CompanyListTestCase(APITestCase):
    """
    Tests the CompanyList View
    """

    def setUp(self):
        self.userid = ''
        self.superuser = TestUtils._create_superuser()
        self.login = TestUtils._admin_login(self.client)

    def test_001_create_company_success(self):
        """
        Creating company with all information ( test company for further testing)
        :return:
        :rtype:
        """
        self.data = {
            "id": 1,
            "name": "Test Company",
            "external_id": "ABC123",
            "website": "https://en.wikipedia.org/wiki/Unit_testing",
            "employee_count": 1,
            "default_currency": "CAD",
            "accounting_type": "Quickbooks"
        }
        code, response = TestUtils._post(self.client, 'company-list', self.data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_002_create_company_without_required_values_failure(self):
        """
        Creating company without some required information
        :return:
        :rtype:
        """
        self.data = {
            "name": "Test Company",
            "external_id": "ABC123",
            "employee_count": 1,
            "default_currency": "CAD"
        }
        code, response = TestUtils._post(self.client, 'company-list', self.data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)

    def test_003_create_company_with_empty_values_failure(self):
        """
        Creating company  with empty information
        :return:
        :rtype:
        """
        self.data = {
        }
        code, response = TestUtils._post(self.client, 'company-list', self.data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)

    def test_004_create_company_with_invalid_data_failure(self):
        """
        Creating company with invalid data
        ( invalid website,Maximum/Min Length for name,Currency,invalid account type )
        :return:
        :rtype:
        """
        self.data = {
            "name": "Test Company",
            "external_id": "ABC123",
            "website": "https://wikipedia",
            "employee_count": 1,
            "default_currency": "CADOLLAR"
        }
        code, response = TestUtils._post(self.client, 'company-list', self.data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)

    def test_005_get_company_list_success(self):
        """
        Get the all company list
        :return:
        :rtype:
        """
        code, response = TestUtils._get(self.client, 'company-list')
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)


class _008_CompanyDetailsTestCase(APITestCase):
    """
     Tests the CompanyDetails View
    """

    def setUp(self):
        self.superuser = TestUtils._create_superuser()
        self.login = TestUtils._admin_login(self.client)
        TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        TestUtils._create_companymeta(1)
        TestUtils._create_user("ut_user001", 1)
        self.company = Company.objects.get(id=1)

    def test_001_get_company_success(self):
        """
        Getting information with existing admin user id
        :return:
        :rtype:
        """
        code, response = TestUtils._get_with_args(self.client, 'company-detail', self.company.id)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_002_get_invalid_company_id_failure(self):
        """
        Getting information with not existing user id
        :return:
        :rtype:
        """
        code, response = TestUtils._get_with_args(self.client, 'company-detail', TestConstants.INVALID_ID)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_003_update_company_success(self):
        """
        Updating all information with existing user id
        :return:
        :rtype:
        """
        data = {
            "name": "Test Company1",
            "external_id": "ABC1234",
            "website": "https://en.wikipedia.org/wiki/Unit_testing/1/",
            "employee_count": 10,
            "default_currency": "INR",
            "accounting_type": "Quickbooks"
        }

        code, response = TestUtils._put_with_args(self.client, 'company-detail', self.company.id, data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_004_update_company_invalid_company_failure(self):
        """
        Updating all information with not existing user id
        :return:
        :rtype:
        """
        data = {
            "name": "Test Company1",
            "external_id": "ABC1234",
            "website": "https://en.wikipedia.org/wiki/Unit_testing/1/",
            "employee_count": 10,
            "default_currency": "INR",
            "accounting_type": "Quickbooks"
        }

        code, response = TestUtils._put_with_args(self.client, 'company-detail', TestConstants.INVALID_ID, data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_005_update_company_empty_value_failure(self):
        """
        Updating all information with existing user id with empty information
        :return:
        :rtype:
        """
        data = {
            "name": "",
            "external_id": "",
            "website": "",
            "employee_count": 10,
            "default_currency": "",
            "accounting_type": ""
        }

        code, response = TestUtils._put_with_args(self.client, 'company-detail', self.company.id, data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)

    def test_006_update_company_empty_value_invalid_company_failure(self):
        """
        Updating all information with existing user id
        :return:
        :rtype:
        """
        data = {
            "name": "",
            "external_id": "",
            "website": "",
            "employee_count": 10,
            "default_currency": "",
            "accounting_type": ""
        }

        code, response = TestUtils._put_with_args(self.client, 'company-detail', TestConstants.INVALID_ID, data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_007_update_company_valid_info_success(self):
        """
        Updating valid information with existing company id
        :return:
        :rtype:
        """
        data = {'name': 'Testing'}

        code, response = TestUtils._put_with_args(self.client, 'company-detail', self.company.id, data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_008_update_company_valid_info_invalid_company_failure(self):
        """
        Updating valid information with not existing company id
        :return:
        :rtype:
        """
        data = {'name': 'Testing'}

        code, response = TestUtils._put_with_args(self.client, 'company-detail', TestConstants.INVALID_ID, data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_009_delete_company_success(self):
        """
        Delete with existing company id
        :return:
        :rtype:
        """
        code, response = TestUtils._delete(self.client, 'company-detail', self.company.id)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_010_delete_company_invalid_user_failure(self):
        """
        Delete with existing company id
        :return:
        :rtype:
        """
        code, response = TestUtils._delete(self.client, 'company-detail', TestConstants.INVALID_ID)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)


class _009_CompanyMetaDetailsTestCase(APITestCase):
    """
     Tests the CompanyMetaDetails View
    """

    def setUp(self):
        self.superuser = TestUtils._create_superuser()
        self.login = TestUtils._admin_login(self.client)
        TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        TestUtils._create_companymeta(1)
        TestUtils._create_user("ut_user001", 1)
        self.company = Company.objects.get(id=1)

    def test_001_get_companymeta_success(self):
        """
        Getting information with existing admin user id
        :return:
        :rtype:
        """
        code, response = TestUtils._get_with_args(self.client, 'company-meta', self.company.id)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_002_get_invalid_companymeta_id_failure(self):
        """
        Getting information with not existing user id
        :return:
        :rtype:
        """
        code, response = TestUtils._get_with_args(self.client, 'company-meta', TestConstants.INVALID_ID)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_003_update_companymeta_success(self):
        """
        Updating all information with existing user id
        :return:
        :rtype:
        """
        data = {
            "monthly_reporting_sync_method": "Quickbooks Desktop",
            "monthly_reporting_current_period_status": "COMPLETE",
            "is_initial_setup": False,
            "trialbalance_dl_complete": True,
            "qb_desktop_installed": False,
        }

        code, response = TestUtils._put_with_args(self.client, 'company-meta', self.company.id, data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_004_update_companymeta_invalid_company_failure(self):
        """
        Updating all information with not existing company id
        :return:
        :rtype:
        """
        data = {
            "monthly_reporting_sync_method": "Quickbooks Desktop",
            "monthly_reporting_current_period_status": "COMPLETE",
            "is_initial_setup": False,
            "trialbalance_dl_complete": True,
            "qb_desktop_installed": False,
        }

        code, response = TestUtils._put_with_args(self.client, 'company-meta', TestConstants.INVALID_ID, data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_005_update_companymeta_invalid_value_failure(self):
        """
        Updating all information with existing company id with empty information
        :return:
        :rtype:
        """
        data = {
            "monthly_reporting_current_period": "2018-06-31"
        }

        code, response = TestUtils._put_with_args(self.client, 'company-meta', self.company.id, data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)

    def test_006_update_companymeta_empty_value_invalid_company_failure(self):
        """
        Updating all information with existing user id
        :return:
        :rtype:
        """
        data = {
            "monthly_reporting_sync_method": "",
            "monthly_reporting_current_period_status": "",
        }

        code, response = TestUtils._put_with_args(self.client, 'company-meta', TestConstants.INVALID_ID, data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_007_update_companymeta_valid_info_success(self):
        """
        Updating valid information with existing company id
        :return:
        :rtype:
        """
        data = {"is_initial_setup": True}

        code, response = TestUtils._put_with_args(self.client, 'company-meta', self.company.id, data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_008_update_companymeta_valid_info_invalid_company_failure(self):
        """
        Updating valid information with not existing company id
        :return:
        :rtype:
        """
        data = {"is_initial_setup": True}

        code, response = TestUtils._put_with_args(self.client, 'company-meta', TestConstants.INVALID_ID, data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)


class _010_ContactDetailsTestCase(APITestCase):
    """
     Tests the ContactDetails View
    """

    def setUp(self):
        self.superuser = TestUtils._create_superuser()
        self.login = TestUtils._admin_login(self.client)
        TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        TestUtils._create_companymeta(1)
        TestUtils._create_contact(1)
        TestUtils._create_user("ut_user001", 1)
        self.company = Company.objects.get(id=1)
        self.contact = Contact.objects.get(company__id=1, external_id=ContactConstant.DEFAULT_CONTACT_EXTERNALID)

    def test_001_get_contact_list_success(self):
        """
        Getting information with existing company id
        :return:
        :rtype:
        """
        code, response = TestUtils._get_with_args(self.client, 'company-contacts-list', self.company.id)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_002_get_invalid_company_id_failure(self):
        """
        Getting information with not existing company id
        :return:
        :rtype:
        """
        code, response = TestUtils._get_with_args(self.client, 'company-contacts-list', TestConstants.INVALID_ID)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_003_create_contact_success(self):
        """
        Creating contact with all information ( test company for further testing)
        :return:
        :rtype:
        """
        self.data = {
            "title": "Espresso Employee",
            "last_name": "Employee",
            "email": "expressoemployee@exp.com",
            "first_name": "Expresso",
            "phone": "",
            "external_id": "EX0001"
        }

        code, response = TestUtils._post_with_args(self.client, 'company-contacts-list', self.company.id, self.data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_004_create_contact_without_required_values_failure(self):
        """
        Creating contact without some required information
        :return:
        :rtype:
        """
        self.data = {
            "last_name": "Employee",
            "first_name": "Expresso",
            "phone": "",
            "external_id": "EX0001"
        }
        code, response = TestUtils._post_with_args(self.client, 'company-contacts-list', self.company.id, self.data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)

    def test_005_create_contact_with_required_values_success(self):
        """
        Creating contact with only required information
        :return:
        :rtype:
        """
        self.data = {
            "title": "Espresso Employee",
            "email": "expressoemployee@exp.com",
            "external_id": "EX0001",
            "first_name": "Espresso",
            "last_name": "Employee"
        }
        code, response = TestUtils._post_with_args(self.client, 'company-contacts-list', self.company.id, self.data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_006_create_contact_with_invalid_data_failure(self):
        """
        Creating contact with invalid data
        ( min/max length validation for first name , last name ,email,phone validation )
        :return:
        :rtype:
        """
        self.data = {
            "title": "Espresso Employee",
            "last_name": "Employee",
            "email": "expressoemplop.com",
            "first_name": "Expresso",
            "phone": "",
            "external_id": "EX0001"
        }
        code, response = TestUtils._post_with_args(self.client, 'company-contacts-list', self.company.id, self.data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)

    def test_007_get_contact_with_exisitng_company_and_contact_success(self):
        """
        Getting information with existing company id and existing contact id
        :return:
        :rtype:
        """

        code, response = TestUtils._get_with_args(self.client, 'company-contacts-list',
                                                  [self.company.id, self.contact.id])
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_008_get_contact_with_not_exisitng_company_and_contact_success(self):
        """
        Getting information with not existing company id and existing contact id
        :return:
        :rtype:
        """

        code, response = TestUtils._get_with_args(self.client, 'company-contacts-list',
                                                  [TestConstants.INVALID_ID, self.contact.id])
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_009_get_contact_with_exisitng_company_and_not_exisitng_contact_success(self):
        """
        Getting information with existing company id and not existing contact id
        :return:
        :rtype:
        """

        code, response = TestUtils._get_with_args(self.client, 'company-contacts-list',
                                                  [self.company.id, TestConstants.INVALID_ID])
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_010_get_contact_with_not_exisitng_company_and_not_exisitng_contact_success(self):
        """
        Getting information with not existing company id and not existing contact id
        :return:
        :rtype:
        """

        code, response = TestUtils._get_with_args(self.client, 'company-contacts-list',
                                                  [TestConstants.INVALID_ID, TestConstants.INVALID_ID])
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_011_update_contact_information_success(self):
        """
        Updating information with existing company id  and existing contact id with all information
        :return:
        :rtype:
        """
        data = {
            "title": "Espresso Employee",
            "first_name": "Espresso",
            "last_name": "Test",
            "email": "expressoemployee@espresso.com",
            "phone": "9876543210",
            "external_id": "EX0002"
        }
        code, response = TestUtils._put_with_args(self.client, 'company-contacts-list',
                                                  [self.company.id, self.contact.id], data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_012_update_contact_invalid_information_failure(self):
        """
        Updating information with existing company id and existing contact id with invalid information
        :return:
        :rtype:
        """
        data = {
            "title": "Espresso Employee",
            "first_name": "Espresso",
            "last_name": "Test",
            "email": "expressoemployee.com",
            "phone": "9876543210",
            "external_id": "EX0002"
        }
        code, response = TestUtils._put_with_args(self.client, 'company-contacts-list',
                                                  [self.company.id, self.contact.id], data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)

    def test_013_update_contact_empty_information_failure(self):
        """
        Updating empty information with existing company id  and existing contact id
        :return:
        :rtype:
        """
        data = {
            "title": "",
            "first_name": "",
            "last_name": "",
            "email": "",
            "phone": "",
            "external_id": ""
        }
        code, response = TestUtils._put_with_args(self.client, 'company-contacts-list',
                                                  [self.company.id, self.contact.id], data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)

    def test_014_update_contact_empty_information_invalid_company_failure(self):
        """
        Updating empty information with not existing company id and existing contact id
        :return:
        :rtype:
        """
        data = {
            "title": "",
            "first_name": "",
            "last_name": "",
            "email": "",
            "phone": "",
            "external_id": ""
        }
        code, response = TestUtils._put_with_args(self.client, 'company-contacts-list',
                                                  [TestConstants.INVALID_ID, self.contact.id], data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_015_update_contact_information_not_existing_contact_failure(self):
        """
        Updating information with existing company id  and not existing contact id with all information
        :return:
        :rtype:
        """
        data = {
            "title": "Espresso Employee",
            "first_name": "Espresso",
            "last_name": "Test",
            "email": "expressoemployee@espresso.com",
            "phone": "9876543210",
            "external_id": "EX0002"
        }
        code, response = TestUtils._put_with_args(self.client, 'company-contacts-list',
                                                  [self.company.id, TestConstants.INVALID_ID], data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_016_update_contact_invalid_information_not_existing_contact_failure(self):
        """
        Updating information with existing company id and not existing contact id with invalid information
        :return:
        :rtype:
        """
        data = {
            "title": "Espresso Employee",
            "first_name": "Espresso",
            "last_name": "Test",
            "email": "expressoemployom",
            "phone": "9876543210",
            "external_id": "EX0002"
        }
        code, response = TestUtils._put_with_args(self.client, 'company-contacts-list',
                                                  [self.company.id, TestConstants.INVALID_ID], data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_017_update_contact_information_not_existing_company_failure(self):
        """
        Updating information with not existing company id  and existing contact id with all information
        :return:
        :rtype:
        """
        data = {
            "title": "Espresso Employee",
            "first_name": "Espresso",
            "last_name": "Test",
            "email": "expressoemployee@espresso.com",
            "phone": "9876543210",
            "external_id": "EX0002"
        }
        code, response = TestUtils._put_with_args(self.client, 'company-contacts-list',
                                                  [TestConstants.INVALID_ID, self.contact.id], data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_018_update_contact_invalid_information_not_existing_company_failure(self):
        """
        Updating information with not existing company id and existing contact id with invalid information
        :return:
        :rtype:
        """
        data = {
            "title": "Espresso Employee",
            "first_name": "Espresso",
            "last_name": "Test",
            "email": "expressoemployom",
            "phone": "9876543210",
            "external_id": "EX0002"
        }
        code, response = TestUtils._put_with_args(self.client, 'company-contacts-list',
                                                  [TestConstants.INVALID_ID, self.contact.id], data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_019_delete_contact_success(self):
        """
        Delete with existing company id and exisitng contact id
        :return:
        :rtype:
        """
        code, response = TestUtils._delete(self.client, 'company-contacts-list', [self.company.id, self.contact.id])
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_020_delete_contact_with_invalid_company_failure(self):
        """
        Delete with not existing company id and existing contact id
        :return:
        :rtype:
        """
        code, response = TestUtils._delete(self.client, 'company-contacts-list',
                                           [TestConstants.INVALID_ID, self.contact.id])
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_021_delete_contact_with_invalid_contact_failure(self):
        """
        Delete with existing company id and not existing contact id
        :return:
        :rtype:
        """
        code, response = TestUtils._delete(self.client, 'company-contacts-list',
                                           [self.company.id, TestConstants.INVALID_ID])
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_022_delete_contactwith_invalid_company_invalid_contact_failure(self):
        """
        Delete with not existing company id and not existing contact id
        :return:
        :rtype:
        """
        code, response = TestUtils._delete(self.client, 'company-contacts-list',
                                           [TestConstants.INVALID_ID, TestConstants.INVALID_ID])
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)


class _011_EspressoContactsTestCase(APITestCase):
    """
     Tests the EspressoContacts View
    """

    def setUp(self):
        self.superuser = TestUtils._create_superuser()
        self.login = TestUtils._admin_login(self.client)
        TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        TestUtils._create_companymeta(1)
        TestUtils._create_contact(1)
        TestUtils._create_user("ut_user001", 1)
        self.company = Company.objects.get(id=1)
        self.contact = Contact.objects.get(company__id=1, external_id=ContactConstant.DEFAULT_CONTACT_EXTERNALID)

    def test_001_get_espresso_contact_list_success(self):
        """
        Getting information with existing company id
        :return:
        :rtype:
        """
        TestUtils._create_espresso_contact(self.company.id, self.contact.id)
        code, response = TestUtils._get_with_args(self.client, 'company-special-contacts-list', self.company.id)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_002_get_invalid_company_id_failure(self):
        """
        Getting information with not existing company id
        :return:
        :rtype:
        """
        code, response = TestUtils._get_with_args(self.client, 'company-special-contacts-list',
                                                  TestConstants.INVALID_ID)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_003_create_espresso_contact_success(self):
        """
        Create with valid contact list
        :return:
        :rtype:
        """
        data = {
            "contacts": [self.contact.id, TestConstants.INVALID_ID, self.contact.id]
        }
        code, response = TestUtils._post_with_args(self.client, 'company-special-contacts-list', self.company.id, data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_004_create_espresso_contact_invalid_contact_success(self):
        """
        Create with invalid contact list
        :return:
        :rtype:
        """
        data = {
            "contacts": [TestConstants.INVALID_ID]
        }
        code, response = TestUtils._post_with_args(self.client, 'company-special-contacts-list', self.company.id, data)
        self.assertEquals(response["message"], ErrorMessage.DATA_NOT_FOUND)

    def test_005_get_espresso_contact_valid_contact_id_success(self):
        """
        Getting information with existing company id and existing contact id
        :return:
        :rtype:
        """
        TestUtils._create_espresso_contact(self.company.id, self.contact.id)
        code, response = TestUtils._get_with_args(self.client, 'company-special-contacts-list',
                                                  [self.company.id, self.contact.id])
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_006_get_espresso_contact_invalid_contact_id_failure(self):
        """
        Getting information with not existing company id and existing contact id
        :return:
        :rtype:
        """
        TestUtils._create_espresso_contact(self.company.id, self.contact.id)
        code, response = TestUtils._get_with_args(self.client, 'company-special-contacts-list',
                                                  [self.company.id, TestConstants.INVALID_ID])
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_007_get_espresso_contact_invalid_company_id_failure(self):
        """
        Getting information with existing company id and not existing contact id
        :return:
        :rtype:
        """
        TestUtils._create_espresso_contact(self.company.id, self.contact.id)
        code, response = TestUtils._get_with_args(self.client, 'company-special-contacts-list',
                                                  [TestConstants.INVALID_ID, self.contact.id])
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_008_get_espresso_contact_invalid_company_and_contact_id_failure(self):
        """
        Getting information with existing company id and not existing contact id
        :return:
        :rtype:
        """
        TestUtils._create_espresso_contact(self.company.id, self.contact.id)
        code, response = TestUtils._get_with_args(self.client, 'company-special-contacts-list',
                                                  [TestConstants.INVALID_ID, TestConstants.INVALID_ID])
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_009_delete_espresso_contact_success(self):
        """
        Delete with existing company id and exisitng contact id
        :return:
        :rtype:
        """
        TestUtils._create_espresso_contact(self.company.id, self.contact.id)
        code, response = TestUtils._delete(self.client, 'company-special-contacts-list',
                                                  [self.company.id, self.contact.id])
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_010_delete_espresso_contact_invalid_contact_failure(self):
        """
        Delete with not existing company id and existing contact id
        :return:
        :rtype:
        """
        code, response = TestUtils._delete(self.client, 'company-special-contacts-list',
                                                  [self.company.id, TestConstants.INVALID_ID])
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_009_delete_espresso_contact_invalid_company_failure(self):
        """
        Delete with existing company id and not existing contact id
        :return:
        :rtype:
        """
        TestUtils._create_espresso_contact(self.company.id, self.contact.id)
        code, response = TestUtils._delete(self.client, 'company-special-contacts-list',
                                                  [TestConstants.INVALID_ID, self.contact.id])
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_009_delete_espresso_contact_invalid_company_invalid_contact_failure(self):
        """
        Delete with not existing company id and not existing contact id
        :return:
        :rtype:
        """
        TestUtils._create_espresso_contact(self.company.id, self.contact.id)
        code, response = TestUtils._delete(self.client, 'company-special-contacts-list',
                                                  [TestConstants.INVALID_ID, TestConstants.INVALID_ID])
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

class _012_EmailValidationTestCase(APITestCase):
    """
     Tests the EmailValidation View
    """
    def setUp(self):
        self.superuser = TestUtils._create_superuser()
        self.login = TestUtils._admin_login(self.client)
        TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        TestUtils._create_companymeta(1)
        TestUtils._create_user("ut_user001", 1)
        self.user = User.objects.get(username = "ut_user001")
        self.company = Company.objects.get(id=1)
        global token

    def test_001_create_forgot_password_request_success(self):
        """
        Requesting with Valid email Id
        :return:
        :rtype:
        """
        data = {
            "email" : self.user.email
        }
        code, response = TestUtils._post(self.client, 'validate-forgot-password',
                                           data)
        token = ForgotPasswordRequest.objects.get(user=self.user).token
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_002_create_forgot_password_request_invalid_email_failure(self):
        """
        Requesting with Invalid email ID
        :return:
        :rtype:
        """

        data = {
            "email" : TestConstants.INVALID_EMAIL
        }
        code, response = TestUtils._post(self.client, 'validate-forgot-password',
                                           data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)

    def test_003_create_forgot_password_request_not_existing_email_failure(self):
        """
        Requesting with valid email ID but not exists
        :return:
        :rtype:
        """

        data = {
            "email" : ContactConstant.DEFAULT_CONTACT_EMAIL
        }
        code, response = TestUtils._post(self.client, 'validate-forgot-password',
                                           data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)

    def test_004_create_forgot_password_request_without_email_failure(self):
        """
        Requesting with empty email ID
        :return:
        :rtype:
        """

        data = {
        }
        code, response = TestUtils._post(self.client, 'validate-forgot-password',
                                           data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

class _013_ForgotPasswordTestCase(APITestCase):
    """
     Tests the EmailValidation View
    """
    def setUp(self):
        self.superuser = TestUtils._create_superuser()
        self.login = TestUtils._admin_login(self.client)
        TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        TestUtils._create_companymeta(1)
        TestUtils._create_user("ut_user001", 1)
        self.user = User.objects.get(username = "ut_user001")
        self.company = Company.objects.get(id=1)

    def test_001_get_check_change_password_token_success(self):
        """
        Requesting with valid token
        :return:
        :rtype:
        """
        data = {
            "email" : self.user.email
        }
        TestUtils._post(self.client, 'validate-forgot-password',
                                           data)

        token = ForgotPasswordRequest.objects.get(user=self.user).token

        code, response = TestUtils._get_with_args(self.client, 'forgot-password',
                                            token)
        print(response)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_002_get_check_change_password_with_intoken_failure(self):
        """
        Requesting with invalid token
        :return:
        :rtype:
        """
        code, response = TestUtils._get_with_args(self.client, 'forgot-password',
                                            TestConstants.INVALID_TOKEN)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)

    def test_003_get_check_change_password_with_empty_failure(self):
        """
        Requesting with invalid token
        :return:
        :rtype:
        """
        code, response = TestUtils._get_with_args(self.client, 'forgot-password','_')
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)