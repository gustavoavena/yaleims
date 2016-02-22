# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 15:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='residentialcollege',
            name='full_name',
        ),
        migrations.AlterField(
            model_name='points',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 22, 15, 36, 22, 237131, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='residentialcollege',
            name='name',
            field=models.CharField(choices=[('BK', 'Berkeley College'), ('BR', 'Branford College'), ('CC', 'Calhoun College'), ('DC', 'Davenport College'), ('ES', 'Ezra Stile College'), ('JE', 'Jonathan Edwards College'), ('MC', 'Morse College'), ('PC', 'Pierson College'), ('SM', 'Silliman College'), ('SY', 'Saybrook College'), ('TC', 'Trumbull College'), ('TD', 'Timothy Dwight College')], max_length=2, unique=True),
        ),
    ]