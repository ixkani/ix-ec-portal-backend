# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-18 23:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0007_auto_20171004_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialstatemententry',
            name='monthly_report',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reporting.MonthlyReport'),
        ),
    ]
