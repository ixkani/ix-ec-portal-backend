import os
import json
import datetime

from rest_framework.test import APITestCase

from portalbackend.lendapi.reporting.models import MonthlyReport
from portalbackend.validator.errormapping import ErrorMessage

from tests.utils import TestUtils
from tests.constants import ResponseCodeConstant, TestConstants, CompanyConstant, URLConstant, \
    UserConstant


class _001_MonthlyReportListTestCase(APITestCase):
    """
    Tests the MonthlyReportList View
    """

    def setUp(self):
        self.superuser = TestUtils._create_superuser()

        self.company = TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        self.meta = TestUtils._create_companymeta(self.company.id)

        self.user = TestUtils._create_user('ut_user001', self.company.id)

        self.login = TestUtils._admin_login(self.client)

    def test_001_create_monthly_report_success(self):
        """
        create monthly report with valid data
        """

        self.data = {
            "company": self.company.id,
            "status": MonthlyReport.IN_PROGRESS,
            "period_ending": CompanyConstant.COMPANY_CURRENT_REPORT_PERIOD,
            "due_date": CompanyConstant.COMPANY_CURRENT_REPORT_PERIOD
        }

        code, response = TestUtils._post_with_args(self.client, URLConstant.MonthlyReportList, self.company.id,
                                                   self.data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertEquals(MonthlyReport.objects.filter(company=self.company).count(), 1)

    def test_002_create_monthly_report_without_current_report_period_success(self):
        """
        create monthly report with valid data without current reporting period in company meta
        """

        self.data = {
            "company": self.company.id,
            "status": MonthlyReport.IN_PROGRESS,
            "period_ending": CompanyConstant.COMPANY_CURRENT_REPORT_PERIOD,
            "due_date": CompanyConstant.COMPANY_CURRENT_REPORT_PERIOD
        }
        self.meta.monthly_reporting_current_period = None
        self.meta.save()
        self.client.logout()
        self.login = TestUtils._user_login(self.client, "ut_user001")
        code, response = TestUtils._post_with_args(self.client, URLConstant.MonthlyReportList, self.company.id,
                                                   self.data)
        self.assertEqual(code, ResponseCodeConstant.MISSING_MONTHLY_REPORTING_CURRENT_PERIOD)
        self.assertTrue(
            TestUtils._check_response_message(response, ErrorMessage.MISSING_MONTHLY_REPORTING_CURRENT_PERIOD))

    def test_003_create_monthly_report_without_initial_setup_success(self):
        """
        create monthly report with valid data without initial setup
        """

        self.data = {
            "company": self.company.id,
            "status": MonthlyReport.IN_PROGRESS,
            "period_ending": CompanyConstant.COMPANY_CURRENT_REPORT_PERIOD,
            "due_date": CompanyConstant.COMPANY_CURRENT_REPORT_PERIOD
        }
        self.meta.is_initial_setup = False
        self.meta.save()
        code, response = TestUtils._post_with_args(self.client, URLConstant.MonthlyReportList, self.company.id,
                                                   self.data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertEquals(MonthlyReport.objects.filter(company=self.company).count(), 1)

    def test_004_create_monthly_report_with_inprogress_success(self):
        """
        create monthly report with already exists
        """

        self.data = {
            "company": self.company.id,
            "status": MonthlyReport.IN_PROGRESS,
            "period_ending": CompanyConstant.COMPANY_CURRENT_REPORT_PERIOD,
            "due_date": CompanyConstant.COMPANY_CURRENT_REPORT_PERIOD
        }
        TestUtils._post_with_args(self.client, URLConstant.MonthlyReportList, self.company.id, self.data)
        code, response = TestUtils._post_with_args(self.client, URLConstant.MonthlyReportList, self.company.id,
                                                   self.data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(
            TestUtils._check_response_message(response, ErrorMessage.MONTHLY_REPORT_ALREADY_EXISTS_WITH_INPROGRESS))

    def test_005_get_monthly_report_success(self):
        """
        get monthly report with existing data
        """

        self.data = {
            "company": self.company.id,
            "status": MonthlyReport.IN_PROGRESS,
            "period_ending": CompanyConstant.COMPANY_CURRENT_REPORT_PERIOD,
            "due_date": CompanyConstant.COMPANY_CURRENT_REPORT_PERIOD
        }

        TestUtils._post_with_args(self.client, URLConstant.MonthlyReportList, self.company.id,
                                  self.data)
        code, response = TestUtils._get_with_args(self.client, URLConstant.MonthlyReportList, self.company.id)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertEquals(MonthlyReport.objects.filter(company=self.company).count(), 1)

    def test_006_get_monthly_report_without_data_failure(self):
        """
        get monthly report with without existing data
        """

        code, response = TestUtils._get_with_args(self.client, URLConstant.MonthlyReportList, self.company.id)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.DATA_NOT_FOUND))

    def test_007_get_monthly_report_with_invalid_company_failure(self):
        """
        get monthly report with with invalid company
        """

        code, response = TestUtils._get_with_args(self.client, URLConstant.MonthlyReportList, TestConstants.INVALID_ID)
        self.assertEqual(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.RESOURCE_NOT_FOUND))


class _002_MonthlyReportDetailsTestCase(APITestCase):
    """
    Tests the MonthlyReportDetails View
    """

    def setUp(self):
        self.superuser = TestUtils._create_superuser()

        self.company = TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        self.meta = TestUtils._create_companymeta(self.company.id)

        self.user = TestUtils._create_user('ut_user001', self.company.id)

        self.login = TestUtils._admin_login(self.client)

        self.report = TestUtils._create_monthly_report(self.company)

    def test_001_get_monthly_report_success(self):
        """
        get monthly report with report id
        """
        code, response = TestUtils._get_with_args(self.client, URLConstant.MonthlyReportDetail,
                                                  [self.company.id, self.report.id])
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_key_success(response, 'due_date'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'period_ending'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'lookup_period'))

    def test_002_get_monthly_report_success(self):
        """
        get monthly report with report month
        """
        code, response = TestUtils._get_with_args(self.client, URLConstant.MonthlyReportDetail,
                                                  [self.company.id, '2016-10'])
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_key_success(response, 'due_date'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'period_ending'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'lookup_period'))

    def test_003_get_monthly_report_failure(self):
        """
        get monthly report with invalid report id
        """
        code, response = TestUtils._get_with_args(self.client, URLConstant.MonthlyReportDetail,
                                                  [self.company.id, TestConstants.INVALID_ID])
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.MONTHLY_REPORT_NOT_FOUND))

    def test_004_get_monthly_report_failure(self):
        """
        get monthly report with invalid report month

        """
        code, response = TestUtils._get_with_args(self.client, URLConstant.MonthlyReportDetail,
                                                  [self.company.id, TestConstants.INVALID_PERIOD])
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.MONTHLY_REPORT_NOT_FOUND))

    def test_005_update_monthly_report_success(self):
        """
        update monthly report with report id
        """
        self.data = {
            "submitted_on": datetime.date.today(),
        }
        code, response = TestUtils._put_with_args(self.client, URLConstant.MonthlyReportDetail,
                                                  [self.company.id, self.report.id], self.data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_value(response, 'submitted_on', str(datetime.date.today())))

    def test_006_update_monthly_report_success(self):
        """
        update monthly report with report month
        """
        self.data = {
            "submitted_on": datetime.date.today(),
        }
        code, response = TestUtils._put_with_args(self.client, URLConstant.MonthlyReportDetail,
                                                  [self.company.id, '2016-10'], self.data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_value(response, 'submitted_on', str(datetime.date.today())))

    def test_007_update_monthly_report_failure(self):
        """
        update monthly report with invalid data
        """
        self.data = {
            "submitted_on": datetime.datetime.now(),
        }
        code, response = TestUtils._put_with_args(self.client, URLConstant.MonthlyReportDetail,
                                                  [self.company.id, '2016-10'], self.data)
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_key_error(response, 'submitted_on'))

    def test_008_update_monthly_report_failure(self):
        """
        update monthly report with invalid report month
        """
        self.data = {
            "submitted_on": datetime.datetime.now(),
        }
        code, response = TestUtils._put_with_args(self.client, URLConstant.MonthlyReportDetail,
                                                  [self.company.id, TestConstants.INVALID_PERIOD], self.data)
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.MONTHLY_REPORT_NOT_FOUND))

    def test_009_delete_monthly_report_success(self):
        """
        delete monthly report with report id
        """
        code, response = TestUtils._delete(self.client, URLConstant.MonthlyReportDetail,
                                           [self.company.id, self.report.id])
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.DELETED_SUCCESSFULLY))

    def test_010_get_monthly_report_success(self):
        """
        delete monthly report with report month
        """
        code, response = TestUtils._delete(self.client, URLConstant.MonthlyReportDetail,
                                           [self.company.id, '2016-10'])
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.DELETED_SUCCESSFULLY))

    def test_011_get_monthly_report_invalid_date_failure(self):
        """
        delete monthly report with invalid report month
        """
        code, response = TestUtils._delete(self.client, URLConstant.MonthlyReportDetail,
                                           [self.company.id, TestConstants.INVALID_PERIOD])
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.MONTHLY_REPORT_NOT_FOUND))

    def test_012_delete_monthly_report_unauthorized_access_failure(self):
        """
        Delete monthly report with report month with  unauthorized access
        """
        self.client.logout()
        self.login = TestUtils._user_login(self.client, "ut_user001")
        code, response = TestUtils._delete(self.client, URLConstant.MonthlyReportDetail,
                                           [self.company.id, TestConstants.INVALID_PERIOD])
        self.assertEquals(code, ResponseCodeConstant.UNAUTHORIZED_ACCESS_401)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.UNAUTHORIZED_ACCESS))


class _003_MonthlyReportStatusDetailTestCase(APITestCase):
    """
    Tests the MonthlyReportStatusDetail View
    """

    def setUp(self):
        self.superuser = TestUtils._create_superuser()

        self.company = TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        self.meta = TestUtils._create_companymeta(self.company.id)

        self.user = TestUtils._create_user('ut_user001', self.company.id)

        self.login = TestUtils._admin_login(self.client)

        self.report = TestUtils._create_monthly_report(self.company)

    def test_001_get_monthly_report_status_success(self):
        """
        get monthly report status with report id
        """
        code, response = TestUtils._get_with_args(self.client, URLConstant.MonthlyReportStatusDetail,
                                                  [self.company.id, self.report.id])
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_key_success(response, 'status'))

    def test_002_get_monthly_report_status_success(self):
        """
        get monthly report status with report month
        """
        code, response = TestUtils._get_with_args(self.client, URLConstant.MonthlyReportStatusDetail,
                                                  [self.company.id, '2016-10'])
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_key_success(response, 'status'))

    def test_003_get_monthly_report_status_failure(self):
        """
        get monthly report status with invalid report id
        """
        code, response = TestUtils._get_with_args(self.client, URLConstant.MonthlyReportStatusDetail,
                                                  [self.company.id, TestConstants.INVALID_ID])
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.MONTHLY_REPORT_NOT_FOUND))

    def test_004_get_monthly_report_status_failure(self):
        """
        get monthly report status with invalid report month

        """
        code, response = TestUtils._get_with_args(self.client, URLConstant.MonthlyReportStatusDetail,
                                                  [self.company.id, TestConstants.INVALID_PERIOD])
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.MONTHLY_REPORT_NOT_FOUND))


class _004_MonthlyReportSignoffTestCase(APITestCase):
    """
    Tests the MonthlyReportSignoff View
    """

    def setUp(self):
        self.superuser = TestUtils._create_superuser()

        self.company = TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        self.meta = TestUtils._create_companymeta(self.company.id)

        self.user = TestUtils._create_user('ut_user001', self.company.id)

        self.login = TestUtils._admin_login(self.client)

        TestUtils._create_fiscal_year(self.company)

        self.report = TestUtils._create_monthly_report(self.company)

        base_path = os.path.dirname(os.path.realpath(__file__))

        with open(base_path + '/sample_data/coa_sample_data.json') as file:
            self.coa_data = json.load(file)

    def test_001_put_monthly_report_signoff_success(self):
        """
        update monthly report signoff status with report id
        """
        self.data = {
            "signoff_by_name": UserConstant.ADMIN_USERNAME,
            "signoff_by_title": UserConstant.USER_ROLE
        }

        TestUtils._create_default_mapping()
        TestUtils._create_finacial_tag_mapping()
        TestUtils._post_with_args(self.client, URLConstant.ChartOfAccounts, self.company.id, self.coa_data)
        TestUtils._get_with_args(self.client, URLConstant.CoaMapView, self.company.id)
        code, response = TestUtils._put_with_args(self.client, URLConstant.MonthlyReportSignoff,
                                                  [self.company.id], self.data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_value(response, 'signoff_by_name', UserConstant.ADMIN_USERNAME))
        self.assertTrue(TestUtils._check_response_value(response, 'signoff_by_title', UserConstant.USER_ROLE))

    def test_002_put_monthly_report_signoff_failure(self):
        """
        update monthly report signoff status with invalid report id
        """
        self.data = {
            "signoff_by_name": UserConstant.ADMIN_USERNAME,
            "signoff_by_title": UserConstant.USER_ROLE
        }
        MonthlyReport.objects.filter(company=self.company).delete()
        code, response = TestUtils._put_with_args(self.client, URLConstant.MonthlyReportSignoff, [self.company.id],
                                                  self.data)
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.MONTHLY_REPORT_NOT_FOUND))

    def test_003_put_monthly_report_signoff_failure(self):
        """
        update monthly report signoff status with completed report
        """
        self.data = {
            "signoff_by_name": UserConstant.ADMIN_USERNAME,
            "signoff_by_title": UserConstant.USER_ROLE
        }
        self.report.status = MonthlyReport.COMPLETE
        self.report.save()

        code, response = TestUtils._put_with_args(self.client, URLConstant.MonthlyReportSignoff, [self.company.id],
                                                  self.data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(
            TestUtils._check_response_message(response, ErrorMessage.MONTHLY_REPORT_ALREADY_EXISTS_WITH_COMPLETED))

    def test_004_put_monthly_report_signoff_with_auto_fiscal_year_generation_success(self):
        """
        update monthly report signoff status with report id with auto fiscal year creation
        """
        self.data = {
            "signoff_by_name": UserConstant.ADMIN_USERNAME,
            "signoff_by_title": UserConstant.USER_ROLE
        }

        TestUtils._create_default_mapping()
        TestUtils._create_finacial_tag_mapping()
        self.meta.monthly_reporting_next_period = CompanyConstant.MONTHLY_REPORT_NEXT_PERIOD
        self.meta.save()

        TestUtils._post_with_args(self.client, URLConstant.ChartOfAccounts, self.company.id, self.coa_data)
        TestUtils._get_with_args(self.client, URLConstant.CoaMapView, self.company.id)
        code, response = TestUtils._put_with_args(self.client, URLConstant.MonthlyReportSignoff,
                                                  [self.company.id], self.data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_value(response, 'signoff_by_name', UserConstant.ADMIN_USERNAME))
        self.assertTrue(TestUtils._check_response_value(response, 'signoff_by_title', UserConstant.USER_ROLE))
