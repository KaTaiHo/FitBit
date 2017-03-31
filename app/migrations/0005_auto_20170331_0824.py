# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-31 08:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_accesstokeninfo_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='data',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
