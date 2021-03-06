# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 07:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime(2016, 2, 22, 7, 57, 15, 920482, tzinfo=utc))),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ResidentialCollege',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('BK', 'Berkeley College'), ('BR', 'Branford College'), ('CC', 'Calhoun College'), ('DC', 'Davenport College'), ('ES', 'Ezra Stile College'), ('JE', 'Jonathan Edwards College'), ('MC', 'Morse College'), ('PC', 'Pierson College'), ('SM', 'Silliman College'), ('SY', 'Saybrook College'), ('TC', 'Trumbull College'), ('TD', 'Timothy Dwight College')], max_length=2)),
                ('full_name', models.CharField(max_length=30)),
                ('img_URL', models.CharField(max_length=1024)),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.CharField(max_length=30)),
                ('competitors', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='points',
            name='college',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scores.ResidentialCollege'),
        ),
        migrations.AddField(
            model_name='points',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scores.Match'),
        ),
        migrations.AddField(
            model_name='match',
            name='colleges',
            field=models.ManyToManyField(related_name='matches', through='scores.Points', to='scores.ResidentialCollege'),
        ),
        migrations.AddField(
            model_name='match',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='scores.Sport'),
        ),
    ]
