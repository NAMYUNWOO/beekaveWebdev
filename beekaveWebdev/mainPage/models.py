from django.db import models

#from django.conf import settings
#os.environ.setdefault("DJANGO_SETTINGS_MODULE","beekave.settings")
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.URLField()
    rank = models.IntegerField()
    rate = models.CharField(max_length = 200)
    score = models.IntegerField()
    movieID = models.IntegerField()
    def __str__(self):
        return self.title


class Game(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.URLField()
    rank = models.IntegerField()
    platform = models.CharField(max_length = 200)
    score = models.IntegerField()
    gameID = models.IntegerField()
    def __str__(self):
        return self.title

class TV(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.URLField()
    rank = models.IntegerField()
    broadcaster = models.CharField(max_length = 200)
    score = models.IntegerField()
    tvId = models.IntegerField()
    def __str__(self):
        return self.title
