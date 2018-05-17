from django.test import TestCase
from portalbackend.lendapi.accounts import forms as accounts_forms
from portalbackend.lendapi.accounts.models import AccountingConfiguration, FiscalYearEnd
from tests.constants import CompanyConstant, UserConstant, TestConstants
from tests.utils import TestUtils


class AccountsFormTest(TestCase):
    def test_001_create_user_success(self):
        """
        Create user with valid data
        """
        form_data = {
            'username': 'utuser001',
            'email': UserConstant.USER_EMAIL,
            'password1': UserConstant.USER_PASSWORD,
            'password2': UserConstant.USER_PASSWORD
        }
        form = accounts_forms.EcUserCreationForm(data=form_data)
        self.assertEquals(form.is_valid(), True)

    def test_002_create_user_failure(self):
        """
        Create user invalid data failure
        """
        form_data = {
            'username': 'utuser001',
            'email': TestConstants.INVALID_EMAIL,
            'password1': UserConstant.USER_PASSWORD,
            'password2': UserConstant.USER_PASSWORD
        }
        form = accounts_forms.EcUserCreationForm(data=form_data)
        self.assertEquals(form.is_valid(), False)

    def test_003_change_user_failure(self):
        """
        Change user with invalid data
        """
        company = TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        form = accounts_forms.EcUserChangeForm()
        form.data['email'] = UserConstant.USER_EMAIL
        form.data['username'] = 'utuser001'
        form.data['password'] = UserConstant.USER_PASSWORD
        form.data['company'] = company
        self.assertEquals(form.is_valid(), False)

    def test_004_create_company_success(self):
        """
        Create Company with valid data
        """
        form_data = {
            "name": "Test Company",
            "external_id": "ABC123",
            "website": "https://en.wikipedia.org/wiki/Unit_testing",
            "employee_count": 1,
            "default_currency": "CAD",
            "accounting_type": "Quickbooks"
        }
        form = accounts_forms.CompanyForm(data=form_data)
        self.assertEquals(form.is_valid(), True)

    def test_005_create_company_failure(self):
        """
        Create Company with invalid data
        """
        form_data = {
            "name": "Test Company",
            "external_id": "ABC123",
            "website": TestConstants.INVALID_STRING,
            "employee_count": 1,
            "default_currency": TestConstants.INVALID_STRING,
        }
        form = accounts_forms.CompanyForm(data=form_data)
        self.assertEquals(form.is_valid(), False)

    def test_006_create_company_meta_sucess(self):
        """
        Create Company meta with valid data
        """
        company = TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        form_data = {
            "company": company.id,
            "monthly_reporting_sync_method": "Quickbooks Desktop",
            "monthly_reporting_current_period_status": "COMPLETE",
            "is_initial_setup": False,
            "trialbalance_dl_complete": True,
            "qb_desktop_installed": False,
        }
        form = accounts_forms.CompanyMetaForm(data=form_data)
        self.assertEquals(form.is_valid(), True)

    def test_007_create_company_meta_invalid(self):
        """
        Create Company meta with invalid data
        """
        company = TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        form_data = {
            "company": company.id,
            "monthly_reporting_current_period": "2018-12-31",
            "monthly_reporting_next_period": "2018-11-30",
        }
        form = accounts_forms.CompanyMetaForm(data=form_data)
        self.assertEquals(form.is_valid(), False)

    def test_008_create_accounting_configuration_success(self):
        """
        create accounting configuration with valid data and invalid scenarios
        """
        accounting_configuration1 = AccountingConfiguration(
            accounting_type=AccountingConfiguration.QUICKBOOKS,
            type=AccountingConfiguration.PUBLIC,
            client_id="Q0W1osEOriGM0rwlt7ZBE2ArpDAuczZyDxUmQyx6neVBbU4lkI",
            client_secret="RPHtn6oWjCsQuwYyi5j0Jh2M8hl93LsYk934pR81",
            is_active=True
        )

        accounting_configuration = AccountingConfiguration(
            accounting_type=AccountingConfiguration.QUICKBOOKS,
            type=AccountingConfiguration.PUBLIC,
            client_id="Q0W1osEOriGM0rwlt7ZBE2ArpDAuczZyDxUmQyx6neVBbU4lkI",
            client_secret="RPHtn6oWjCsQuwYyi5j0Jh2M8hl93LsYk934pR81",
            is_active=True
        )

        form_data = {
            "accounting_type": "Quickbooks",
            "client_id": "Q0W1osEOriGM0rwlt7ZBE2ArpDAuczZyDxUmQyx6neVBbU4lkI",
            "client_secret": "RPHtn6oWjCsQuwYyi5j0Jh2M8hl93LsYk934pR81",
            "is_active": True
        }

        kwargs = {
            "instance": accounting_configuration
        }

        form = accounts_forms.AccountingConfigurationForm(data=form_data, **kwargs)
        self.assertEquals(form.is_valid(), True)

        form_data["is_active"] = False
        form = accounts_forms.AccountingConfigurationForm(data=form_data, **kwargs)
        self.assertEquals(form.is_valid(), False)

        accounting_configuration1.save()
        form = accounts_forms.AccountingConfigurationForm(data=form_data, **kwargs)
        self.assertEquals(form.is_valid(), True)

        form_data["is_active"] = True
        form = accounts_forms.AccountingConfigurationForm(data=form_data, **kwargs)
        self.assertEquals(form.is_valid(), True)

        form_data["accounting_type"] = AccountingConfiguration.XERO
        form = accounts_forms.AccountingConfigurationForm(data=form_data, **kwargs)
        self.assertEquals(form.is_valid(), False)

    def test_009_create_contact_valid(self):
        """
        Create Contact with valid data
        """
        company = TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)
        form_data = {
            "title": "Espresso Employee",
            "last_name": "Employee",
            "email": "expressoemployee@exp.com",
            "first_name": "Expresso",
            "phone": "",
            "external_id": "EX0001",
            "company": company.id,
        }
        form = accounts_forms.ContactForm(data=form_data)
        self.assertEquals(form.is_valid(), True)

    def test_010_create_fiscal_year(self):
        """
        create fiscal year configuration with valid data and invalid scenarios
        """
        company = TestUtils._create_company(1, CompanyConstant.COMPANY_NAME_001)

        fiscalyearobject = FiscalYearEnd(
            company=company,
            fye_start_date="2018-01-01",
            fye_end_date="2018-12-31",
            label="This Year",
            is_active=True
        )

        fiscalyearobject1 = FiscalYearEnd(
            company=company,
            fye_start_date="2017-01-01",
            fye_end_date="2017-12-31",
            label="Last Year",
            is_active=True
        )

        form_data = {
            "company": company.id,
            "fye_start_date": "2018-01-01",
            "fye_end_date": "2018-12-31",
            "label": "This Year",
            "is_active": True
        }

        kwargs = {
            "instance": fiscalyearobject
        }

        form = accounts_forms.FiscalYearEndForm(data=form_data, **kwargs)
        self.assertEquals(form.is_valid(), True)

        form_data["is_active"] = False
        form = accounts_forms.FiscalYearEndForm(data=form_data, **kwargs)
        self.assertEquals(form.is_valid(), False)

        fiscalyearobject1.save()
        form = accounts_forms.FiscalYearEndForm(data=form_data, **kwargs)
        self.assertEquals(form.is_valid(), True)

        form_data["is_active"] = True
        form = accounts_forms.FiscalYearEndForm(data=form_data, **kwargs)
        self.assertEquals(form.is_valid(), True)

        form_data["fye_start_date"] = "2019-01-01"
        form = accounts_forms.FiscalYearEndForm(data=form_data, **kwargs)
        self.assertEquals(form.is_valid(), False)
