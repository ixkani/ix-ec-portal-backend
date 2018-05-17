from rest_framework.test import APITestCase

from portalbackend.lendapi.accounts.models import User
from portalbackend.validator.errormapping import ErrorMessage
from tests.constants import ResponseCodeConstant, TestConstants, CompanyConstant, ResponseMessageConstant, URLConstant
from tests.utils import TestUtils


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
        """
        self.data = {'username': 'ut_user001', 'password': 'Espresso@1', 'email': 'ut_user001@unittesting.com',
                     'first_name': 'Unit', 'last_name': 'Testing', 'company': 1}
        code, response = TestUtils._post(self.client, URLConstant.UserList, self.data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue('username' in response['result'])
        self.assertTrue(TestUtils._check_response_key_success(response, 'email'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'first_name'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'last_name'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'company'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'url'))
        self.assertTrue(TestUtils._check_response_value(response, 'username', 'ut_user001'))
        self.assertTrue(TestUtils._check_response_value(response, 'email', 'ut_user001@unittesting.com'))

    def test_002_create_user_existing_username_failure(self):
        """
        Creating user with already existing user name
        """
        self.data = {'username': 'ut_user001', 'password': 'Espresso@1', 'email': 'ut_user001@unittesting.com',
                     'first_name': 'Unit', 'last_name': 'Testing', 'company': 1}
        TestUtils._post(self.client, URLConstant.UserList, self.data)
        self.data = {'username': 'ut_user001', 'password': 'Espresso@1', 'email': 'ut_user001@unittesting.com',
                     'first_name': 'Unit', 'last_name': 'Testing', 'company': 1}
        code, response = TestUtils._post(self.client, URLConstant.UserList, self.data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(response['errors'])

    def test_003_create_user_failure(self):
        """
        Creating user with empty information
        """
        self.data = {}
        code, response = TestUtils._post(self.client, URLConstant.UserList, self.data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(response['errors'])

    def test_004_create_user_missing_password_failure(self):
        """
        Creating user without some required information.
        """
        self.data = {'username': 'ut_user002', 'email': 'ut_user002@unittesting.com',
                     'first_name': 'Unit', 'last_name': 'Testing002', 'company': 1}
        code, response = TestUtils._post(self.client, URLConstant.UserList, self.data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(response['errors'])
        self.assertTrue(TestUtils._check_response_key_error(response, 'password'))

    def test_005_create_user_invalid_data_failure(self):
        """
        Creating user with invalid data
        ( invalid email id,Maximum/Min Length for username, firstname, lastname)
        """
        self.data = {'username': 'ut_user002', 'email': 'ut_user002g.com',
                     'first_name': 'u', 'last_name': 'T', 'company': 1, 'password': 'Espresso@1'}
        code, response = TestUtils._post(self.client, URLConstant.UserList, self.data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(response['errors'])
        self.assertTrue(TestUtils._check_response_key_error(response, 'email'))

    def test_006_get_user_list_success(self):
        """
        Get and verify the all list of users.
        """
        code, response = TestUtils._get(self.client, URLConstant.UserList)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(response['result'][0]['username'])
        self.assertTrue(response['result'][0]['email'])

    def test_007_get_user_list_with_normal_login_failure(self):
        """
        Get user call verify by user unauthorized access.
        """
        TestUtils._create_user("ut_user001", 1)
        self.login = TestUtils._user_login(self.client, 'ut_user001')
        code, response = TestUtils._get(self.client, URLConstant.UserList)
        self.assertEquals(code, ResponseCodeConstant.UNAUTHORIZED_ACCESS_401)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.UNAUTHORIZED_ACCESS))

    def test_008_get_user_INTERNAL_SERVER_ERROR_500_failure(self):
        """
        Get user list which user has invalid company mapping
        """
        TestUtils._create_user("ut_user001", TestConstants.INVALID_ID)
        code, response = TestUtils._get(self.client, URLConstant.UserList)
        self.assertEquals(code, ResponseCodeConstant.INTERNAL_SERVER_ERROR_500)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.INTERNAL_SERVER_ERROR))

    def test_009_post_user_INTERNAL_SERVER_ERROR_500_failure(self):
        """
        Create user without company
        """
        self.data = {'username': 'ut_user001', 'password': 'Espresso@1', 'email': 'ut_user001@unittesting.com',
                     'first_name': 'Unit'}
        code, response = TestUtils._post(self.client, URLConstant.UserList, self.data)
        self.assertEquals(code, ResponseCodeConstant.INTERNAL_SERVER_ERROR_500)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.INTERNAL_SERVER_ERROR))


class _002_MeTestCase(APITestCase):

    def setUp(self):
        self.superuser = TestUtils._create_superuser()
        self.login = TestUtils._admin_login(self.client)
        TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        TestUtils._create_companymeta(1)

    def test_001_get_admin_user_success(self):
        """
        Getting self user information  (admin)
        """
        code, response = TestUtils._get(self.client, URLConstant.Me)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_value(response, 'username', self.superuser.username))

    def test_002_get_normal_user_success(self):
        """
        Getting self information  (non admin user)
        """
        self.client.logout()
        self.user = TestUtils._create_user("ut_user001", 1)
        self.login = TestUtils._user_login(self.client, "ut_user001")
        code, response = TestUtils._get(self.client, URLConstant.Me)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_value(response, 'username', self.user.username))

    def test_003_get_user_without_login_failure(self):
        """
        Getting self information (not existing)
        """
        self.client.logout()
        code, response = TestUtils._get(self.client, URLConstant.Me)
        self.assertEquals(code, ResponseCodeConstant.UNAUTHORIZED_ACCESS_401)
        TestUtils._check_response_detail(response, ResponseMessageConstant.AUTH_FAILED)

    def test_004_get_user_company_meta_not_available_failure(self):
        """
        Getting information with user id without company meta
        """
        TestUtils._create_company(2, CompanyConstant.COMPANY_NAME_001)
        self.client.logout()
        self.user = TestUtils._create_user("ut_user002", 2)
        self.login = TestUtils._user_login(self.client, "ut_user002")
        TestUtils._delete_company_meta(2)
        code, response = TestUtils._get(self.client, URLConstant.Me)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.COMPANY_META_NOT_AVAILABLE))

    def test_005_get_user_INTERNAL_SERVER_ERROR_500_failure(self):
        """
        Getting self information with invalid company mapping
        """
        self.client.logout()
        self.user = TestUtils._create_user("ut_user002", TestConstants.INVALID_ID)
        self.login = TestUtils._user_login(self.client, "ut_user002")
        code, response = TestUtils._get(self.client, URLConstant.Me)
        self.assertEquals(code, ResponseCodeConstant.INTERNAL_SERVER_ERROR_500)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.INTERNAL_SERVER_ERROR))


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
        """
        code, response = TestUtils._get_with_args(self.client, URLConstant.UserDetails, self.user.id)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_key_success(response, 'username'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'email'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'company'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'email'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'first_name'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'last_name'))

    def test_002_get_invalid_user_id_failure(self):
        """
        Getting information with not existing user id
        """
        code, response = TestUtils._get_with_args(self.client, URLConstant.UserDetails, TestConstants.INVALID_ID)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_003_get_user_normal_user_success(self):
        """
        Getting information with user login
        """
        self.client.logout()
        self.login = TestUtils._user_login(self.client, "ut_user001")
        code, response = TestUtils._get_with_args(self.client, URLConstant.UserDetails, self.user.id)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_key_success(response, 'username'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'email'))

    def test_004_get_user_without_login_failure(self):
        """
        Getting information without logged in
        """
        self.client.logout()
        code, response = TestUtils._get_with_args(self.client, URLConstant.UserDetails, self.user.id)
        self.assertEquals(code, ResponseCodeConstant.UNAUTHORIZED_ACCESS_401)
        TestUtils._check_response_detail(response, ResponseMessageConstant.AUTH_FAILED)

    def test_005_get_user_unauthorized_access_failure(self):
        """
        Getting information with unauthorized user login
        """
        self.client.logout()
        TestUtils._create_user("ut_user002", 2)
        self.login = TestUtils._user_login(self.client, "ut_user002")
        code, response = TestUtils._get_with_args(self.client, URLConstant.UserDetails, self.user.id)
        self.assertEquals(code, ResponseCodeConstant.UNAUTHORIZED_ACCESS_401)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.UNAUTHORIZED_ACCESS))

    def test_006_get_user_INTERNAL_SERVER_ERROR_500_failure(self):
        """
        Getting user information without company mapping
        """
        self.client.logout()
        self.user = TestUtils._create_user("ut_user002", TestConstants.INVALID_ID)
        self.login = TestUtils._user_login(self.client, "ut_user002")
        code, response = TestUtils._get_with_args(self.client, URLConstant.UserDetails, self.user.id)
        self.assertEquals(code, ResponseCodeConstant.INTERNAL_SERVER_ERROR_500)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.INTERNAL_SERVER_ERROR))

    def test_007_update_user_success(self):
        """
        Updating all information with existing user id
        """
        data = {'username': 'ut_user001', 'password': 'Espresso#1', 'email': 'ut_user001@unittesting.com',
                'first_name': 'Unit', 'last_name': 'Testing001'}

        code, response = TestUtils._put_with_args(self.client, URLConstant.UserDetails, self.user.id, data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_value(response, 'last_name', 'Testing001'))
        self.assertTrue(TestUtils._check_response_value(response, 'first_name', 'Unit'))
        self.assertTrue(TestUtils._check_response_value(response, 'email', 'ut_user001@unittesting.com'))

    def test_008_update_user_invalid_user_failure(self):
        """
        Updating all information with not existing user id
        """
        data = {'username': 'ut_user001', 'password': 'Espresso#1', 'email': 'ut_user001@unittesting.com',
                'first_name': 'Unit', 'last_name': 'Testing001'}

        code, response = TestUtils._put_with_args(self.client, URLConstant.UserDetails, TestConstants.INVALID_ID, data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_009_update_user_empty_value_failure(self):
        """
        Updating empty and invalid value for required field with existing user id
        """
        data = {'username': '', 'password': 'Espresso#1', 'email': 'ut_user001@unittesting.com',
                'first_name': 'Unit', 'last_name': 'Testing001'}

        code, response = TestUtils._put_with_args(self.client, URLConstant.UserDetails, self.user.id, data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_key_error(response, 'username'))

    def test_010_update_user_empty_value_invalid_user_failure(self):
        """
        Updating  empty and invalid value for required field with non existing user id
        """
        data = {'username': '', 'password': 'Espresso#1', 'email': 'ut_user001@unittesting.com',
                'first_name': 'Unit', 'last_name': 'Testing001'}

        code, response = TestUtils._put_with_args(self.client, URLConstant.UserDetails, TestConstants.INVALID_ID, data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_011_update_user_valid_info_success(self):
        """
        Updating valid information with existing user id
        """
        data = {'last_name': 'Testing'}

        code, response = TestUtils._put_with_args(self.client, URLConstant.UserDetails, self.user.id, data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_value(response, 'last_name', 'Testing'))

    def test_012_update_user_valid_info_invalid_user_failure(self):
        """
        Updating valid information with not existing user id
        """
        data = {'last_name': 'Testing'}

        code, response = TestUtils._put_with_args(self.client, URLConstant.UserDetails, TestConstants.INVALID_ID, data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_013_update_user_invalid_value_failure(self):
        """
        Updating information with admin login with existing user id and invalid information ( invalid email id,Maximum/Min Length for username, firstname, lastname)
        """
        data = {'email': 'ut_usting.com'}

        code, response = TestUtils._put_with_args(self.client, URLConstant.UserDetails, self.user.id, data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_key_error(response, 'email'))

    def test_014_update_user_unauthorized_access_failure(self):
        """
        Updating information with normal user login
        """
        data = {'email': 'ut_usting@espresso.com'}
        self.client.logout()
        TestUtils._create_user("ut_user002", 2)
        self.login = TestUtils._user_login(self.client, "ut_user002")
        code, response = TestUtils._put_with_args(self.client, URLConstant.UserDetails, self.user.id, data)
        self.assertEquals(code, ResponseCodeConstant.UNAUTHORIZED_ACCESS_401)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.UNAUTHORIZED_ACCESS))

    def test_015_update_user_INTERNAL_SERVER_ERROR_500_failure(self):
        """
        Update user with invalid company data
        """
        data = {'email': 'ut_usting@espresso.com'}
        self.client.logout()
        self.user = TestUtils._create_user("ut_user002", TestConstants.INVALID_ID)
        self.login = TestUtils._user_login(self.client, "ut_user002")
        code, response = TestUtils._put_with_args(self.client, URLConstant.UserDetails, self.user.id, data)
        self.assertEquals(code, ResponseCodeConstant.INTERNAL_SERVER_ERROR_500)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.INTERNAL_SERVER_ERROR))

    def test_016_delete_user_success(self):
        """
        Delete with existing user id
        """
        code, response = TestUtils._delete(self.client, URLConstant.UserDetails, self.user.id)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.DELETED_SUCCESSFULLY))

    def test_017_delete_user_invalid_user_failure(self):
        """
        Delete with not existing user id
        """
        code, response = TestUtils._delete(self.client, URLConstant.UserDetails, TestConstants.INVALID_ID)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_018_delete_unauthorized_access_failure(self):
        """
        Delete with existing user id unauthorized access
        """
        self.client.logout()
        self.user = TestUtils._create_user("ut_user002", 1)
        self.login = TestUtils._user_login(self.client, "ut_user002")
        code, response = TestUtils._delete(self.client, URLConstant.UserDetails, self.user.id)
        self.assertEquals(code, ResponseCodeConstant.UNAUTHORIZED_ACCESS_401)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.UNAUTHORIZED_ACCESS))
