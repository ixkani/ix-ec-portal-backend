if False:

    from tests.accounts.testcases import tc_user, tc_company, tc_contact, tc_espresso_contact, tc_change_password, \
        tc_sceduled_maintaince, tc_two_factor, tc_login_logout, tc_forms

    # @unittest - Tests User List api calls
    tc_user_list_view = tc_user._001_UserListTestCase

    # @unittest - Tests Me api calls
    tc_user_me_view = tc_user._002_MeTestCase

    # @unittest - Tests User Details api calls
    tc_user_detail_view = tc_user._003_UserDetailsTestCase

    # @unittest - Tests Company List api calls
    tc_company_list_view = tc_company._001_CompanyListTestCase

    # @unittest - Tests Company Details api calls
    tc_company_details_view = tc_company._002_CompanyDetailsTestCase

    # @unittest - Tests Company Meta api calls
    tc_company_meta_view = tc_company._003_CompanyMetaDetailsTestCase

    # @unittest - Tests Contact Details api calls
    tc_contact_view = tc_contact._001_ContactDetailsTestCase

    # @unittest - Tests Espresso Contact api calls
    tc_espresso_contact_view = tc_espresso_contact._001_EspressoContactsTestCase

    # @unittest - Tests Email validation api calls
    tc_email_validation_view = tc_change_password._001_EmailValidationTestCase

    # @unittest - Tests Forgot password api calls
    tc_forgot_password_view = tc_change_password._002_ForgotPasswordTestCase

    # @unittest - Tests Change password api calls
    tc_change_password_view = tc_change_password._003_ChangePasswordTestCase

    # @unittest - Tests Scheduled Maintenance Details api calls
    tc_sceduled_maintaince_view = tc_sceduled_maintaince._001_ScheduledMaintenanceDetailsTestCase

    # @unittest - Tests Two Factor Authentication api calls
    tc_two_factor_view = tc_two_factor._001_TwoFactorAuthenticationDetailsTestCase

    # @unittest - Tests Login api calls
    tc_login_view = tc_login_logout._001_LoginViewTestCase

    # @unittest - Tests Logout api calls
    tc_logout_view = tc_login_logout._002_LogoutTestCase

    # @unittest - Tests Two Factor Authentication api calls
    form_test = tc_forms.AccountsFormTest
