# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-26 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=256)),
                ('SecondName', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=70)),
            ],
        ),
    ]