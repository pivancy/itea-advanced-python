# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('available_money', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]
