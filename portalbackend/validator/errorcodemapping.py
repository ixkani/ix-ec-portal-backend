class ErrorCode:
    # Common
    UNAUTHORIZED_ACCESS = 1000
    VALIDATION_ERROR = 1001
    MISSING_PARAMETERS = 1002
    INVALID_PARAMETERS = 1003
    DATA_PARSING_ISSUE = 1004
    MONTHLY_REPORT_NOT_FOUND = 1005
    DATA_NOT_FOUND = 1006
    INTERNAL_SERVER_ERROR = 1007
    OBJECT_RESOURCE_NOT_FOUND = 1008
    NO_DATA_CHANGES = 1009
    DELETED_SUCCESSFULLY = 1010
    RESOURCE_NOT_FOUND = 1011
    MULTIPLE_EMAIL_FOUND = 1012
    EMAIL_NOT_FOUND = 1013
    USER_NOT_CONNECTED = 1014


    # Reports
    MISSING_MONTHLY_REPORTING_CURRENT_PERIOD = 1100
    MONTHLY_REPORT_ALREADY_EXISTS_WITH_INPROGRESS = 1101
    MONTHLY_REPORT_ALREADY_EXISTS_WITH_COMPLETED = 1102
    INVALID_FILE_FORMAT = 1103
    ALL_SIGHT_CONNECTION = 1104
    MISSING_MONTHLY_REPORTING_PREVIOUS_PERIOD = 1105
    INVALID_COA_CSV = 1106
    INVALID_TB_CSV = 1107
    INVALID_TB_DATE = 1108

    #sessions
    SESSION_EXPRIED = 1200
    SESSION_ALREADY_ACTIVE = 1201


    # Company Error Messages
    COMPANY_META_NOT_AVAILABLE = 1300

