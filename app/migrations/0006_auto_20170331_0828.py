# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-31 08:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20170331_0824'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='clientId',
            new_name='user_id',
        ),
    ]
