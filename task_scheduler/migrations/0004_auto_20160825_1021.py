# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 03:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_scheduler', '0003_auto_20160825_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]