# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 21:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0012_trialbalance_account_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trialbalance',
            old_name='account_id',
            new_name='gl_account_id',
        ),
    ]