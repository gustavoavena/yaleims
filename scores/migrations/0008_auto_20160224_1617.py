# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 16:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0007_remove_sport_competitors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateField(default=datetime.date(2016, 2, 24)),
        ),
    ]
