
from .models import Company, User, CompanyMeta, EspressoContact, Contact,FiscalYearEnd,AccountingConfiguration
from portalbackend.lendapi.accounting.models import AccountingOauth2
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.db import models
from portalbackend.validator.errormapping import ErrorMessage,UIErrorMessage

class EcUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Make sure valid email address.')
    class Media:
        js = ('./admin/js/admin-custom-actions.js',)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class EcUserChangeForm(UserChangeForm):
    class Media:
        js = ('./admin/js/admin-custom-actions.js',)
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(EcUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['company'].queryset = Company.objects.order_by('name')
        for field in self.fields.values():
            field.error_messages = {'required': UIErrorMessage.REQUIRED_VALID_DATA,'invalid':UIErrorMessage.REQUIRED_INVALID_DATA}


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required': UIErrorMessage.REQUIRED_VALID_DATA,'invalid':UIErrorMessage.REQUIRED_INVALID_DATA}


class CompanyMetaForm(forms.ModelForm):
    class Meta:
        model = CompanyMeta
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(CompanyMetaForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required': UIErrorMessage.REQUIRED_VALID_DATA}

            if ('date' or 'period' or 'year' in field.label):
                field.error_messages = {'invalid': UIErrorMessage.INVALID_DATE_FORMAT}

    def clean(self):
        current_date = self.cleaned_data.get('monthly_reporting_current_period')
        next_date = self.cleaned_data.get('monthly_reporting_next_period')

        if current_date is not None and next_date is not None:
            if current_date >= next_date:
                raise forms.ValidationError(
                    "Monthly reporting current period date should be less than Monthly reporting next period date")
        return self.cleaned_data


class AccountingConfigurationForm (forms.ModelForm):
    class Media:
        js = ('./admin/js/admin-custom-actions.js',)

    class Meta:
        model = AccountingConfiguration
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        if 'initial' not in kwargs:
            self.instance = kwargs.__getitem__('instance')
        super (AccountingConfigurationForm, self).__init__ (*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required': UIErrorMessage.REQUIRED_VALID_DATA}

    def clean(self):
        accounting_type = self.cleaned_data.get('accounting_type')
        if self.is_valid():
            if accounting_type != AccountingConfiguration.XERO:
                self.cleaned_data['type'] = None
            else:
                if self.cleaned_data['type'] == None:
                    raise forms.ValidationError("Xero Accounting Type not null")
            acc_objects = AccountingConfiguration.objects.filter(accounting_type = self.cleaned_data['accounting_type'])
            if self.cleaned_data['is_active']:
                for obj in acc_objects:
                    obj.is_active = False
                    obj.save()
            else:
                is_true = False
                for obj in acc_objects:
                    if obj.is_active and obj.id is not self.instance.id:
                        is_true = True
                if not is_true:
                    raise forms.ValidationError("Atleast one configuration year end should be active for {}".format(
                        self.cleaned_data['accounting_type']))

        return self.cleaned_data


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['company'].queryset = Company.objects.order_by('name')

        for field in self.fields.values():
            field.error_messages = {'required' : UIErrorMessage.REQUIRED_VALID_DATA}

class FiscalYearEndForm(forms.ModelForm):
    class Meta:
        model = FiscalYearEnd
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        if 'initial' not in kwargs:
            self.instance = kwargs.__getitem__('instance')
        super(FiscalYearEndForm, self).__init__(*args, **kwargs)
        self.fields['company'].queryset = Company.objects.order_by('name')

    def clean(self):

        start_date = self.cleaned_data.get('fye_start_date')
        end_date = self.cleaned_data.get('fye_end_date')

        if start_date is not None and end_date is not None:
            if start_date >= end_date:
                raise forms.ValidationError("Fye start date should be less than Fye end date")

        if self.is_valid():

            fs_objects = FiscalYearEnd.objects.filter(company=self.cleaned_data['company'])
            if self.cleaned_data['is_active']:
                for obj in fs_objects:
                    obj.is_active = False
                    obj.save()
            else:
                is_true = False
                for obj in fs_objects:
                    if obj.is_active and obj.id is not self.instance.id:
                        is_true = True
                if not is_true:
                    raise forms.ValidationError("Atleast one fiscal year end should be active")

        return self.cleaned_data