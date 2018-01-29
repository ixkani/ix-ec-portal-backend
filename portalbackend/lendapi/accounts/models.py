from django import forms
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinValueValidator, MinLengthValidator
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from model_utils import FieldTracker
from oauth2_provider.models import AccessToken

from portalbackend.validator.errormapping import UIErrorMessage
from django.db.models import Q

from django.conf import settings
from django.contrib.sessions.models import Session

class Company(models.Model):
    QUICKBOOKS = "Quickbooks"
    XERO = "Xero"
    SAGE = "Sage"

    ACCOUNTING_CHOICES = (
        (QUICKBOOKS, "Quickbooks"),
        (XERO, "Xero"),
        (SAGE, "Sage")
    )

    name = models.CharField(max_length=100, validators=[
        MinLengthValidator(3, message=UIErrorMessage.MINIMUM_LENGTH_3),
        RegexValidator("^([(\[]|[a-zA-Z0-9_\s]|[\"-\.'#&!]|[)\]])+$")

    ])
    external_id = models.CharField(max_length=150, validators=[
        MinLengthValidator(3, message=UIErrorMessage.MINIMUM_LENGTH_3)
    ])
    parent_company = models.ForeignKey('self', null=True, blank=True)
    default_currency = models.CharField(max_length=3, validators=[
        MinLengthValidator(3, message=UIErrorMessage.MINIMUM_LENGTH_3)
    ])
    # todo: this forces the field to contain http / https which is a pain for the user. Need to validate URL without
    website = models.CharField(max_length=200, validators=[
        MinLengthValidator(4, message=UIErrorMessage.MINIMUM_LENGTH_4),
        RegexValidator(
            "^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$",
            message=UIErrorMessage.REQUIRED_INVALID_DATA)
    ])
    employee_count = models.IntegerField(null=True, default=0,
                                         validators=[MinValueValidator(0)])
    accounting_type = models.CharField(max_length=60, choices=ACCOUNTING_CHOICES, default=QUICKBOOKS)
    auth_key = models.CharField(max_length=500, default="", validators=[
        MinLengthValidator(10, message=UIErrorMessage.MINIMUM_LENGTH_10)
    ])
    secret_key = models.CharField(max_length=500, default="", validators=[
        MinLengthValidator(10, message=UIErrorMessage.MINIMUM_LENGTH_10)
    ])
    current_fiscal_year_end = models.DateField(null=True, blank=True)
    is_tag_error_notified = models.BooleanField(default=False,blank=True,help_text="No Need to Change. Auto Updation Field")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "company"


@receiver(post_save, sender=Company)
def company_created(sender, instance, created, *args, **kwargs):
    """
    Creates blank company metadata object upon company creation
    :param sender:
    :param instance:
    :param created:
    :param args:
    :param kwargs:
    :return:
    """
    if created:
        if not CompanyMeta.objects.filter(company=instance):
            CompanyMeta.objects.create(company=instance)


class User(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    external_id = models.CharField(max_length=150, blank=True, validators=[
        MinLengthValidator(3, message=UIErrorMessage.MINIMUM_LENGTH_3)])
    role = models.CharField(max_length=100, blank=True, validators=[
        MinLengthValidator(3, message=UIErrorMessage.MINIMUM_LENGTH_3)])
    # last_login_time = models.DateField(blank=True, null=True)
    is_session_active = models.BooleanField(default=False)

    class Meta:
        db_table = "user"


class ForgotPasswordRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    email = models.CharField(max_length=100, validators=[
        RegexValidator("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                       message=UIErrorMessage.REQUIRED_INVALID_DATA)])
    token = models.CharField(max_length=100, blank=True, null=True)
    request_time = models.DateTimeField(blank=True, null=True)
    expiry_time = models.IntegerField(default=0, null=True)
    is_expired = models.BooleanField(default=False)

    class Meta:
        db_table = "forgot_password_request"


class Contact(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message=UIErrorMessage.INVALID_PHONE_NUMBER)
    company = models.ForeignKey(Company)
    external_id = models.CharField(max_length=150, validators=[
        MinLengthValidator(3, message=UIErrorMessage.MINIMUM_LENGTH_3)])
    title = models.CharField(max_length=50, blank=True, validators=[
        MinLengthValidator(3, message=UIErrorMessage.MINIMUM_LENGTH_3)])
    phone = models.CharField(max_length=15, validators=[phone_regex], blank=True, )
    first_name = models.CharField(max_length=100, validators=[
        MinLengthValidator(3, message=UIErrorMessage.MINIMUM_LENGTH_3),
        RegexValidator("^([(\[]|[a-zA-Z0-9_\s]|[\"-\.'#&!]|[)\]])+$")])
    last_name = models.CharField(max_length=100, validators=[
        MinLengthValidator(3, message=UIErrorMessage.MINIMUM_LENGTH_3),
        RegexValidator("^([(\[]|[a-zA-Z0-9_\s]|[\"-\.'#&!]|[)\]])+$")])
    email = models.CharField(max_length=100, validators=[
        RegexValidator("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                       message=UIErrorMessage.INVALID_EMAIL_ID)])

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        db_table = "contact"


class CompanyMeta(models.Model):
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETE = "COMPLETE"

    ACCOUNTING_STEPS = (
        (NOT_STARTED, "NOT_STARTED"),
        (IN_PROGRESS, "IN_PROGRESS"),
        (COMPLETE, "COMPLETE")
    )

    company = models.ForeignKey(Company)
    monthly_reporting_sync_method = models.CharField(max_length=50, null=True, blank=True, validators=[
        MinLengthValidator(3, message=UIErrorMessage.MINIMUM_LENGTH_3)
    ])
    monthly_reporting_current_period = models.DateField(null=True, blank=True)
    monthly_reporting_next_period = models.DateField(null=True, blank=True)

    monthly_reporting_current_period_status = models.CharField(max_length=20, null=True, blank=True, validators=[
        MinLengthValidator(3, message=UIErrorMessage.MINIMUM_LENGTH_3)])
    last_page = models.CharField(max_length=200, null=True, blank=True, validators=[
        MinLengthValidator(3, message=UIErrorMessage.MINIMUM_LENGTH_3)
    ])

    qb_connect_desktop_version = models.CharField(max_length=5, null=True, blank=True, validators=[
        MinLengthValidator(3, message=UIErrorMessage.MINIMUM_LENGTH_3)
    ])

    # todo: I don't think this is being used, remove if possible
    monthly_reporting_last_step = models.IntegerField(null=True, blank=True,
                                                      validators=[MinValueValidator(0)])

    # todo: rename this to setup_status so that it applies for Manual Form Entry type as well.
    accounting_setup_status = models.CharField(max_length=20, null=True, blank=True,
                                               default=NOT_STARTED, choices=ACCOUNTING_STEPS)

    qb_desktop_installed = models.BooleanField(default=False)

    is_initial_setup = models.BooleanField(default=True)
    setup_completed = models.BooleanField(default=False)
    initial_tracker = FieldTracker(fields=['is_initial_setup'])
    # this is a flag used by the UI to control the timing of API calls to All Sight
    trialbalance_dl_complete = models.BooleanField(default=False)

    chartofaccounts_last_refresh_date = models.DateField(null=True, blank=True)
    trialbalance_last_refresh_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "companymeta"


# this function can probably be phased out. Need to assess and decide. #brad #todo
@receiver(post_save, sender=CompanyMeta)
def changed_tracker(sender, instance, **kwargs):
    """
    Sets initial setup to false, only allows once
    """
    if 'is_initial_setup' in instance.initial_tracker.changed() and not instance.setup_completed:
        if instance.initial_tracker.changed()['is_initial_setup'] is True and instance.is_initial_setup is False:
            instance.setup_completed = True
            instance.save()

            # todo: at this point we've decided to keep the monthly report data that is collected during the
            # setup period because it is valid data from a closed month, but verify with Jim.

            # This cleans up any entries into the Financial Statement Entry table that were created during setup
            # because setup is always done before their first actul reporting.

            # todo: if this is re-enabled, we need to add an if that will avoid doing this for manual form entry users
            # because there is effectively no setup process so they'll setup and report for the first time in the same
            # session
            # entries = apps.get_model('reporting', 'FinancialStatementEntry')
            # entries.objects.filter(company=instance.company).delete()


class CompanyNotification(models.Model):
    company = models.ForeignKey(Company)
    for_user_only = models.BooleanField(default=False)
    date_created = models.DateField()
    date_read = models.DateField()
    is_read = models.BooleanField(default=False)
    message = models.TextField()

    class Meta:
        db_table = "companynotification"


class EspressoContact(models.Model):
    company = models.ForeignKey(Company)
    # To list contacts only from Espresso Company
    contact = models.ForeignKey(Contact,limit_choices_to=Q(company=settings.ESPRESSO_COMAPANY_ID))

    class Meta:
        db_table = "espressocontact"

@receiver(post_save,sender=CompanyMeta)
def remove_meta(sender, instance, **kwargs):
    company = instance.company
    if CompanyMeta.objects.filter(company=company).count() > 1 :
        c = CompanyMeta.objects.filter(company=company).first()
        c.delete()

class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    auth_key = models.ForeignKey(AccessToken,null=True)
    start_time = models.DateTimeField(default=None)
    end_time = models.DateTimeField(default=None)
    is_first_time = models.BooleanField(default=True)

class FiscalYearEnd(models.Model):
    # TODO : CHECK THIS OUT - is_active is neccesary if not found first data will be loaded
    company = models.ForeignKey(Company)
    fye_start_date = models.DateField()
    fye_end_date = models.DateField()
    label = models.CharField(max_length=60)
    last_update_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
