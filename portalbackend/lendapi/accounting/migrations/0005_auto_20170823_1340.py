# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0004_auto_20170822_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coa',
            name='gl_account_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
