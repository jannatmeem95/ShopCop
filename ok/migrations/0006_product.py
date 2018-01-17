# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-13 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ok', '0005_receiptionist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=250)),
                ('price', models.CharField(max_length=250)),
                ('color', models.CharField(max_length=100)),
                ('pic', models.CharField(max_length=100)),
                ('qty', models.CharField(max_length=250)),
            ],
        ),
    ]
