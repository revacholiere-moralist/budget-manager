# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 07:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_scheduler', '0002_auto_20160823_1621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='budget',
            old_name='cost',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='budget',
            old_name='budget_name',
            new_name='name',
        ),
    ]
