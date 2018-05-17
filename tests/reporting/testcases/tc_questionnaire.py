from rest_framework.test import APITestCase

from portalbackend.validator.errormapping import ErrorMessage

from tests.utils import TestUtils
from tests.constants import ResponseCodeConstant, CompanyConstant, URLConstant


class _001_QuestionnaireListTestCase(APITestCase):
    """
    Tests the QuestionnaireList View
    """

    def setUp(self):
        self.superuser = TestUtils._create_superuser()

        self.company = TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        self.meta = TestUtils._create_companymeta(self.company.id)

        self.user = TestUtils._create_user('ut_user001', self.company.id)

        self.login = TestUtils._admin_login(self.client)

    def test_001_get_questionnaire_without_question_success(self):
        """
        get questionnaire without questions data
        """
        code, response = TestUtils._get_with_args(self.client, URLConstant.QuestionnaireList, self.company.id)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
        self.assertTrue(TestUtils._check_response_message(response, ErrorMessage.NO_ANSWER_FOUND))

    def test_002_get_questionnaire_success(self):
        """
        get questionnaire with questionnaire data
        """
        TestUtils._create_question_catagory()
        TestUtils._create_question(self.company)
        code, response = TestUtils._get_with_args(self.client, URLConstant.QuestionnaireList, self.company.id)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
