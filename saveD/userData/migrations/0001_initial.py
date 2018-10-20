# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-20 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=400)),
                ('email_id', models.CharField(max_length=600)),
                ('phoneNumber', models.CharField(max_length=20)),
                ('email_id_friend_1', models.CharField(max_length=600)),
                ('email_id_friend_2', models.CharField(max_length=600)),
                ('email_id_friend_3', models.CharField(max_length=600)),
                ('location', models.CharField(max_length=300)),
                ('blood_group', models.CharField(max_length=4)),
                ('medical_history', models.CharField(max_length=200)),
            ],
        ),
    ]