from django.contrib import admin
from django import forms
from django.contrib.sessions.models import Session
from django.utils import timezone

from .models import Company, User, CompanyMeta, EspressoContact, Contact, ForgotPasswordRequest,UserSession,FiscalYearEnd,AccountingConfiguration,ScheduledMaintenance,LoggedInUser
from portalbackend.lendapi.reporting.models import MonthlyReport

from oauth2_provider.models import AccessToken
from django.contrib.auth.admin import UserAdmin
from django.db import models
from .forms import CompanyMetaForm, CompanyForm, ContactForm, EcUserChangeForm, EcUserCreationForm,FiscalYearEndForm,AccountingConfigurationForm
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

class AccountingConfigurationInline(admin.StackedInline):
    model = AccountingConfiguration
    form = AccountingConfigurationForm
    extra = 2
    show_change_link = True
    fields = [field.name for field in AccountingConfiguration._meta.fields]
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
    inlines = (CompanyUserInline, CompanyMetaInline, CompanyMonthlyReportInline, CompanyContactInline)
    search_fields = ('name','accounting_type')
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
        (None, {'fields': ('external_id', 'company','is_password_reset','is_tfa_enabled','enforce_tfa_enabled','tfa_secret_code','is_tfa_setup_completed','tour_guide_enabled','last_login')}),

    )
    readonly_fields = ('tfa_secret_code',)
    """
    set the type of users and display to user list
    """
    def user_type(self,obj):
        type = "Company"
        if obj.is_staff:
            type = "Admin"
        return type
    """
    Custom field search 
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
    search_fields = ('company__name','email',)

class AccountingConfigurationAdmin(admin.ModelAdmin):
    form = AccountingConfigurationForm
    list_display = ['accounting_type','type','is_active']
    search_fields = ('accounting_type',)

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
    search_fields = ('company__name',)

class ScheduledMaintenanceAdmin(admin.ModelAdmin):
    list_display = ('message','start_time','end_time','is_active')
    list_editable = ('is_active',)
    # list_display_links = None
    actions = None

    def has_add_permission(self, request):
        return not ScheduledMaintenance.objects.exists()

class LoggedInUserAdmin(admin.ModelAdmin):
    list_display = ('user','company','login_time')
    actions = None
    list_display_links = None
    def company(self,obj):
        return obj.user.company

    def login_time(self,obj):
        return obj.user.last_login

    def has_add_permission(self, request):
        return False

    def get_queryset(self, request):
        for user in User.objects.all():
            exists = LoggedInUser.objects.filter(user=user).first()
            if user.is_logged_in and not exists:
                new_user = LoggedInUser(user=user)
                new_user.save()
            if not user.is_logged_in and exists:
                exists.delete()

            exists = LoggedInUser.objects.filter(user=user).first()


            session = UserSession.objects.filter(user=user).first()
            if session is not None and exists and timezone.now() > session.end_time:
                exists.delete()
                session.delete()
                user.is_logged_in = False
                user.save()
        return LoggedInUser.objects.exclude(user__is_staff=True)


admin.site.register(FiscalYearEnd,FiscalYearEndAdmin)
admin.site.register(AccountingConfiguration,AccountingConfigurationAdmin)
admin.site.register(ScheduledMaintenance,ScheduledMaintenanceAdmin)
admin.site.register(LoggedInUser,LoggedInUserAdmin)
admin.site.register(UserSession)