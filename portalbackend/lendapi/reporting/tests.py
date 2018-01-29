from django.test import TestCase

from .models import Question, Answer, QuestionCategory, MonthlyReport
from rest_framework.test import APIRequestFactory, force_authenticate

from portalbackend.lendapi.v1.reporting.views import QuestionnaireList
from portalbackend.lendapi.accounts.models import Company, User
import pprint
import datetime
import json


class QuestionnaireTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = '/lend/v1/company/1/monthlyreport/2017-09/questionnaire/'
        self.company = Company.objects.create(id=1, name="Test Company", external_id="ABC123",
                                              website="https://en.wikipedia.org/wiki/Unit_testing", employee_count=1)
        self.user = User.objects.create(id=1, first_name='test', last_name='user', email='test@mail.com',
                                        username='testusername', password='TestPass1', company=self.company)
        self.monthlyReport = MonthlyReport.objects.create(id=1, company=self.company,
                                                          period_ending=datetime.date(2017, 9, 30),
                                                          due_date=datetime.date(2017, 10, 30),
                                                          status=MonthlyReport.IN_PROGRESS)
        self.question_category = QuestionCategory.objects.create(group_name="Compliance", purpose="To Comply")

        self.question_one_followup = Question.objects.create(id=2, company=self.company,
                                                             question_category=self.question_category,
                                                             short_tag="Followup Question", answer_data_type="Text",
                                                             ask_order=2, show_on_ui=True,
                                                             common_to_all_companies=True,
                                                             question_text="And Why is That")

        self.question_one = Question.objects.create(id=1, company=self.company,
                                                    question_category=self.question_category,
                                                    short_tag="First Question", answer_data_type="Text",
                                                    ask_order=1, show_on_ui=True, common_to_all_companies=True,
                                                    question_text="Are you enjoying the borrower portal",
                                                    question_choices=['Yes', 'No'],
                                                    next_question=self.question_one_followup, next_question_if='Yes')
        self.question_two = Question.objects.create( id=3, company=self.company,
                                                     question_category=self.question_category,
                                                     short_tag="Third question", answer_data_type="Text",
                                                     ask_order=3, show_on_ui=True,
                                                     common_to_all_companies=True,
                                                     question_text="Please answer this question in a timely manner")

    def test_get(self):
        request = self.factory.get(self.url, format='json')
        force_authenticate(request, user=self.user)
        response = QuestionnaireList.as_view()(request, pk=1, period='2017-09')
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        data = [
            {'answer': 'Yes',
             'question': 1},
            {'answer': 'Because i love it',
             'question': 2},
            {'answer': 'Fine ill answer faster',
             'question': 3}
        ]
        request = self.factory.post(self.url, format='json', data=data)
        force_authenticate(request, user=self.user)
        response = QuestionnaireList.as_view()(request, pk=1, period='2017-09')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertNotEqual(data[0]['answer'], None)

