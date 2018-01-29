APP_NAME = "Espresso Capital"
FORGOT_PASSWORD_EMAIL_BODY = "We received a request to reset your Espresso Capital password.\n\nClick on below link to " \
                             "change your password.\n\n"
MONTHLY_REPORT_KEY_ERROR_EMAIL_SUBJECT = "Espresso Capital - Monthly Report"

MONTHLY_REPORT_KEY_ERROR_ADMIN_EMAIL_BODY = "We faced an exception during the generate statement process.<br><br>Check the " \
                                      "below response for more information.<br>"

MONTHLY_REPORT_KEY_ERROR_USER_EMAIL_BODY = "At the time of generate statement process, we have faced an exception. Your data are being saved and processed shortly."


COMAPANY_META_EMAIL_SUBJECT = "Company Metadata Missing for "
COMAPANY_META_EMAIL_BODY = "Espresso capital faced an configuration error where company meta data is not found for following company profile \n"

COMAPANY_CURRENT_REPORT_PERIOD_EMAIL_SUBJECT = "Current Reporting period is missing for "
COMAPANY_CURRENT_REPORT_PERIOD_EMAIL_BODY = "Espresso capital faced an configuration error where company current reporting period is not found for following company profile \n"

SESSION_EXPIRE_MINUTES = 60

SESSION_SAVE_URLS = ['accounting/balancesheet/', 'accounting/incomestatement/',
                    'accounting/coamap/', 'monthlyreport/\d{4}-\d{2}/questionnaire/',
                    'monthlyreport/signoff/',]