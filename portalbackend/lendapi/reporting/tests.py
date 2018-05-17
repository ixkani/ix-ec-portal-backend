from tests.reporting.testcases import tc_monthly_report, tc_questionaire_answer, tc_questionnaire, \
    tc_previous_report_edit

# @unittest - Tests Monthly Report List api calls
tc_monthly_report_list = tc_monthly_report._001_MonthlyReportListTestCase

# @unittest - Tests Monthly Report Details api calls
tc_monthly_report_details = tc_monthly_report._002_MonthlyReportDetailsTestCase

# @unittest - Tests Monthly Report Status api calls
tc_monthly_report_status_details = tc_monthly_report._003_MonthlyReportStatusDetailTestCase

# @unittest - Tests Monthly Report Signoff calls
tc_monthly_report_signoff_details = tc_monthly_report._004_MonthlyReportSignoffTestCase

# @unittest - Tests Questionnaire Details api calls
tc_questionnaire_details = tc_questionaire_answer._001_QuestionnaireDetailsTestCase

# @unittest - Tests Questionnaire List api calls
tc_questionnaire_list = tc_questionnaire._001_QuestionnaireListTestCase

# @unittest - Tests Previous report edit api calls
tc_report_edit_details = tc_previous_report_edit._001_PreviousMonthlyReportEditDetailsTestCase