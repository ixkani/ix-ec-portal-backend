from portalbackend.settings import RUN_UNIT_TEST
from tests.accounts.testcases.tc_change_password import _001_EmailValidationTestCase, _002_ForgotPasswordTestCase, \
    _003_ChangePasswordTestCase
from tests.accounts.testcases.tc_company import _001_CompanyListTestCase, _002_CompanyDetailsTestCase, \
    _003_CompanyMetaDetailsTestCase
from tests.accounts.testcases.tc_contact import _001_ContactDetailsTestCase
from tests.accounts.testcases.tc_espresso_contact import _001_EspressoContactsTestCase
from tests.accounts.testcases.tc_forms import AccountsFormTest
from tests.accounts.testcases.tc_login_logout import _001_LoginViewTestCase, _002_LogoutTestCase
from tests.accounts.testcases.tc_sceduled_maintaince import _001_ScheduledMaintenanceDetailsTestCase
from tests.accounts.testcases.tc_two_factor import _001_TwoFactorAuthenticationDetailsTestCase
from tests.accounts.testcases.tc_user import _001_UserListTestCase, _002_MeTestCase, _003_UserDetailsTestCase

if RUN_UNIT_TEST:

    # @unittest - Tests User List api calls
    tc_user_list_view = _001_UserListTestCase

    # @unittest - Tests Me api calls
    tc_user_me_view = _002_MeTestCase

    # @unittest - Tests User Details api calls
    tc_user_detail_view = _003_UserDetailsTestCase

    # @unittest - Tests Company List api calls
    tc_company_list_view = _001_CompanyListTestCase

    # @unittest - Tests Company Details api calls
    tc_company_details_view = _002_CompanyDetailsTestCase

    # @unittest - Tests Company Meta api calls
    tc_company_meta_view = _003_CompanyMetaDetailsTestCase

    # @unittest - Tests Contact Details api calls
    tc_contact_view = _001_ContactDetailsTestCase

    # @unittest - Tests Espresso Contact api calls
    tc_espresso_contact_view = _001_EspressoContactsTestCase

    # @unittest - Tests Email validation api calls
    tc_email_validation_view = _001_EmailValidationTestCase

    # @unittest - Tests Forgot password api calls
    tc_forgot_password_view = _002_ForgotPasswordTestCase

    # @unittest - Tests Change password api calls
    tc_change_password_view = _003_ChangePasswordTestCase

    # @unittest - Tests Scheduled Maintenance Details api calls
    tc_sceduled_maintaince_view = _001_ScheduledMaintenanceDetailsTestCase

    # @unittest - Tests Two Factor Authentication api calls
    tc_two_factor_view = _001_TwoFactorAuthenticationDetailsTestCase

    # @unittest - Tests Login api calls
    tc_login_view = _001_LoginViewTestCase

    # @unittest - Tests Logout api calls
    tc_logout_view = _002_LogoutTestCase

    # @unittest - Tests Two Factor Authentication api calls
    form_test = AccountsFormTest
