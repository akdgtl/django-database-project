# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-05 17:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='uer',
            new_name='user',
        ),
    ]
