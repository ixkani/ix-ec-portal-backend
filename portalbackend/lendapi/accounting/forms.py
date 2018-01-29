from .models import CoA,CoAMap
from django import forms
from django.db import models
from portalbackend.validator.errormapping import ErrorMessage,UIErrorMessage


class CoAForm(forms.ModelForm):
    class Meta:
        model = CoA
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(CoAForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required': UIErrorMessage.REQUIRED_VALID_DATA}


class CoAMapForm(forms.ModelForm):
    class Meta:
        model = CoAMap
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(CoAMapForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required': UIErrorMessage.REQUIRED_VALID_DATA}


