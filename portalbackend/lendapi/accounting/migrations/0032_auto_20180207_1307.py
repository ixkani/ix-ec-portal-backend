# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-07 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0031_auto_20180207_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultaccounttagmapping',
            name='software',
            field=models.CharField(choices=[('quickbooks', 'Quickbooks'), ('xero', 'Xero'), ('sage', 'Sage')], max_length=60),
        ),
    ]