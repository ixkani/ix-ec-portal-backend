from portalbackend.settings import RUN_UNIT_TEST
from tests.reporting.testcases.tc_monthly_report import _001_MonthlyReportListTestCase, \
    _002_MonthlyReportDetailsTestCase, _003_MonthlyReportStatusDetailTestCase, _004_MonthlyReportSignoffTestCase
from tests.reporting.testcases.tc_previous_report_edit import _001_PreviousMonthlyReportEditDetailsTestCase
from tests.reporting.testcases.tc_questionaire_answer import _001_QuestionnaireDetailsTestCase
from tests.reporting.testcases.tc_questionnaire import _001_QuestionnaireListTestCase

if RUN_UNIT_TEST:

    # @unittest - Tests Monthly Report List api calls
    tc_monthly_report_list = _001_MonthlyReportListTestCase

    # @unittest - Tests Monthly Report Details api calls
    tc_monthly_report_details = _002_MonthlyReportDetailsTestCase

    # @unittest - Tests Monthly Report Status api calls
    tc_monthly_report_status_details = _003_MonthlyReportStatusDetailTestCase

    # @unittest - Tests Monthly Report Signoff calls
    tc_monthly_report_signoff_details = _004_MonthlyReportSignoffTestCase

    # @unittest - Tests Questionnaire Details api calls
    tc_questionnaire_details = _001_QuestionnaireDetailsTestCase

    # @unittest - Tests Questionnaire List api calls
    tc_questionnaire_list = _001_QuestionnaireListTestCase

    # @unittest - Tests Previous report edit api calls
    tc_report_edit_details = _001_PreviousMonthlyReportEditDetailsTestCase