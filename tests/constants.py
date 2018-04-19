class TestConstants:

    HOST_URL = 'espresso-ix-backend.herokuapp.com'
    SECURE_CONNECTION = True






    INVALID_ID = 100
    INVALID_STRING = "DUMMY"
    INVALID_USERNAME = "dummmy_username"
    INVALID_PASSWORD = "dummmy_password"
    INVALID_EMAIL = "dummmy_email"
    INVALID_TOKEN = "dummmytoken"
    INVALID_TOTP = "1234567"


class UserConstant:
    ADMIN_USERNAME = 'ut_admin'
    ADMIN_PASSWORD = 'Espresso@1'
    ADMIN_EMAIL = 'ut_admin@unittesting.com'

    USER_PASSWORD = 'Espresso@1'
    USER_EMAIL = 'ut_user@unittesting.com'


class CompanyConstant:

    DEFAULT_COMPANY_EMPLOYEE_COUNT = 10
    DEFAULT_COMPANY_EXTERNALID = 'UT00A'
    DEFAULT_COMPANY_WEBSITE = 'espressocapital.com'

    COMPANY_NAME_001 = 'UTCompany001'

    COMPANY_CURRENT_REPORT_PERIOD = '2016-10-31'
    COMPANY_NEXT_REPORT_PERIOD = '2016-11-30'

class ContactConstant:

    DEFAULT_CONTACT_FIRST_NAME = "TEST"
    DEFAULT_CONTACT_LAST_NAME = "CONTACT"
    DEFAULT_CONTACT_TITLE = "TEST COMPANY CONTACT"
    DEFAULT_CONTACT_EMAIL = "testcontact@espressocapital.com"
    DEFAULT_CONTACT_EXTERNALID = 'UTC001'



class ResponseCodeConstant:
    SUCCESS_200 = 200
    FAILURE_400 = 400
    UNAUTHORIZED_ACCESS_401 = 401
    RESOURCE_NOT_FOUND_404 = 404
    INTERNAL_SERVER_ERROR = 500
