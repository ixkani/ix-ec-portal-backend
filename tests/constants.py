from portalbackend import settings


class TestConstants:
    """
    Common configurable constants
    """
    INVALID_ID = 100
    INVALID_STRING = "DUMMY"
    INVALID_USERNAME = "dummmy_username"
    INVALID_PASSWORD = "dummmy_password"
    INVALID_EMAIL = "dummmy_email"
    INVALID_TOKEN = "dummmytoken"
    INVALID_TOTP = "1234567"
    INVALID_PERIOD = 2018 - 10
    UNBALANCED_THRESHOLD = 0.1


    HOST_URL = settings.HOST_URL
    SECURE_CONNECTION = True



class UserConstant:
    """
    User related configurable constants
    """
    ADMIN_USERNAME = 'ut_admin'
    ADMIN_PASSWORD = 'Espresso@1'
    ADMIN_EMAIL = 'ut_admin@unittesting.com'

    USER_PASSWORD = 'Espresso@1'
    USER_EMAIL = 'ut_user@unittesting.com'
    USER_ROLE = 'Financial Manager'


class CompanyConstant:
    """
    Company related configurable constants
    """
    DEFAULT_COMPANY_EMPLOYEE_COUNT = 10
    DEFAULT_COMPANY_EXTERNALID = 'UT00A'
    DEFAULT_COMPANY_WEBSITE = 'espressocapital.com'

    COMPANY_NAME_001 = 'UTCompany001'
    COMPANY_NAME_002 = 'UTCompany002'

    COMPANY_CURRENT_REPORT_PERIOD = '2016-10-31'
    COMPANY_NEXT_REPORT_PERIOD = '2016-11-30'

    PREV_FISCAL_YEAR_START_DATE = '2016-01-31'
    PREV_FISCAL_YEAR_END_DATE = '2016-12-31'
    PREV_FISCAl_YEAR_LABEL = '2016FY'

    CUR_FISCAL_YEAR_START_DATE = '2017-01-31'
    CUR_FISCAL_YEAR_END_DATE = '2017-12-31'
    CUR_FISCAl_YEAR_LABEL = '2017FY'

    # This date will be one month ahead of CUR_FISCAL_YEAR_END_DATE
    # because this variable is used for auto creation of fiscal year in signoff call

    MONTHLY_REPORT_NEXT_PERIOD = '2018-01-31'


class AccountingConstant:
    """
    Accounting related configurable constants
    """
    CHART_OF_ACCOUNTS = "CHART_OF_ACCOUNTS"
    TRIAL_BALANCE = "TRIAL_BALANCE"


class ContactConstant:
    """
    Contact related configurable constants
    """
    DEFAULT_CONTACT_FIRST_NAME = "TEST"
    DEFAULT_CONTACT_LAST_NAME = "CONTACT"
    DEFAULT_CONTACT_TITLE = "TEST COMPANY CONTACT"
    DEFAULT_CONTACT_EMAIL = "testcontact@espressocapital.com"
    DEFAULT_CONTACT_EXTERNALID = 'UTC001'


class ResponseCodeConstant:
    """
    Response code non-configurable constants
    """
    SUCCESS_200 = 200
    REDIRECT_302 = 302
    FAILURE_400 = 400
    UNAUTHORIZED_ACCESS_401 = 401
    RESOURCE_NOT_FOUND_404 = 404
    MISSING_MONTHLY_REPORTING_CURRENT_PERIOD = 412
    INVALID_FILE_FORMAT = 422
    INTERNAL_SERVER_ERROR_500 = 500


class ResponseMessageConstant:
    """
    Response message non-configurable constants
    """
    INTERNAL_SERVER_ERROR_500 = "The server could not process the request."
    UNAUTHORIZED_ACCESS = "User unauthorized access."
    RESOURCE_NOT_FOUND = "Resource not found."
    AUTH_FAILED = "Authentication credentials were not provided."


class URLConstant:
    """
    url name list non-configurable values
    """
    # accounts

    # user
    UserList = 'user-list'
    Me = 'me'
    UserDetails = 'user-detail'

    # company
    CompanyList = 'company-list'
    CompanyDetails = 'company-detail'
    CompanyMetaDetails = 'company-meta'

    # contact
    ContactDetails = 'company-contacts-list'
    EspressoContacts = 'company-special-contacts-list'

    # login & Logout
    LoginView = 'login'
    LogoutView = 'logout'

    # Scheduled Maintenance
    ScheduledMaintenanceDetails = 'scheduled-maintenance'

    # 2FA
    TwoFactorAuthenticationDetails = 'twofactor-auth'

    # change password
    EmailValidation = 'validate-forgot-password'

    # change password
    ForgotPassword = 'forgot-password'
    ChangePassword = 'change-password'

    # accounting

    # connect
    CreateConnection = "connect"

    # auth code handler's
    QuickBooksAuthCodeHandler = "qbo-authCodeHandler"
    XeroAuthCodeHandler = "xero-authCodeHandler"

    # connection status
    RefreshToken = "refresh"
    DisconnectToken = "disconnect"
    TokenValid = "qbo-valid"
    LoginStatus = "qbo-status"

    # trail balance
    TrialBalanceView = "trial-balance"

    # chart of accounts
    ChartOfAccounts = "chart-of-accounts"

    # generate statement
    Statement = "statement-view"
    BalanceSheetView = "balance-sheet"
    IncomeStatementView = "income-statement"

    # coa map
    CoaMapView = "coa-map"

    # generate pdf
    GeneratePDF = "generate-pdf"

    # Reporting

    # monthly report
    MonthlyReportList = "report-list"
    MonthlyReportDetail = "report-detail"
    MonthlyReportStatusDetail = "report-status"
    PreviousMonthlyReportEditDetails = "prev-report-edit"
    MonthlyReportSignoff = "report-signoff"

    # Questionnaire
    QuestionnaireDetail = "report-questionnaire-details"
    QuestionnaireList = "report-questionnaire-list"
