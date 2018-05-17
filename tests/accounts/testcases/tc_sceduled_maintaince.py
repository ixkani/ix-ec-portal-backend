from rest_framework.test import APITestCase

from tests.utils import TestUtils


class _001_ScheduledMaintenanceDetailsTestCase(APITestCase):
    def setUp(self):
        TestUtils._create_scheduled_maintenance()

    def test_001_schedule_maintenance_on_success(self):
        """
        Scheduled Maintenance is Turned ON
        """
        code, response = TestUtils._get(self.client, 'scheduled-maintenance')
        self.assertTrue(TestUtils._check_response_value(response, "is_under_maintenance", True))
        self.assertTrue(TestUtils._check_response_key_success(response, 'message'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'is_under_maintenance'))
        self.assertTrue(TestUtils._check_response_key_success(response, 'end_time'))

    def test_002_schedule_maintenance_off_failure(self):
        """
        Scheduled Maintenance is Turned OFF
        """
        TestUtils._update_scheduled_maintenance(False)
        code, response = TestUtils._get(self.client, 'scheduled-maintenance')
        self.assertTrue(TestUtils._check_response_value(response, "is_under_maintenance", False))

    def test_003_schedule_maintenance_off_timeout_failure(self):
        """
        Scheduled Maintenance is timeout to off
        """
        TestUtils._update_scheduled_maintenance(True)
        code, response = TestUtils._get(self.client, 'scheduled-maintenance')
        self.assertTrue(TestUtils._check_response_value(response, "is_under_maintenance", False))
