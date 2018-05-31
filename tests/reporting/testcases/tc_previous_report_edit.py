import os
import json

from rest_framework.test import APITestCase

from tests.constants import ResponseCodeConstant, CompanyConstant, URLConstant
from tests.utils import TestUtils


class _001_PreviousMonthlyReportEditDetailsTestCase(APITestCase):
    """
    Tests the PreviousMonthlyReportEditDetails View
    """

    def setUp(self):
        self.superuser = TestUtils._create_superuser()

        self.company = TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        self.meta = TestUtils._create_companymeta(self.company.id)

        self.user = TestUtils._create_user('ut_user001', self.company.id)

        self.login = TestUtils._admin_login(self.client)

        base_path = os.path.dirname(os.path.realpath(__file__))

        with open(base_path + '/sample_data/income_statement_sample_data.json') as file:
            self.is_data = json.load(file)

        with open(base_path + '/sample_data/balance_sheet_sample_data.json') as file:
            self.bs_data = json.load(file)

        TestUtils._create_default_mapping()
        TestUtils._create_finacial_tag_mapping()

        TestUtils._post_with_args(self.client, URLConstant.BalanceSheetView, self.company.id,
                                  self.bs_data)
        TestUtils._post_with_args(self.client, URLConstant.IncomeStatementView, self.company.id,
                                  self.is_data)

        self.report = TestUtils._create_monthly_report(self.company)
        self.answer = TestUtils._create_answer(company=self.company, report=self.report,
                                               question=1, answer=100)

    def test_001_update_previous_monthly_report_edit_details_success(self):
        """
        update previous monthly report edit details
        """

        edited_data = {
            "Balancesheet": {
                "data": {
                    "Cash": "3",
                    "OtherCurrentLiabilities": "",
                    "Currentbalance": "4"  # invalid Financial Tag
                }
            },
            "Incomestatement": {
                "data": {
                    "Ebitda": "3",
                    "RecurringRevenues": "",
                    "IncomeValue": "4"  # invalid Financial Tag
                }
            },
            "Answers": [
                {
                    "answer_data_type": "integer",
                    "question_choices": None,
                    "answer": {
                        "id": self.answer.id,
                        "answer": "23"
                    },
                    "question_category": 2,
                    "company": 1,
                    "question_text": "How many Current Full-Time Employees are at the company?",
                    "answer_validation_regex": "[0-9]+",
                    "common_to_all_companies": True,
                    "next_question": None,
                    "short_tag": "empl_ft",
                    "show_on_ui": True,
                    "ask_order": 100,
                    "id": 1,
                    "next_question_if": None
                }
            ]
        }
        code, response = TestUtils._put_with_args(self.client, URLConstant.PreviousMonthlyReportEditDetails,
                                                  [self.company.id, self.report.id], edited_data)
        self.assertEqual(code, ResponseCodeConstant.SUCCESS_200)
