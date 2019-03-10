# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-07 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sales_Counts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assin', models.CharField(max_length=100)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
                ('sales_count', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'sale_counts',
            },
        ),
    ]
