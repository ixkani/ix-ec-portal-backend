from django.contrib import admin
from django import forms
from .models import MonthlyReport, QuestionCategory, Question, Answer

from .forms import AnswerForm,QuestionForm


class MonthlyReportAdmin(admin.ModelAdmin):
    list_display = ('period_ending','company')

admin.site.register(MonthlyReport, MonthlyReportAdmin)


class QuestionCategoryInline(admin.TabularInline):
    model = Question
    extra = 0
    fields = ('company', 'next_question', 'next_question_if', 'question_text',
              'short_tag', 'ask_order', 'show_on_ui', 'common_to_all_companies')


class QuestionCategoryAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'is_active', 'purpose')
    inlines = (QuestionCategoryInline, )

admin.site.register(QuestionCategory, QuestionCategoryAdmin)




class QuestionAnswerInline(admin.TabularInline):
    model = Answer
    extra = 0
    fields = [field.name for field in Answer._meta.fields]
    form = AnswerForm


class QuestionAdmin(admin.ModelAdmin):

    def answers(self, obj):
        return obj.answer_set.count()

    list_display = ('short_tag', 'question_category', 'common_to_all_companies',
                    'show_on_ui', 'question_text', 'ask_order', 'answers')

    form = QuestionForm
    inlines = (QuestionAnswerInline, )

class AnswerAdmin(admin.ModelAdmin):
    form = AnswerForm
    model = Answer

admin.site.register(Question, QuestionAdmin)

admin.site.register(Answer,AnswerAdmin)