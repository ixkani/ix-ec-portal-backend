# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20170901_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='companymeta',
            name='setup_completed',
            field=models.BooleanField(default=False),
        ),
    ]
