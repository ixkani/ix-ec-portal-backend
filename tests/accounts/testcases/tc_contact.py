from rest_framework.test import APITestCase

from portalbackend.lendapi.accounts.models import Contact, Company
from portalbackend.validator.errormapping import ErrorMessage
from tests.constants import ResponseCodeConstant, TestConstants, CompanyConstant, ContactConstant, \
    ResponseMessageConstant, URLConstant
from tests.utils import TestUtils


class _001_ContactDetailsTestCase(APITestCase):
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
        """
        code, response = TestUtils._get_with_args(self.client, URLConstant.ContactDetails, self.company.id)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(response['result'][0]['first_name'])
        self.assertTrue(response['result'][0]['external_id'])
        self.assertTrue(response['result'][0]['email'])
        self.assertTrue(response['result'][0]['title'])
        self.assertTrue(response['result'][0]['last_name'])

    def test_002_get_invalid_company_id_failure(self):
        """
        Getting information with not existing company id
        """
        code, response = TestUtils._get_with_args(self.client, URLConstant.ContactDetails, TestConstants.INVALID_ID)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_003_create_contact_success(self):
        """
        Creating contact with all information ( test company for further testing)
        """
        self.data = {
            "title": "Espresso Employee",
            "last_name": "Employee",
            "email": "expressoemployee@exp.com",
            "first_name": "Expresso",
            "phone": "",
            "external_id": "EX0001"
        }

        code, response = TestUtils._post_with_args(self.client, URLConstant.ContactDetails, self.company.id, self.data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_key_success(response, 'first_name'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'external_id'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'email'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'last_name'))
        self.assertTrue(TestUtils._check_response_value(response, 'email', "expressoemployee@exp.com"))
        self.assertTrue(TestUtils._check_response_value(response, 'last_name', "Employee"))

    def test_004_create_contact_without_required_values_failure(self):
        """
        Creating contact without some required information
        """
        self.data = {
            "last_name": "Employee",
            "first_name": "Expresso",
            "phone": "",
            "external_id": "EX0001"
        }
        code, response = TestUtils._post_with_args(self.client, URLConstant.ContactDetails, self.company.id, self.data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(response["errors"]["email"])

    def test_005_create_contact_with_required_values_success(self):
        """
        Creating contact with only required information
        """
        self.data = {
            "title": "Espresso Employee",
            "email": "expressoemployee@exp.com",
            "external_id": "EX0001",
            "first_name": "Espresso",
            "last_name": "Employee"
        }
        code, response = TestUtils._post_with_args(self.client, URLConstant.ContactDetails, self.company.id, self.data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_key_success(response, 'first_name'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'external_id'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'email'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'title'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'last_name'))

    def test_006_create_contact_with_invalid_data_failure(self):
        """
        Creating contact with invalid data
        ( min/max length validation for first name , last name ,email,phone validation )
        """
        self.data = {
            "title": "Espresso Employee",
            "last_name": "Employee",
            "email": "expressoemplop.com",
            "first_name": "Expresso",
            "phone": "",
            "external_id": "EX0001"
        }
        code, response = TestUtils._post_with_args(self.client, URLConstant.ContactDetails, self.company.id, self.data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(response["errors"]["email"])

    def test_007_get_contact_with_exisitng_company_and_contact_success(self):
        """
        Getting information with existing company id and existing contact id
        """

        code, response = TestUtils._get_with_args(self.client, URLConstant.ContactDetails,
                                                  [self.company.id, self.contact.id])
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(response['result'][0]['first_name'])
        self.assertTrue(response['result'][0]['external_id'])
        self.assertTrue(response['result'][0]['email'])
        self.assertTrue(response['result'][0]['title'])
        self.assertTrue(response['result'][0]['last_name'])

    def test_008_get_contact_with_not_exisitng_company_and_contact_success(self):
        """
        Getting information with not existing company id and existing contact id
        """

        code, response = TestUtils._get_with_args(self.client, URLConstant.ContactDetails,
                                                  [TestConstants.INVALID_ID, self.contact.id])
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_009_get_contact_with_exisitng_company_and_not_exisitng_contact_success(self):
        """
        Getting information with existing company id and not existing contact id
        """

        code, response = TestUtils._get_with_args(self.client, URLConstant.ContactDetails,
                                                  [self.company.id, TestConstants.INVALID_ID])
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_010_get_contact_with_not_exisitng_company_and_not_exisitng_contact_success(self):
        """
        Getting information with not existing company id and not existing contact id
        """

        code, response = TestUtils._get_with_args(self.client, URLConstant.ContactDetails,
                                                  [TestConstants.INVALID_ID, TestConstants.INVALID_ID])
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)

    def test_011_update_contact_information_success(self):
        """
        Updating information with existing company id  and existing contact id with all information
        """
        data = {
            "title": "Espresso Employee",
            "first_name": "Espresso",
            "last_name": "Test",
            "email": "expressoemployee@espresso.com",
            "phone": "9876543210",
            "external_id": "EX0002"
        }
        code, response = TestUtils._put_with_args(self.client, URLConstant.ContactDetails,
                                                  [self.company.id, self.contact.id], data)
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_value(response, 'email', "expressoemployee@espresso.com"))
        self.assertTrue(TestUtils._check_response_value(response, 'last_name', "Test"))
        self.assertTrue(TestUtils._check_response_value(response, 'title', "Espresso Employee"))

    def test_012_update_contact_invalid_information_failure(self):
        """
        Updating information with existing company id and existing contact id with invalid information
        """
        data = {
            "title": "Espresso Employee",
            "first_name": "Espresso",
            "last_name": "Test",
            "email": "expressoemployee.com",
            "phone": "9876543210",
            "external_id": "EX0002"
        }
        code, response = TestUtils._put_with_args(self.client, URLConstant.ContactDetails,
                                                  [self.company.id, self.contact.id], data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(response["errors"]["email"])

    def test_013_update_contact_empty_information_failure(self):
        """
        Updating empty information with existing company id  and existing contact id
        """
        data = {
            "title": "",
            "first_name": "",
            "last_name": "",
            "email": "",
            "phone": "",
            "external_id": ""
        }
        code, response = TestUtils._put_with_args(self.client, URLConstant.ContactDetails,
                                                  [self.company.id, self.contact.id], data)
        self.assertEquals(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(response["errors"]["email"])
        self.assertTrue(response["errors"]["external_id"])

    def test_014_update_contact_empty_information_invalid_company_failure(self):
        """
        Updating empty information with not existing company id and existing contact id
        """
        data = {
            "title": "",
            "first_name": "",
            "last_name": "",
            "email": "",
            "phone": "",
            "external_id": ""
        }
        code, response = TestUtils._put_with_args(self.client, URLConstant.ContactDetails,
                                                  [TestConstants.INVALID_ID, self.contact.id], data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_015_update_contact_information_not_existing_contact_failure(self):
        """
        Updating information with existing company id  and not existing contact id with all information
        """
        data = {
            "title": "Espresso Employee",
            "first_name": "Espresso",
            "last_name": "Test",
            "email": "expressoemployee@espresso.com",
            "phone": "9876543210",
            "external_id": "EX0002"
        }
        code, response = TestUtils._put_with_args(self.client, URLConstant.ContactDetails,
                                                  [self.company.id, TestConstants.INVALID_ID], data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_016_update_contact_invalid_information_not_existing_contact_failure(self):
        """
        Updating information with existing company id and not existing contact id with invalid information
        """
        data = {
            "title": "Espresso Employee",
            "first_name": "Espresso",
            "last_name": "Test",
            "email": "expressoemployom",
            "phone": "9876543210",
            "external_id": "EX0002"
        }
        code, response = TestUtils._put_with_args(self.client, URLConstant.ContactDetails,
                                                  [self.company.id, TestConstants.INVALID_ID], data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_017_update_contact_information_not_existing_company_failure(self):
        """
        Updating information with not existing company id  and existing contact id with all information
        """
        data = {
            "title": "Espresso Employee",
            "first_name": "Espresso",
            "last_name": "Test",
            "email": "expressoemployee@espresso.com",
            "phone": "9876543210",
            "external_id": "EX0002"
        }
        code, response = TestUtils._put_with_args(self.client, URLConstant.ContactDetails,
                                                  [TestConstants.INVALID_ID, self.contact.id], data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_018_update_contact_invalid_information_not_existing_company_failure(self):
        """
        Updating information with not existing company id and existing contact id with invalid information
        """
        data = {
            "title": "Espresso Employee",
            "first_name": "Espresso",
            "last_name": "Test",
            "email": "expressoemployom",
            "phone": "9876543210",
            "external_id": "EX0002"
        }
        code, response = TestUtils._put_with_args(self.client, URLConstant.ContactDetails,
                                                  [TestConstants.INVALID_ID, self.contact.id], data)
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_019_delete_contact_success(self):
        """
        Delete with existing company id and exisitng contact id
        """
        code, response = TestUtils._delete(self.client, URLConstant.ContactDetails, [self.company.id, self.contact.id])
        self.assertEquals(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.DELETED_SUCCESSFULLY))

    def test_020_delete_contact_with_invalid_company_failure(self):
        """
        Delete with not existing company id and existing contact id
        """
        code, response = TestUtils._delete(self.client, URLConstant.ContactDetails,
                                           [TestConstants.INVALID_ID, self.contact.id])
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_021_delete_contact_with_invalid_contact_failure(self):
        """
        Delete with existing company id and not existing contact id
        """
        code, response = TestUtils._delete(self.client, URLConstant.ContactDetails,
                                           [self.company.id, TestConstants.INVALID_ID])
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))

    def test_022_delete_contactwith_invalid_company_invalid_contact_failure(self):
        """
        Delete with not existing company id and not existing contact id
        """
        code, response = TestUtils._delete(self.client, URLConstant.ContactDetails,
                                           [TestConstants.INVALID_ID, TestConstants.INVALID_ID])
        self.assertEquals(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ResponseMessageConstant.RESOURCE_NOT_FOUND))
