# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-09 07:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('releaseDate', models.DateTimeField()),
                ('summary', models.TextField()),
            ],
            options={
                'ordering': ('releaseDate',),
            },
        ),
        migrations.CreateModel(
            name='MovieReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('date', models.DateTimeField()),
                ('movieid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='sceneIMG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scene', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='moviereview',
            name='userid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='detail.User'),
        ),
        migrations.AddField(
            model_name='movie',
            name='actor',
            field=models.ManyToManyField(to='detail.Person'),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ManyToManyField(to='detail.Director'),
        ),
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ManyToManyField(to='detail.sceneIMG'),
        ),
    ]
