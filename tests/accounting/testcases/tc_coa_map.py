import os
import json

from rest_framework.test import APITestCase

from portalbackend.lendapi.accounting.models import CoAMap
from portalbackend.validator.errormapping import ErrorMessage

from tests.utils import TestUtils
from tests.constants import ResponseCodeConstant, TestConstants, CompanyConstant, ResponseMessageConstant, URLConstant


class _001_CoAMapTestCase(APITestCase):
    """
    Tests the CoAMap View
    """

    def setUp(self):
        self.superuser = TestUtils._create_superuser()
        self.company = TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        TestUtils._create_companymeta(self.company.id)

        self.user = TestUtils._create_user('ut_user001', self.company.id)

        self.login = TestUtils._admin_login(self.client)

        base_path = os.path.dirname(os.path.realpath(__file__))
        with open(base_path + '/sample_data/cao_map_sample_data.json') as file:
            self.coamap_data = json.load(file)

        with open(base_path + '/sample_data/coa_sample_data.json') as file:
            self.coa_data = json.load(file)

        TestUtils._create_default_mapping()
        TestUtils._create_finacial_tag_mapping()

    def test_001_get_coa_map_success(self):
        """
        Getting coa map information with existing company id
        """
        TestUtils._post_with_args(self.client, URLConstant.ChartOfAccounts, self.company.id, self.coa_data)
        code, response = TestUtils._get_with_args(self.client, URLConstant.CoaMapView, self.company.id)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(CoAMap.objects.filter(company=self.company).count() > 0)

    def test_002_get_coa_map_without_default_mapping_success(self):
        """
        Getting coa map with existing company id without default mapping
        """
        TestUtils._delete_default_mapping()
        TestUtils._post_with_args(self.client, URLConstant.ChartOfAccounts, self.company.id, self.coa_data)
        code, response = TestUtils._get_with_args(self.client, URLConstant.CoaMapView, self.company.id)
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.OBJECT_RESOURCE_NOT_FOUND))

    def test_003_get_coa_map_exists_success(self):
        """
        Getting coa map with existing company id with exists data
        """
        TestUtils._post_with_args(self.client, URLConstant.ChartOfAccounts, self.company.id, self.coa_data)
        TestUtils._get_with_args(self.client, URLConstant.CoaMapView, self.company.id)
        code, response = TestUtils._get_with_args(self.client, URLConstant.CoaMapView, self.company.id)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(CoAMap.objects.filter(company=self.company).count() > 0)

    def test_004_get_coa_map_without_coa_failure(self):
        """
        Getting coa map with existing company id without coa
        """
        code, response = TestUtils._get_with_args(self.client, URLConstant.CoaMapView, self.company.id)
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.OBJECT_RESOURCE_NOT_FOUND))

    def test_005_get_coa_map_invalid_company_failure(self):
        """
        Getting coa map with invalid company id
        """
        code, response = TestUtils._get_with_args(self.client, URLConstant.CoaMapView, TestConstants.INVALID_ID)
        self.assertEqual(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.RESOURCE_NOT_FOUND))

    def test_006_create_coa_map_manual_post_success(self):
        """
        Create the coa map  with valid data
        """

        TestUtils._post_with_args(self.client, URLConstant.ChartOfAccounts, self.company.id, self.coa_data)
        TestUtils._get_with_args(self.client, URLConstant.CoaMapView, self.company.id)
        self.data = self.coamap_data
        code, response = TestUtils._post_with_args(self.client, URLConstant.CoaMapView, self.company.id, self.data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)

    def test_007_create_coa_map_manual_post_with_no_data_changes_success(self):
        """
        Create the coa map with no data changes
        """
        TestUtils._post_with_args(self.client, URLConstant.ChartOfAccounts, self.company.id, self.coa_data)
        TestUtils._get_with_args(self.client, URLConstant.CoaMapView, self.company.id)
        self.data = {}
        code, response = TestUtils._post_with_args(self.client, URLConstant.CoaMapView, self.company.id, self.data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.NO_DATA_CHANGES))

    def test_008_update_coa_map_verified_by_user_success(self):
        """
        Reset all verified by user column for particular company
        """

        TestUtils._post_with_args(self.client, URLConstant.ChartOfAccounts, self.company.id, self.coa_data)
        TestUtils._get_with_args(self.client, URLConstant.CoaMapView, self.company.id)
        TestUtils._post_with_args(self.client, URLConstant.CoaMapView, self.company.id, self.coamap_data)
        self.data = {}
        code, response = TestUtils._put_with_args(self.client, URLConstant.CoaMapView, self.company.id, self.data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.COAMAP_UPDATED_SUCCESSFULLY))

    def test_009_delete_coa_map_success(self):
        """
        Deleting all exists coa map
        """

        TestUtils._post_with_args(self.client, URLConstant.ChartOfAccounts, self.company.id, self.coa_data)
        TestUtils._get_with_args(self.client, URLConstant.CoaMapView, self.company.id)
        code, response = TestUtils._delete(self.client, URLConstant.CoaMapView, self.company.id)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.DELETED_SUCCESSFULLY))

    def test_010_delete_coa_map_failure(self):
        """
        Deleting all not exists coa map
        """

        code, response = TestUtils._delete(self.client, URLConstant.CoaMapView, self.company.id)
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.OBJECT_RESOURCE_NOT_FOUND))

    def test_011_delete_coa_map_invalid_company_failure(self):
        """
        Deleting all exists coa map with invalid company
        """

        code, response = TestUtils._delete(self.client, URLConstant.CoaMapView, TestConstants.INVALID_ID)
        self.assertEqual(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.RESOURCE_NOT_FOUND))

    def test_012_delete_coa_map_unauthorized_access_failure(self):
        """
        Removing all coa map with unauthorized access
        """
        self.client.logout()
        self.login = TestUtils._user_login(self.client, "ut_user001")
        code, response = TestUtils._delete(self.client, URLConstant.CoaMapView, self.company.id)
        self.assertEqual(code, ResponseCodeConstant.UNAUTHORIZED_ACCESS_401)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.UNAUTHORIZED_ACCESS))
