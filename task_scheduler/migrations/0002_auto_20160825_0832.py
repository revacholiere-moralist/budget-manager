# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 01:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='monthly_budget_target',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=99),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='total_saving',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=99),
            preserve_default=False,
        ),
    ]