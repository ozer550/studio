# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-18 08:00
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('contentcuration', '0126_merge_20201207_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='invitation',
            name='declined',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='invitation',
            name='revoked',
            field=models.BooleanField(default=False),
        ),
    ]
