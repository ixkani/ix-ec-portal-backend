from rest_framework.test import APITestCase

from portalbackend.lendapi.accounts.models import Company
from portalbackend.lendapi.accounts.utils import AccountsUtils
from portalbackend.validator.errormapping import ErrorMessage
from tests.constants import ResponseCodeConstant, TestConstants, CompanyConstant, ResponseMessageConstant, URLConstant
from tests.utils import TestUtils


class _001_CompanyListTestCase(APITestCase):
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
        code, response = TestUtils._post(self.client, URLConstant.CompanyList, self.data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_key_success(response, 'name'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'external_id'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'website'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'employee_count'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'default_currency'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'accounting_type'))
        self.assertTrue(TestUtils._check_response_value(response, 'name', 'Test Company'))
        self.assertTrue(
            TestUtils._check_response_value(response, 'website', 'https://en.wikipedia.org/wiki/Unit_testing'))

    def test_002_create_company_without_required_values_failure(self):
        """
        Creating company without some required information
        """
        self.data = {
            "name": "Test Company",
            "external_id": "ABC123",
            "employee_count": 1,
            "default_currency": "CAD"
        }
        code, response = TestUtils._post(self.client, URLConstant.CompanyList, self.data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_key_error(response, 'website'))

    def test_003_create_company_with_empty_values_failure(self):
        """
        Creating company  with empty information
        """
        self.data = {
        }
        code, response = TestUtils._post(self.client, URLConstant.CompanyList, self.data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_key_error(response, 'website'))

    def test_004_create_company_with_invalid_data_failure(self):
        """
        Creating company with invalid data
        ( invalid website,Maximum/Min Length for name,Currency,invalid account type )
        """
        self.data = {
            "name": "Test Company",
            "external_id": "ABC123",
            "website": "https://wikipedia",
            "employee_count": 1,
            "default_currency": "CADOLLAR"
        }
        code, response = TestUtils._post(self.client, URLConstant.CompanyList, self.data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_key_error(response, 'website'))
        self.assertTrue(TestUtils._check_response_key_error(response, 'default_currency'))

    def test_005_get_company_list_success(self):
        """
        Get the all company list
        """
        code, response = TestUtils._get(self.client, URLConstant.CompanyList)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)

    def test_006_get_company_from_utils_success(self):
        """
        Get the all company list from accounting Utils
        """
        company = TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        self.assertEquals(company, AccountsUtils.get_company(company.id))

    def test_007_get_company_from_utils_failure(self):
        """
        Get the all company list without having company
        """
        with self.assertRaises(Exception) as e:
            self.assertEquals(e, AccountsUtils.get_company(TestConstants.INVALID_ID))


class _002_CompanyDetailsTestCase(APITestCase):
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
        """
        code, response = TestUtils._get_with_args(self.client, URLConstant.CompanyDetails, self.company.id)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_key_success(response, 'name'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'external_id'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'website'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'employee_count'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'accounting_type'))
        self.assertTrue(TestUtils._check_response_value(response, 'name', CompanyConstant.COMPANY_NAME_001))
        self.assertTrue(TestUtils._check_response_value(response, 'website', CompanyConstant.DEFAULT_COMPANY_WEBSITE))

    def test_002_get_invalid_company_id_failure(self):
        """
        Getting information with not existing user id
        """
        code, response = TestUtils._get_with_args(self.client, URLConstant.CompanyDetails, TestConstants.INVALID_ID)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_003_update_company_success(self):
        """
        Updating all information with existing user id
        """
        data = {
            "name": "Test Company1",
            "external_id": "ABC1234",
            "website": "https://en.wikipedia.org/wiki/Unit_testing/1/",
            "employee_count": 10,
            "default_currency": "INR",
            "accounting_type": "Quickbooks"
        }

        code, response = TestUtils._put_with_args(self.client, URLConstant.CompanyDetails, self.company.id, data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_value(response, 'employee_count', 10))

    def test_004_update_company_invalid_company_failure(self):
        """
        Updating all information with not existing user id
        """
        data = {
            "name": "Test Company1",
            "external_id": "ABC1234",
            "website": "https://en.wikipedia.org/wiki/Unit_testing/1/",
            "employee_count": 10,
            "default_currency": "INR",
            "accounting_type": "Quickbooks"
        }

        code, response = TestUtils._put_with_args(self.client, URLConstant.CompanyDetails, TestConstants.INVALID_ID,
                                                  data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_005_update_company_empty_value_failure(self):
        """
        Updating all information with existing user id with empty information
        """
        data = {
            "name": "",
            "external_id": "",
            "website": "",
            "employee_count": 10,
            "default_currency": "",
            "accounting_type": ""
        }

        code, response = TestUtils._put_with_args(self.client, URLConstant.CompanyDetails, self.company.id, data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_key_error(response, 'accounting_type'))
        self.assertTrue(TestUtils._check_response_key_error(response, 'website'))
        self.assertTrue(TestUtils._check_response_key_error(response, 'external_id'))

    def test_006_update_company_empty_value_invalid_company_failure(self):
        """
        Updating empty and invalid value for required field with non existing company id
        """
        data = {
            "name": "",
            "external_id": "",
            "website": "",
            "employee_count": 10,
            "default_currency": "",
            "accounting_type": ""
        }

        code, response = TestUtils._put_with_args(self.client, URLConstant.CompanyDetails, TestConstants.INVALID_ID,
                                                  data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_007_update_company_valid_info_success(self):
        """
        Updating valid information with existing company id
        """
        data = {'name': 'Testing'}

        code, response = TestUtils._put_with_args(self.client, URLConstant.CompanyDetails, self.company.id, data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_value(response, 'name', 'Testing'))

    def test_008_update_company_valid_info_invalid_company_failure(self):
        """
        Updating empty and valid value for required field with non existing company id
        """
        data = {'name': 'Testing'}

        code, response = TestUtils._put_with_args(self.client, URLConstant.CompanyDetails, TestConstants.INVALID_ID,
                                                  data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_009_delete_company_success(self):
        """
        Delete with existing company id
        """
        code, response = TestUtils._delete(self.client, URLConstant.CompanyDetails, self.company.id)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.DELETED_SUCCESSFULLY))

    def test_010_delete_company_invalid_user_failure(self):
        """
        Delete with not existing company id
        """
        code, response = TestUtils._delete(self.client, URLConstant.CompanyDetails, TestConstants.INVALID_ID)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))


class _003_CompanyMetaDetailsTestCase(APITestCase):
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
        Getting information with existing company id
        """
        code, response = TestUtils._get_with_args(self.client, URLConstant.CompanyMetaDetails, self.company.id)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_value(response, 'monthly_reporting_sync_method', None))
        self.assertTrue(TestUtils._check_response_value(response, 'monthly_reporting_current_period_status', None))
        self.assertTrue(TestUtils._check_response_value(response, 'is_initial_setup', True))
        self.assertTrue(TestUtils._check_response_value(response, 'trialbalance_dl_complete', False))
        self.assertTrue(TestUtils._check_response_value(response, 'qb_desktop_installed', False))

    def test_002_get_invalid_companymeta_id_failure(self):
        """
        Getting information with not existing company id
        """
        code, response = TestUtils._get_with_args(self.client, URLConstant.CompanyMetaDetails, TestConstants.INVALID_ID)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_003_update_companymeta_success(self):
        """
        Updating all information with existing company id
        """
        data = {
            "monthly_reporting_sync_method": "Quickbooks Desktop",
            "monthly_reporting_current_period_status": "COMPLETE",
            "is_initial_setup": False,
            "trialbalance_dl_complete": True,
            "qb_desktop_installed": False,
        }

        code, response = TestUtils._put_with_args(self.client, URLConstant.CompanyMetaDetails, self.company.id, data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_value(response, 'qb_desktop_installed', False))
        self.assertTrue(TestUtils._check_response_value(response, 'trialbalance_dl_complete', True))
        self.assertTrue(TestUtils._check_response_value(response, 'is_initial_setup', False))

    def test_004_update_companymeta_invalid_company_failure(self):
        """
        Updating all information with not existing company id
        """
        data = {
            "monthly_reporting_sync_method": "Quickbooks Desktop",
            "monthly_reporting_current_period_status": "COMPLETE",
            "is_initial_setup": False,
            "trialbalance_dl_complete": True,
            "qb_desktop_installed": False,
        }

        code, response = TestUtils._put_with_args(self.client, URLConstant.CompanyMetaDetails, TestConstants.INVALID_ID,
                                                  data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_005_update_companymeta_invalid_value_failure(self):
        """
        Updating all information with existing company id with empty information
        """
        data = {
            "monthly_reporting_current_period": "2018-06-31"
        }

        code, response = TestUtils._put_with_args(self.client, URLConstant.CompanyMetaDetails, self.company.id, data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_key_error(response, 'monthly_reporting_current_period'))

    def test_006_update_companymeta_empty_value_invalid_company_failure(self):
        """
        Updating all information with existing company id
        """
        data = {
            "monthly_reporting_sync_method": "",
            "monthly_reporting_current_period_status": "",
        }

        code, response = TestUtils._put_with_args(self.client, URLConstant.CompanyMetaDetails, TestConstants.INVALID_ID,
                                                  data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_007_update_companymeta_valid_info_success(self):
        """
        Updating valid information with existing company id
        """
        data = {"is_initial_setup": True}

        code, response = TestUtils._put_with_args(self.client, URLConstant.CompanyMetaDetails, self.company.id, data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_value(response, 'is_initial_setup', True))

    def test_008_update_companymeta_valid_info_invalid_company_failure(self):
        """
        Updating valid information with not existing company id
        """
        data = {"is_initial_setup": True}

        code, response = TestUtils._put_with_args(self.client, URLConstant.CompanyMetaDetails, TestConstants.INVALID_ID,
                                                  data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))
