# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0022_auto_20170911_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialstatemententrytag',
            name='is_total_row',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='defaultaccounttagmapping',
            name='software',
            field=models.CharField(choices=[('Quickbooks', 'Quickbooks'), ('Xero', 'Xero'), ('Sage', 'Sage')], max_length=60),
        ),
    ]
