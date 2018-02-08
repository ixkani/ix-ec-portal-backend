from django.contrib import admin
from django import forms
from django.contrib.sessions.models import Session
from .models import Company, User, CompanyMeta, EspressoContact, Contact, ForgotPasswordRequest,UserSession,FiscalYearEnd, CompanyAccountingConfiguration
from portalbackend.lendapi.reporting.models import MonthlyReport

from django.contrib.auth.admin import UserAdmin
from django.db import models
from .forms import CompanyMetaForm, CompanyForm, ContactForm, EcUserChangeForm, EcUserCreationForm,FiscalYearEndForm,CompanyAccountingConfigurationForm
from portalbackend.lendapi.v1.accounts.serializers import CompanySerializer, UserSerializer, CompanyMetaSerializer, \
    UserLoginSerializer, LoginSerializer, CreateUserSerializer, ContactSerializer, EspressoContactSerializer

class CompanyUserInline(admin.TabularInline):
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'external_id')
    show_change_link = True
    extra = 0


class CompanyMetaInline(admin.StackedInline):
    model = CompanyMeta
    form = CompanyMetaForm
    extra = 0
    fields = [field.name for field in CompanyMeta._meta.fields]
    max_num = 1

class CompanyAccountingConfigurationInline(admin.StackedInline):
    model = CompanyAccountingConfiguration
    form = CompanyAccountingConfigurationForm
    extra = 2
    show_change_link = True
    fields = [field.name for field in CompanyAccountingConfiguration._meta.fields]
    max_num = 1


class CompanyMonthlyReportInline(admin.TabularInline):
    show_change_link = True
    model = MonthlyReport
    extra = 0
    fields = [field.name for field in MonthlyReport._meta.fields] #if field.name != 'lookup_period']
    readonly_fields = ('lookup_period', )

class CompanyContactInline(admin.TabularInline):
    model = EspressoContact
    extra = 0





class CompanyAdmin(admin.ModelAdmin):
    form = CompanyForm
    # list_display = [field.name for field in Company._meta.fields]
    list_display = ('id', 'name', 'external_id', 'parent_company', 'default_currency', 'website', 'employee_count',
                    'accounting_type', 'current_fiscal_year_end')
    inlines = (CompanyAccountingConfigurationInline,CompanyUserInline, CompanyMetaInline, CompanyMonthlyReportInline, CompanyContactInline)

admin.site.register(Company, CompanyAdmin)



class EcUserAdmin(UserAdmin):
    add_form = EcUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password1', 'password2')}
         ),
    )
    form = EcUserChangeForm
    list_display = ('username', 'company', 'email','user_type')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('external_id', 'company')}),
    )
    """
    set the type of users and display to user list
    """
    def user_type(self,obj):
        type = "Company"
        if obj.is_staff:
            type = "Admin"
        return type
    """
    Custome field search 
    """
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super (EcUserAdmin, self).get_search_results (request, queryset, search_term)
        if search_term.lower() in "admin":
            queryset |= self.model.objects.filter (is_staff=True)
        elif search_term.lower() in "company":
            queryset |= self.model.objects.filter (is_staff=False)

        return queryset, use_distinct

admin.site.register(User, EcUserAdmin)


class ContactAdmin(admin.ModelAdmin):
    form = ContactForm
    list_display = [field.name for field in Contact._meta.fields]

admin.site.register(Contact, ContactAdmin)



# class EspressoContactAdmin(admin.ModelAdmin):
#     form = EspressoContactForm
#     list_display = ('company', 'available_contacts',)
#
#     def available_contacts(self, obj):
#          return obj.contact.first_name + ' ' + obj.contact.last_name

# admin.site.register(EspressoContact,EspressoContactAdmin)


class FiscalYearEndAdmin(admin.ModelAdmin):
    form = FiscalYearEndForm
    list_display = [field.name for field in FiscalYearEnd._meta.fields]

admin.site.register(FiscalYearEnd,FiscalYearEndAdmin)
