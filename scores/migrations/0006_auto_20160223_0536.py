# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0005_auto_20160223_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sport',
            name='competitors',
            field=models.IntegerField(blank=True),
        ),
    ]
