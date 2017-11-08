# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('thumbnail', models.URLField()),
                ('accessUrl', models.URLField()),
                ('accessImg', models.IntegerField()),
                ('releaseDate', models.DateField()),
                ('score', models.IntegerField()),
                ('summary', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('thumbnail', models.URLField()),
                ('accessUrl', models.URLField()),
                ('accessImg', models.IntegerField()),
                ('releaseDate', models.DateField()),
                ('score', models.IntegerField()),
                ('summary', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='moviereview',
            name='movieid',
        ),
        migrations.RemoveField(
            model_name='moviereview',
            name='userid',
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={},
        ),
        migrations.RemoveField(
            model_name='movie',
            name='actor',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='img',
        ),
        migrations.AddField(
            model_name='movie',
            name='accessImg',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='accessUrl',
            field=models.URLField(default='https://www.netflix.com/kr-en/title/80091936'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='score',
            field=models.IntegerField(default=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='thumbnail',
            field=models.URLField(default='http://res.cloudinary.com/beekave/image/upload/v1503487539/okja2_rpaauh.jpg'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='releaseDate',
            field=models.DateField(),
        ),
        migrations.DeleteModel(
            name='Director',
        ),
        migrations.DeleteModel(
            name='MovieReview',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='sceneIMG',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
