# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 19:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0020_coadefaultid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coadefaultid',
            name='company',
        ),
        migrations.DeleteModel(
            name='CoADefaultID',
        ),
    ]
