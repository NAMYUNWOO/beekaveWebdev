from django.shortcuts import render
from mainPage.models import Movie,Game,TV
from django.http import Http404
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import Http404


# Create your views here.
def index(request):
    top10_movie_list = Movie.objects.all().order_by('rank')
    top10_game_list = Game.objects.all().order_by('rank')
    top10_tv_list = TV.objects.all().order_by('rank')
    context = {'top10_movie_list':top10_movie_list,
    "top10_game_list":top10_game_list,
    "top10_tv_list":top10_tv_list,}
    return render(request,'mainPage/index.html',context)
