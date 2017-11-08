from django.db import models
from detail.models import Movie,Game,TV
from django.contrib.auth.models import User
# Create your models here.
class reviewMovie(models.Model):
    reviewUser = models.ForeignKey(User,related_name="author",default=0)
    date = models.DateTimeField()
    comment = models.CharField(max_length=2000)
    score = models.FloatField()
    contentsId = models.ForeignKey(Movie,null=False)
    recommend=  models.IntegerField()
    nonRecommend =  models.IntegerField()
    votingUser = models.ManyToManyField(User,related_name="votingUser")
    def __str__(self):
        return self.comment[:7]

class reviewGame(models.Model):
    user = models.CharField(max_length=200)
    date = models.DateTimeField()
    comment = models.CharField(max_length=2000)
    score = models.FloatField()
    contentsId = models.ForeignKey(Game,null=False)
    def __str__(self):
        return self.user

class reviewTV(models.Model):
    user = models.CharField(max_length=200)
    date = models.DateTimeField()
    comment = models.CharField(max_length=2000)
    score = models.FloatField()
    contentsId = models.ForeignKey(TV,null=False)
    def __str__(self):
        return self.user
