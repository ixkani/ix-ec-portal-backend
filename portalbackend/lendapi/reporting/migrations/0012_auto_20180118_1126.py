# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-18 11:26
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0011_auto_20171027_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='monthlyreport',
            name='signoff_by_name',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator('^([(\\[]|[a-zA-Z0-9_\\s]|["-\\.\'#&!]|[)\\]])+$')]),
        ),
        migrations.AlterField(
            model_name='monthlyreport',
            name='signoff_by_title',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator('^([(\\[]|[a-zA-Z0-9_\\s]|["-\\.\'#&!]|[)\\]])+$')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_data_type',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3, message='Atleast 3 characters required')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='next_question_if',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.MinLengthValidator(10, message='Atleast 10 characters required')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(10, message='Atleast 10 characters required')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='short_tag',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3, message='Atleast 3 characters required')]),
        ),
    ]