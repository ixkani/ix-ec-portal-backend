# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 19:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20170907_2015'),
        ('accounting', '0017_financialstatemententrytag_generated_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoADefaultID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('software', models.CharField(choices=[('Quickbooks', 'Quickbooks'), ('Zero', 'Zero'), ('Sage', 'Sage')], max_length=60)),
                ('gl_account_id', models.IntegerField(blank=True, null=True)),
                ('gl_account_name', models.CharField(max_length=60, verbose_name='Account Name')),
                ('gl_account_type', models.CharField(max_length=60, verbose_name='Account Type')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Company')),
            ],
            options={
                'verbose_name': 'Chart of Accounts Default ID',
                'verbose_name_plural': 'Chart of Accounts Default IDs',
                'db_table': 'coadefaultid',
            },
        ),
    ]
