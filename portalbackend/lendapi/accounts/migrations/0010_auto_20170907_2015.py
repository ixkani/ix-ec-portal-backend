# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20170906_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companymeta',
            name='qb_connect_desktop_version',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
