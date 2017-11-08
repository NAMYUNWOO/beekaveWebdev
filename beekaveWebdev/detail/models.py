from django.db import models
from django.utils import timezone
import time
import os


class Movie(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.URLField()
    accessUrl = models.URLField()
    accessImg = models.CharField(max_length=50)
    releaseDate = models.DateField(blank=False)
    score = models.IntegerField()
    scoreAct = models.IntegerField()
    scoreStory = models.IntegerField()
    scoreDirector = models.IntegerField()
    scoreOST = models.IntegerField()
    scoreVisual = models.IntegerField()
    scoreFresh = models.IntegerField()
    movieCode = models.IntegerField()
    def __str__(self):
        return self.title


class Game(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.URLField()
    accessUrl = models.URLField()
    accessImg = models.CharField(max_length=50)
    releaseDate = models.DateField(blank=False)
    score = models.IntegerField()
    summary = models.TextField()
    def __str__(self):
        return self.title

class TV(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.URLField()
    accessUrl = models.URLField()
    accessImg = models.CharField(max_length=50)
    releaseDate = models.DateField(blank=False)
    score = models.IntegerField()
    summary = models.TextField()
    def __str__(self):
        return self.title
