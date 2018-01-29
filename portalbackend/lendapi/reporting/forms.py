from .models import Question
from django import forms
from django.db import models
from portalbackend.validator.errormapping import ErrorMessage,UIErrorMessage
from django.forms.fields import CharField
from django.contrib.postgres.forms import SimpleArrayField
from .models import MonthlyReport, QuestionCategory, Question, Answer


class QuestionForm(forms.ModelForm):
    question_choices = SimpleArrayField(CharField(), delimiter='|', required=False,
                                        widget=forms.Textarea(attrs={'placeholder': "Separate with | as delimiter",
                                                                     'title': "use | as delimiter"}))

    class Meta:
        model = Question
        fields = [field.name for field in Question._meta.fields]

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required' : UIErrorMessage.REQUIRED_VALID_DATA}


class AnswerForm(forms.ModelForm):
    class Meta:
        fields = [field.name for field in Answer._meta.fields]
        model = Answer
        widgets = {
            'answer': forms.TextInput(attrs={'width': 150})
        }
    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required' : UIErrorMessage.REQUIRED_VALID_DATA}
