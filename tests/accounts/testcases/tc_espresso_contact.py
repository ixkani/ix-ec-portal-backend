from rest_framework.test import APITestCase

from portalbackend.lendapi.accounts.models import ForgotPasswordRequest, Company, User, Contact
from portalbackend.validator.errormapping import ErrorMessage
from tests.constants import ResponseCodeConstant, UserConstant, TestConstants, CompanyConstant, ContactConstant, \
    ResponseMessageConstant, URLConstant
from tests.utils import TestUtils


class _001_EspressoContactsTestCase(APITestCase):
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
        """
        TestUtils._create_espresso_contact(self.company.id, self.contact.id)
        code, response = TestUtils._get_with_args(self.client, URLConstant.EspressoContacts, self.company.id)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(response['result'][0]['first_name'])
        self.assertTrue(response['result'][0]['external_id'])
        self.assertTrue(response['result'][0]['email'])
        self.assertTrue(response['result'][0]['title'])
        self.assertTrue(response['result'][0]['last_name'])

    def test_002_get_espresso_contact_list_no_data_available_success(self):  # new
        """
        Getting information for no available data
        """
        code, response = TestUtils._get_with_args(self.client, URLConstant.EspressoContacts, self.company.id)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.DATA_NOT_FOUND))

    def test_003_get_invalid_company_id_failure(self):
        """
        Getting information with not existing company id
        """
        code, response = TestUtils._get_with_args(self.client, URLConstant.EspressoContacts,
                                                  TestConstants.INVALID_ID)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_004_create_espresso_contact_success(self):
        """
        Create with valid contact list
        """
        data = {
            "contacts": [self.contact.id, TestConstants.INVALID_ID, self.contact.id]
        }
        code, response = TestUtils._post_with_args(self.client, URLConstant.EspressoContacts, self.company.id, data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertEquals(response['result'][0]['contact'], self.contact.id)

    def test_005_create_espresso_contact_invalid_data_failure(self):  # new
        """
        Create with invalid contact key
        """
        data = {
            "contact": [self.contact.id, TestConstants.INVALID_ID, self.contact.id]
        }
        code, response = TestUtils._post_with_args(self.client, URLConstant.EspressoContacts, self.company.id, data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.MISSING_PARAMETERS))

    def test_006_create_espresso_contact_invalid_contact_success(self):
        """
        Create with invalid contact list
        """
        data = {
            "contacts": [TestConstants.INVALID_ID]
        }
        code, response = TestUtils._post_with_args(self.client, URLConstant.EspressoContacts, self.company.id, data)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.DATA_NOT_FOUND))

    def test_007_get_espresso_contact_valid_contact_id_success(self):
        """
        Getting information with existing company id and existing contact id
        """
        TestUtils._create_espresso_contact(self.company.id, self.contact.id)
        code, response = TestUtils._get_with_args(self.client, URLConstant.EspressoContacts,
                                                  [self.company.id, self.contact.id])
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(response['result'][0]['first_name'])
        self.assertTrue(response['result'][0]['external_id'])
        self.assertTrue(response['result'][0]['email'])
        self.assertTrue(response['result'][0]['title'])
        self.assertTrue(response['result'][0]['last_name'])

    def test_008_get_espresso_contact_invalid_contact_id_failure(self):
        """
        Getting information with not existing company id and existing contact id
        """
        TestUtils._create_espresso_contact(self.company.id, self.contact.id)
        code, response = TestUtils._get_with_args(self.client, URLConstant.EspressoContacts,
                                                  [self.company.id, TestConstants.INVALID_ID])
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_009_get_espresso_contact_invalid_company_id_failure(self):
        """
        Getting information with existing company id and not existing contact id
        """
        TestUtils._create_espresso_contact(self.company.id, self.contact.id)
        code, response = TestUtils._get_with_args(self.client, URLConstant.EspressoContacts,
                                                  [TestConstants.INVALID_ID, self.contact.id])
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_010_get_espresso_contact_invalid_company_and_contact_id_failure(self):
        """
        Getting information with existing company id and not existing contact id
        """
        TestUtils._create_espresso_contact(self.company.id, self.contact.id)
        code, response = TestUtils._get_with_args(self.client, URLConstant.EspressoContacts,
                                                  [TestConstants.INVALID_ID, TestConstants.INVALID_ID])
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_011_delete_espresso_contact_success(self):
        """
        Delete with existing company id and exisitng contact id
        """
        TestUtils._create_espresso_contact(self.company.id, self.contact.id)
        code, response = TestUtils._delete(self.client, URLConstant.EspressoContacts,
                                           [self.company.id, self.contact.id])
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.DELETED_SUCCESSFULLY))

    def test_012_delete_espresso_contact_invalid_contact_failure(self):
        """
        Delete with not existing company id and existing contact id
        """
        code, response = TestUtils._delete(self.client, URLConstant.EspressoContacts,
                                           [self.company.id, TestConstants.INVALID_ID])
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_013_delete_espresso_contact_invalid_company_failure(self):
        """
        Delete with existing company id and not existing contact id
        """
        TestUtils._create_espresso_contact(self.company.id, self.contact.id)
        code, response = TestUtils._delete(self.client, URLConstant.EspressoContacts,
                                           [TestConstants.INVALID_ID, self.contact.id])
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_014_delete_espresso_contact_invalid_company_invalid_contact_failure(self):
        """
        Delete with not existing company id and not existing contact id
        """
        TestUtils._create_espresso_contact(self.company.id, self.contact.id)
        code, response = TestUtils._delete(self.client, URLConstant.EspressoContacts,
                                           [TestConstants.INVALID_ID, TestConstants.INVALID_ID])
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_015_delete_espresso_contact_unauthorized_access_failure(self):
        """
        Delete with existing company id and exisitng contact id
        """
        TestUtils._create_espresso_contact(self.company.id, self.contact.id)
        self.client.logout()
        code, response = TestUtils._delete(self.client, URLConstant.EspressoContacts,
                                           [self.company.id, self.contact.id])
        self.assertEquals(code, ResponseCodeConstant.UNAUTHORIZED_ACCESS_401)
        self.assertTrue(TestUtils._check_response_detail(response, ResponseMessageConstant.AUTH_FAILED))
