# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0021_auto_20170911_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trialbalance',
            name='gl_account_name',
            field=models.CharField(max_length=150),
        ),
    ]
