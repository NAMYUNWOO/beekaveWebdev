# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-06 16:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviewPage', '0002_auto_20170911_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewmovie',
            name='user',
        ),
        migrations.AddField(
            model_name='reviewmovie',
            name='reivewUser',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reviewmovie',
            name='votingUser',
            field=models.ManyToManyField(related_name='votingUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
