# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 20:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0010_auto_20170823_1943'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trialbalance',
            options={'verbose_name': 'Trial Balance', 'verbose_name_plural': 'Trial Balances'},
        ),
        migrations.AddField(
            model_name='trialbalance',
            name='currency',
            field=models.CharField(blank=True, max_length=3),
        ),
    ]