# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-22 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='activecode',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
