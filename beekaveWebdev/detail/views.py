from django.shortcuts import render
from detail.models import Movie,Game,TV
from mainPage.models import Movie as Top10movie
from django.http import Http404
from django.shortcuts import redirect
from django.http import HttpResponse
from detail.forms import movieReviewForm,gameReviewForm,tvReviewForm
from ipware.ip import get_ip
from django.utils import timezone
import json
import re
# Create your views here.
def contentsInfo(request,type,id):
    mInfo = Movie.objects.get(pk=id)
    top4_movie_list = Top10movie.objects.all().order_by('rank')[:4]
    form = movieReviewForm
    context = {"top10_movie_list":top4_movie_list,"contentsInfo":mInfo,"form":form,}
    return render(request,'detail/detail.html',context)

def gameInfo(request,id):
    top4_movie_list = Top10movie.objects.all().order_by('rank')[:4]
    gInfo = Game.objects.get(pk=id)
    context = {"top4_movie_list":top4_movie_list,"contentsInfo":gInfo}
    return render(request,'detail/detail.html',context)

def tvInfo(request,id):
    top4_movie_list = Top10movie.objects.all().order_by('rank')[:4]
    tInfo = TV.objects.get(pk=id)
    context = {"top4_movie_list":top4_movie_list,"contentsInfo":tInfo}
    return render(request,'detail/detail.html',context)


def postReview(request):
    #print(request.method)
    reviewScore = request.POST.get('reviewScore', None)
    reviewText =  request.POST.get('reviewText', None)
    redirectUrl =  request.POST.get('redirectUrl', None)
    contentsTypeID = redirectUrl.split("/")[2]
    contentsType = re.findall("[m|g|t]",contentsTypeID)[0]
    ID = re.findall("[0-9]+",contentsTypeID)[0]
    form = movieReviewForm()
    post = form.save(commit=False)
    post.reviewUser = request.user
    post.date = timezone.now()
    post.nonRecommend = 0
    post.recommend = 0
    post.contentsId = Movie.objects.get(pk=ID)
    post.comment = reviewText
    post.score = str(float(reviewScore)/2)
    post.save()
    context = {'url': redirectUrl}
    return HttpResponse(json.dumps(context), content_type="application/json")
