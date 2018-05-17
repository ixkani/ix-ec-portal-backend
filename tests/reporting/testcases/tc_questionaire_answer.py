from rest_framework.test import APITestCase

from portalbackend.lendapi.reporting.models import Answer, Question
from portalbackend.validator.errormapping import ErrorMessage

from tests.utils import TestUtils
from tests.constants import ResponseCodeConstant, TestConstants, CompanyConstant, URLConstant


class _001_QuestionnaireDetailsTestCase(APITestCase):
    """
    Tests the QuestionnaireDetails View
    """

    def setUp(self):
        self.superuser = TestUtils._create_superuser()

        self.company = TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        self.meta = TestUtils._create_companymeta(self.company.id)

        self.user = TestUtils._create_user('ut_user001', self.company.id)

        self.login = TestUtils._admin_login(self.client)

    def test_001_create_questionnaire_answer_without_monthly_report_failure(self):
        """
        Create answer for questionnaire without report
        """
        self.data = [{
            "question": 1,
            "answer": 100
        }
        ]
        code, response = TestUtils._post_with_args(self.client, URLConstant.QuestionnaireDetail,
                                                   [self.company.id, TestConstants.INVALID_ID], self.data)
        self.assertEqual(code, ResponseCodeConstant.FAILURE_400)
        self.assertTrue(
            TestUtils._check_response_message(response, ErrorMessage.MISSING_MONTHLY_REPORTING_PREVIOUS_PERIOD))

    def test_002_create_questionnaire_answer_success(self):
        """
        Create answer for questionnaire with report id
        """
        self.data = [{
            "question": 1,
            "answer": 100
        }
        ]
        TestUtils._create_question_catagory()
        TestUtils._create_question(self.company)
        report = TestUtils._create_monthly_report(self.company)
        TestUtils._post_with_args(self.client, URLConstant.QuestionnaireDetail, [self.company.id, '2016-10'], self.data)

        # Create answer for questionnaire with report id with exisitng data
        self.data = [{
            "question": Question.objects.all().first().id,
            "answer": 101
        }
        ]
        code, response = TestUtils._post_with_args(self.client, URLConstant.QuestionnaireDetail,
                                                   [self.company.id, report.id], self.data)
        print(response)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(Answer.objects.filter(company=self.company).count() > 0)

        # Getting questionnaire with report id with answer
        code, response = TestUtils._get_with_args(self.client, URLConstant.QuestionnaireDetail,
                                                  [self.company.id, report.id])
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)

    def test_003_get_questionnaire_without_answer_success(self):
        """
        Get questionnaire with report id without answer
        """

        TestUtils._create_question_catagory()
        TestUtils._create_question(self.company)
        report = TestUtils._create_monthly_report(self.company)

        code, response = TestUtils._get_with_args(self.client, URLConstant.QuestionnaireDetail,
                                                  [self.company.id, report.id])
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.DATA_NOT_FOUND))

    def test_004_get_questionnaire_with_invalid_comapny_failure(self):
        """
        get questionnaire with report id without company
        """

        TestUtils._create_question_catagory()
        TestUtils._create_question(self.company)
        report = TestUtils._create_monthly_report(self.company)

        code, response = TestUtils._get_with_args(self.client, URLConstant.QuestionnaireDetail,
                                                  [TestConstants.INVALID_ID, report.id])
        self.assertEqual(code, ResponseCodeConstant.RESOURCE_NOT_FOUND_404)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.RESOURCE_NOT_FOUND))
