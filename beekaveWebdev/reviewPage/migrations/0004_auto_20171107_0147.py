# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-06 16:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewPage', '0003_auto_20171107_0124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewmovie',
            old_name='reivewUser',
            new_name='reviewUser',
        ),
    ]
