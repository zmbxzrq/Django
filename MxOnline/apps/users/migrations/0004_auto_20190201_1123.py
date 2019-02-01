# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-01 11:23
from __future__ import unicode_literals

import datetime
import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190131_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u53d1\u9001\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(choices=[('register', '\u6ce8\u518c'), ('forget', '\u627e\u56de\u5bc6\u7801')], max_length=10, verbose_name='\u9a8c\u8bc1\u7801\u7c7b\u578b'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username'),
        ),
    ]
