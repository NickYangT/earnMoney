# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-30 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20170930_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersmodel',
            name='image',
            field=models.FileField(blank=True, default='../static/defualt.jpg', upload_to='../static/', verbose_name='\u56fe\u50cf'),
        ),
    ]
