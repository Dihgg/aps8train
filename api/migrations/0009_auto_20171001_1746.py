# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_log_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
