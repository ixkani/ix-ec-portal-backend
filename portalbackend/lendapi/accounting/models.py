from django.db import models
from oauth2_provider.models import RefreshToken
from portalbackend.lendapi.accounts.models import Company
from django.core.validators import RegexValidator, MinValueValidator, MinLengthValidator,DecimalValidator
from django.apps import apps

from portalbackend.validator.errormapping import ErrorMessage,UIErrorMessage

# from django.utils import timezone


# Create your models here.

# todo: add last_update_date and created_date to ALL models set auto_now and auto_now_added=True
class Bearer:
    """
    The bearer token response for qbo response, in memory instance, not db persistent
    """
    def __init__(self, refreshExpiry, accessToken, tokenType, refreshToken, accessTokenExpiry, idToken=None):
        self.refreshExpiry = refreshExpiry
        self.accessToken = accessToken
        self.tokenType = tokenType
        self.refreshToken = refreshToken
        self.accessTokenExpiry = accessTokenExpiry
        self.idToken = idToken


class AccountingOauth2(models.Model):
    """
     Token that each company has relating to their Quickbooks Login, or any other system that it might use
     """
    accessToken = models.CharField(max_length=1000, unique=True)
    refreshToken = models.CharField(max_length=255, blank=True, null=True)
    realmId = models.CharField(max_length=255, blank=True, null=True)
    accessSecretKey = models.CharField(max_length=255, blank=True, null=True)
    tokenAcitvatedOn = models.CharField(max_length=255, blank=True, null=True)
    tokenExpiryON = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company)

    class Meta:
        db_table = "accountingoauth2"


class TrialBalance(models.Model):
    """
    Trial balance object from company's accounting system
    """
    gl_account_name = models.CharField(max_length=150)
    # gl_account_id change made changed Integer field to char field
    gl_account_id = models.CharField(max_length=10,blank=True, null=True)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.ForeignKey(Company)
    period = models.DateField(default=None)
    currency = models.CharField(max_length=3, blank=True)

    def __str__(self):
        return self.period.strftime("%Y-%m")

    class Meta:
        db_table = 'trialbalance'
        verbose_name = 'Trial Balance'
        verbose_name_plural = 'Trial Balances'


class CoAMap(models.Model):
    """
    Mapping of Chart of Accounts from their account id to espresso account id's and names,
    """
    company = models.ForeignKey(Company)
    # gl_account_id change made changed cust_account_id to charfield
    cust_account_id = models.CharField(max_length=10,blank=True, null=True)
    cust_account_name = models.CharField(max_length=60, blank=True,validators=[
        MinLengthValidator(3, message=UIErrorMessage.MINIMUM_LENGTH_3)])
    espresso_account_id = models.IntegerField()
    espresso_account_name = models.CharField(max_length=60, blank=True,validators=[
        MinLengthValidator(3, message=UIErrorMessage.MINIMUM_LENGTH_3)])
    is_mapped = models.BooleanField(default=False)
    verified_by_user = models.BooleanField(default=False)

    class Meta:
        db_table = 'coamap'
        verbose_name = 'Chart of Accounts Map'


class CoA(models.Model):
    """
    Chart of Accounts for company
    """
    company = models.ForeignKey(Company)
    # gl_account_id change made
    gl_account_id = models.CharField(max_length=10,null=True, blank=True)
    gl_account_name = models.CharField(max_length=60, verbose_name="Account Name",validators=[
        MinLengthValidator(3, message=UIErrorMessage.MINIMUM_LENGTH_3)])
    gl_account_type = models.CharField(max_length=60, verbose_name="Account Type",validators=[
        MinLengthValidator(3, message=UIErrorMessage.MINIMUM_LENGTH_3)])
    gl_account_bal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Account Balance",
                                         blank=True, null=True)
    gl_account_currency = models.CharField(max_length=3, verbose_name="Account Currency",validators=[
        MinLengthValidator(3, message=UIErrorMessage.MINIMUM_LENGTH_3)])

    class Meta:
        db_table = 'coa'
        verbose_name = 'Chart of Accounts'
        verbose_name_plural = 'Chart of Accounts'


class DefaultAccountTagMapping(models.Model):
    """
    The default mappings that the COAMAP Resorts to, is then changes when user submits
    """
    software = models.CharField(max_length=60, choices=Company.ACCOUNTING_CHOICES)
    account_category = models.CharField(max_length=60)
    default_map_id = models.IntegerField()
    default_map_name = models.CharField(max_length=60)
    # tag_category = models.CharField(max_length=60)

    class Meta:
        db_table = 'defaultaccounttagmapping'
        verbose_name = 'Account Tag Mapping'

class FinancialStatementEntryTag(models.Model):
    """
    List of Tags that the companys have for coamap options
    """
    tag_id = models.IntegerField(null=True)
    generated_id = models.CharField(max_length=65, null=True, blank=True)

    name = models.CharField(max_length=128, null=True)
    short_label = models.CharField(max_length=60)
    description = models.CharField(max_length=120, blank=True)
    tag_category = models.CharField(max_length=60)
    abstract = models.BooleanField(default=False)
    formula = models.CharField(max_length=120, blank=True, null=True)
    sort_order = models.IntegerField(null=True)
    tag_group = models.CharField(max_length=120, blank=True, null=True)
    is_total_row = models.BooleanField(default=False)
    # todo: this is temporary until AS supports account id values, remove in phase 4
    all_sight_name = models.CharField(max_length=60, null=True)

    def __str__(self):
        return self.short_label

    class Meta:
        db_table = 'financialstatementtag'
        verbose_name = 'Financial Statement Entry Tag'


class LoginInfo(models.Model):
    """
    Login task status of quickbooks, in case user decides to close it? who knows
    """
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    FAILED = "Failed"
    STATUS_CHOICES = (
        (IN_PROGRESS, "In Progress"),
        (COMPLETED, "Completed"),
        (FAILED, "Failed")
    )

    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    created = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey(Company)
