# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0002_passenger'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='boarding_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='passenger',
            name='wallet',
            field=models.FloatField(default=0),
        ),
    ]
