class ErrorMessage:
    INTERNAL_SERVER_ERROR = "The server could not process the request."
    UNAUTHORIZED_ACCESS = "User unauthorized access."
    RESOURCE_NOT_FOUND = "Resource not found."
    VALIDATION_ERROR = "Validation Failed"
    MISSING_PARAMETERS = "Missing required parameter."
    INVALID_PARAMETERS = "Invalid Paramerters"
    DATA_PARSING_ISSUE = "Data parsing error."
    MULTIPLE_EMAIL_FOUND = "Multiple Email Configured.Please contact admin for support"

    MINIMUM_LENGTH_3 = "Atleast 3 characters required"
    MINIMUM_LENGTH_4 = "Atleast 4 characters required"
    MINIMUM_LENGTH_10 = "Atleast 10s characters required"

    REQUIRED_INVALID_DATA = "Invalid data in the parameter."
    REQUIRED_VALID_DATA = "Missing data in the parameter."
    INVALID_CHOICE = "Ensure the valid choice"

    SKIP_NULL_VALUE = "Null value not supported."
    INVALID_JSON_REQUEST = "Invalid JSON format."

    ALL_SIGHT_CONNECTION = "all sight server connection not established."
    INVALID_PHONE_NUMBER = "Phone number must be entered in the format: +999999999.Up to 15 digits allowed."
    INVALID_DATE_FORMAT = "Required valid date and format (YYYY-MM-DD)"

    # COA
    COA_COMPANY_DELETED = "CoA objects have been deleted"
    NO_QBO_AUTHENTICATION = "no quickbooks authentication"
    COA_FETECHED_SUCCESSFULLY = "successfully fetched chart of accounts"
    INVALID_FILE_FORMAT = "Invalid File Format"

    #COAMap

    COAMAP_UPDATED_SUCCESSFULLY = "COA Map Reseted Successfully"

    # questionarie
    NO_ANSWER_FOUND = "No answers found for period."
    OBJECT_RESOURCE_NOT_FOUND = "Object resource not found."
    NO_DATA_CHANGES = "No Data changed."

    # espresso-contact
    DELETED_SUCCESSFULLY = "Deleted Successfully"

    DATA_NOT_FOUND = "No data available"
    QUESTIONNAIRE_NOT_FOUND = "No Questionnaire found for period."
    MONTHLY_REPORT_NOT_FOUND = "No monthly report found for period."
    MONTHLY_REPORT_ALREADY_EXISTS_WITH_INPROGRESS = "A monthly report already exists and is in progress. "
    MONTHLY_REPORT_ALREADY_EXISTS_WITH_COMPLETED = "Monthly report already completed. "


    MISSING_MONTHLY_REPORTING_CURRENT_PERIOD = "Set the monthly reporting current period date in the company's metadata"
    MISSING_MONTHLY_REPORTING_PREVIOUS_PERIOD = "No Monthly report available for current period"

    INVALID_COA_CSV = "Invalid Chart of Accounts format file uploaded"
    INVALID_TB_CSV = "Invalid Trial Balance format file uploaded"
    INVALID_TB_DATE = "Current period doesn't match in Trial balance"

    TRIAL_BALANCE_RECEIVED_SUCCESS = "trial balance received"
    TRIAL_BALANCE_SAVE_SUCCESS = "saved trial balance"

    MISSING_END_DATE = 'start date sent without end_date'
    INVALID_END_DATE = 'end date is not a valid date (format is YYYY-MM-DD).'
    INVALID_DATE = 'Start or End date is not a valid date (format is YYYY-MM-DD).'

    AUTHENTICATED_SUCCESSFULLY = "successfully authenticated"
    NO_TOKEN_FOUND = "no credentials exist for this company"
    REFRESH_TOKEN_NOT_FOUND = "refresh token not valid, please log in again"
    CREDENTIALS_UPDATED = "Credentials updated"
    NO_TOKEN_AUTHENTICATION = "No connection established"
    USER_NOT_CONNECTED = "User must connect to company"
    REVOKE_SUCCESSFULL = "Revoke successful"
    TOKEN_ALREADY_VALIDATED = "Token already in Use."

    # Xero
    XERO_CONFIGURATION_NOT_FOUND = "Xero not configured for this company."
    XERO_CONNECTION_FAILED = "Xero connection establishing failed."
    XERO_CONNECTION_EXPIRED = "Xero connection expired."
    XERO_CONNECTION_ERROR = "Xero connection error."

    EMAIL_SEND = "Email Send"
    TOKEN_VALID = "Token Valid"
    TOKEN_EXPIRED = "Token Expired"
    PASSWORD_RESET_SUCCESSFUL = "Password reset successful"
    EMAIL_NOT_FOUND = "Account not found"

    #sessions
    SESSION_EXPRIED = "Session Expired"
    SESSION_ALREADY_ACTIVE = "Session Already Active"

    COMPANY_META_NOT_AVAILABLE = "No company metadata found. Your administrator has been notified and will be in " \
                                 "touch as soon as possible to help fix the issue "
    FISCAL_YEAR_MISSING = "Fiscal year ends not configured as proper"
    CREDIT_DEBIT_UNEQUALS = "Debit and Credit are not same for this month."


class UIErrorMessage:
    MINIMUM_LENGTH_1 = "Atleast a character required"
    MINIMUM_LENGTH_3 = "Atleast 3 characters required"
    MINIMUM_LENGTH_4 = "Atleast 4 characters required"
    MINIMUM_LENGTH_10 = "Atleast 10 characters required"

    REQUIRED_INVALID_DATA = "Invalid data"
    REQUIRED_VALID_DATA = "This field is required."

    INVALID_DATE_FORMAT = "Please enter a valid date in format (YYYY-MM-DD)"
    INVALID_EMAIL_ID = "Please enter a valid email id"
    INVALID_PHONE_NUMBER = "Please enter a valid phone number"


class ErrorFields:
    DATE_FIELDS = ["monthly_reporting_next_period",
                   "monthly_reporting_current_period",
                   "chartofaccounts_last_refresh_date",
                   "trialbalance_last_refresh_date",
                   "current_fiscal_year_end"]

    PHONE_FIELDS = [
        "phone"
    ]
