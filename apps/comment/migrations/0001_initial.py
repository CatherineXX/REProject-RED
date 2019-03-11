# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-07 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assin_comment', models.CharField(max_length=100)),
                ('comment_content', models.TextField(blank=True)),
                ('comment_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='评论日期')),
                ('member_openid', models.CharField(blank=True, max_length=100, null=True, verbose_name='openid')),
            ],
            options={
                'db_table': 'comment',
            },
        ),
    ]
