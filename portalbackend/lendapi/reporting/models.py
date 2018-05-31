from django.db import models
from portalbackend.lendapi.accounts.models import Company,User
from portalbackend.lendapi.accounting.models import FinancialStatementEntryTag
from django.contrib.postgres.fields import ArrayField
from django.core.validators import RegexValidator, MinValueValidator, MinLengthValidator
from django.apps import apps
from django.core.validators import RegexValidator
from portalbackend.validator.errormapping import ErrorMessage,UIErrorMessage
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class MonthlyReport(models.Model):
    """
    The monthly report Data Object
    """
    DUE = "Due"
    IN_PROGRESS = "In Progress"
    COMPLETE = "Complete"
    OVERDUE = "Over Due"
    STATUS_CHOICES = (
        (DUE, 'Due'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETE, 'Complete'),
        (OVERDUE, "Over Due")
    )

    company = models.ForeignKey(Company)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES)
    period_ending = models.DateField()
    due_date = models.DateField(blank=True, null=True)
    submitted_on = models.DateField(blank=True, null=True)
    lookup_period = models.CharField(max_length=8, blank=True, null=True)
    signoff_by_name = models.CharField(max_length=100, null=True, blank=True,validators=[
        RegexValidator("^([(\[]|[a-zA-Z0-9_\s]|[[\\\/\"-\.'#&!]|[)\]])+$")])
    signoff_by_title = models.CharField(max_length=100, null=True, blank=True,validators=[
        RegexValidator("^([(\[]|[a-zA-Z0-9_\s]|[[\\\/\"-\.'#&!]|[)\]])+$")])
    signoff_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.lookup_period = self.period_ending.strftime("%Y-%m")
        print(self)
        return super(MonthlyReport, self).save(*args, **kwargs)

    def __str__(self):
        return 'Period ' + self.lookup_period

    class Meta:
        db_table = "monthlyreport"
        indexes = [
            models.Index(fields=['company', 'period_ending',])
        ]


# todo: why is this here and not in the accounting models?... needs to be moved
class FinancialStatementEntry(models.Model):
    INCOME_STATEMENT = "Income Statement"
    BALANCE_SHEET = "Balance Sheet"
    CASH_FLOW = "Cash Flow"
    STATEMENT_CHOICES = (
        (INCOME_STATEMENT, "Income Statement"),
        (BALANCE_SHEET, "Balance Sheet"),
        (CASH_FLOW, "Cash Flow")
    )

    company = models.ForeignKey(Company)
    monthly_report = models.ForeignKey(MonthlyReport, null=True, blank=True)
    fse_tag = models.ForeignKey(FinancialStatementEntryTag, null=True, blank=True)
    entry_name = models.CharField(max_length=60, null=True)
    period_ending = models.DateField()
    value = models.DecimalField(max_digits=15, decimal_places=0)
    currency = models.CharField(max_length=3)
    statement_type = models.CharField(max_length=60, choices=STATEMENT_CHOICES, default=INCOME_STATEMENT)
    is_actual = models.BooleanField(default=True)
    period_type = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "financialstatemententry"
        # ordering = ('fse_tag__sort_order',)
        indexes = [
             models.Index (fields=['company', 'statement_type','fse_tag']),
             models.Index (fields=['company', 'period_ending','statement_type','fse_tag',]),
         ]

    def __str__(self):
        return self.fse_tag.short_label

class QuestionCategory(models.Model):
    group_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=False)
    purpose = models.TextField()

    def __str__(self):
        return self.group_name

    class Meta:
        db_table = "questioncategory"
        indexes = [
            models.Index(fields=['group_name', ])
        ]

class Question(models.Model):
    company = models.ForeignKey(Company)
    next_question = models.ForeignKey('self', blank=True, null=True)
    next_question_if = models.CharField(max_length=20, blank=True, null=True,validators=[
        MinLengthValidator(10, message=UIErrorMessage.MINIMUM_LENGTH_10)])

    question_category = models.ForeignKey(QuestionCategory)
    question_text = models.TextField(validators=[
        MinLengthValidator(10, message=UIErrorMessage.MINIMUM_LENGTH_10)])

    # todo: don't use arrayfields, they are not not compatible with many other databases. This should be changed to just
    #       char field eventually.
    question_choices = ArrayField(models.CharField(max_length=100, blank=True, null=True), null=True,
                                  blank=True, default=list)

    short_tag = models.CharField(max_length=100,validators=[
        MinLengthValidator(3, message=UIErrorMessage.MINIMUM_LENGTH_3)])
    answer_data_type = models.CharField(max_length=100,validators=[
        MinLengthValidator(3, message=UIErrorMessage.MINIMUM_LENGTH_3)])
    answer_validation_regex = models.CharField(max_length=254, blank=True)
    ask_order = models.IntegerField()
    show_on_ui = models.BooleanField(default=False)
    common_to_all_companies = models.BooleanField(default=False)

    class Meta:
        db_table = "question"
        indexes = [
            models.Index(fields=['common_to_all_companies','show_on_ui','company',])
        ]

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question)
    monthly_report = models.ForeignKey(MonthlyReport)
    company = models.ForeignKey(Company)
    answer = models.TextField(null=True,blank=True)

    def __str__(self):
        return "{} , {} , {}" \
            .format(self.company, self.monthly_report,self.answer)

    class Meta:
        db_table = "answer"
        indexes = [
            models.Index(fields=['company', 'monthly_report', 'question'])
        ]


class Download(models.Model):
    name = models.CharField(max_length=60, null=True)
    link = models.CharField(max_length=300, null=True)
    version = models.DecimalField(max_digits=4, decimal_places=2)

class PreviousReportEditLogger(models.Model):
    INCOME_STATEMENT = "Income Statement"
    BALANCE_SHEET = "Balance Sheet"
    ANSWER = "Answer"
    SECTION_CHOICES = (
        (INCOME_STATEMENT, "Income Statement"),
        (BALANCE_SHEET, "Balance Sheet"),
        (ANSWER, "Answer")
    )
    company = models.ForeignKey(Company)
    user = models.ForeignKey(User)
    reporting_period = models.ForeignKey(MonthlyReport)
    section_name = models.CharField(max_length=60, choices=SECTION_CHOICES,verbose_name="Section Name")
    finacial_statement_item = models.ForeignKey(FinancialStatementEntry,null=True,verbose_name="Changed Financial Tag")
    question_item = models.ForeignKey(Question,null=True,verbose_name="Changed Question")
    old_value = models.CharField(max_length=512,null=True,verbose_name="Old Value")
    new_value = models.CharField(max_length=512,null=True,verbose_name="New Value")
    date_changed = models.DateTimeField()

