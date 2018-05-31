from django.contrib import admin
from django import forms
from .models import MonthlyReport, QuestionCategory, Question, Answer, FinancialStatementEntry,PreviousReportEditLogger

from .forms import AnswerForm,QuestionForm,PreviousReportEditLoggerForm


class MonthlyReportAdmin(admin.ModelAdmin):
    list_display = ('period_ending','company')
    search_fields = ('company__name',)

admin.site.register(MonthlyReport, MonthlyReportAdmin)


class QuestionCategoryInline(admin.TabularInline):
    model = Question
    extra = 0
    fields = ('company', 'next_question', 'next_question_if', 'question_text',
              'short_tag', 'ask_order', 'show_on_ui', 'common_to_all_companies')


class QuestionCategoryAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'is_active', 'purpose')
    inlines = (QuestionCategoryInline, )
    search_fields = ('group_name',)

admin.site.register(QuestionCategory, QuestionCategoryAdmin)




class QuestionAnswerInline(admin.TabularInline):
    model = Answer
    extra = 0
    fields = [field.name for field in Answer._meta.fields]
    readonly_fields = ['company','monthly_report',]
    show_change_link = True
    form = AnswerForm


class QuestionAdmin(admin.ModelAdmin):

    def answers(self, obj):
        return obj.answer_set.count()

    list_display = ('short_tag', 'question_category', 'common_to_all_companies',
                    'show_on_ui', 'question_text', 'ask_order', 'answers')

    form = QuestionForm
    inlines = (QuestionAnswerInline, )
    search_fields = ('short_tag','question_text',)

class AnswerAdmin(admin.ModelAdmin):
    form = AnswerForm
    model = Answer
    search_fields = ('company__name',)

admin.site.register(Question, QuestionAdmin)

admin.site.register(Answer,AnswerAdmin)



class FinancialStatementEntryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FinancialStatementEntry._meta.fields]
    search_fields = ('company__name',)

admin.site.register(FinancialStatementEntry,FinancialStatementEntryAdmin)


class PreviousReportEditLoggerAdmin(admin.ModelAdmin):
    model = PreviousReportEditLogger
    form = PreviousReportEditLoggerForm
    list_display = ['company','user','reporting_period','section_name','changed_item','old_value','new_value','date_changed']
    search_fields = ('company__name','section_name','user__username','question_item__question_text','finacial_statement_item__fse_tag__all_sight_name')
    #'finacial_statement_item__fsetag__all_sight_name','question_item__question_text'

    def changed_item(self,obj):
        if obj.section_name == PreviousReportEditLogger.ANSWER:
            return obj.question_item
        return obj.finacial_statement_item

    def has_add_permission(self, request):
        return False


admin.site.register(PreviousReportEditLogger,PreviousReportEditLoggerAdmin)