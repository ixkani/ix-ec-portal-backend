APP_NAME = "Espresso Capital"
FORGOT_PASSWORD_EMAIL_BODY = "We received a request to reset your Espresso Capital password.\n\nClick on below link to " \
                             "change your password.\n\n"
MONTHLY_REPORT_KEY_ERROR_EMAIL_SUBJECT = "Espresso Capital - Monthly Report"

MONTHLY_REPORT_KEY_ERROR_ADMIN_EMAIL_BODY = "We faced an exception during the generate statement process.<br><br>Check the " \
                                            "below response for more information.<br>"


PREVIOUS_MONTHLY_REPORT_DOWNLOAD_FILE_PREFIX = "Monthly Report for "

COMAPANY_META_EMAIL_SUBJECT = "Company Metadata Missing for "
COMAPANY_META_EMAIL_BODY = "Espresso capital faced an configuration error where company meta data is not found for following company profile \n"

COMAPANY_CURRENT_REPORT_PERIOD_EMAIL_SUBJECT = "Current Reporting period is missing for "
COMAPANY_CURRENT_REPORT_PERIOD_EMAIL_BODY = "Espresso capital faced an configuration error where company current reporting period is not found for following company profile \n"

COMPANY_MISCONFIG_EMAIL_SUBJECT = "Company Access Key configuration missing for  "
COMPANY_MISCONFIG_EMAIL_BODY = "Espresso capital faced an configuration error where company access keys are not configured for following company profile \n"

LOG_PREV_REPORT_EDIT_SUBJECT = "IMPORTANT: %s has changed their Historical Monthly Reporting Data for %s"

LOG_PREV_REPORT_EDIT_BODY = "The following changes have been made to the <b>%s</b> monthly reporting submission for " \
                            "<b>%s</b> by <b>%s</b> <br><br>" \
                            "<table border='1' style='border-collapse:collapse; border-spacing: 50px 0; font-family:Sans-Serif; font-size:14px'" \
                            "<tr><th>Section Name</th>" \
                            "<th>Changed Item Desc.</th>" \
                            "<th>Old Value</th>" \
                            "<th>New value</th>" \
                            "<th>Changed By</th>" \
                            "<th>Date changed</th></tr>%s</table><br>" \

SESSION_EXPIRE_MINUTES = 60

SESSION_SAVE_URLS = ['accounting/balancesheet/', 'accounting/incomestatement/',
                     'accounting/coamap/', 'monthlyreport/\d{4}-\d{2}/questionnaire/',
                     'monthlyreport/signoff/','logout', ]

ERROR_TAG_EMAIL_ADMIN_BODY = "Admin,<br><p>%s</p><br><b>Company Details</b><br><br>" \
                             "<table border='1' style='border-collapse:collapse'" \
                             "<tr><td>Company Name</td> <td>%s</td>" \
                             "<tr><td>Company Id</td> <td>%s</td>" \
                             "<tr><td>Accounting Type</td> <td>%s</td>" \
                             "<tr><td>Monthly reporting current period</td> <td>%s</td>" \
                             "<tr><td>Monthly reporting next period</td> <td>%s</td></table><br><br>" \
                             "<b>Errors</b><br><p>" \
                             "The following financial statement entry tag map are not found%s" \
                             "<br><b> Actual JSON Response </b> <pre>%s</pre>"

COMPANY_META_NOT_FOUND_EMAIL_ADMIN = "Admin,<br><p>%s</p><br><b>Company Details</b><br><br>" \
                                     "<table border='1' style='border-collapse:collapse'>" \
                                     "<tr><td>Company Name</td> <td>%s</td>" \
                                     "<tr><td>Company Id</td> <td>%s</td>" \
                                     "<tr><td>Accounting Type</td> <td>%s</td>"

COMPANY_PERIOD_NOT_FOUND_EMAIL_ADMIN = "Admin,<br><p>%s</p><br><b>Company Details</b><br><br>" \
                                       "<table border='1' style='border-collapse:collapse'>" \
                                       "<tr><td>Company Name</td> <td>%s</td>" \
                                       "<tr><td>Company Id</td> <td>%s</td>" \
                                       "<tr><td>Accounting Type</td> <td>%s</td>"

COMPANY_MISCONFIG_EMAIL_ADMIN = "Admin,<br><p>%s</p><br><b>Company Details</b><br><br>" \
                                "<table border='1' style='border-collapse:collapse'>" \
                                "<tr><td>Company Name</td> <td>%s</td>" \
                                "<tr><td>Company Id</td> <td>%s</td>" \
                                "<tr><td>Accounting Type</td>  <td>%s</td></table>" \
                                "<br><b>Errors</b><br><p> " \
                                "%s"
