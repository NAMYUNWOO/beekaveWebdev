from django.shortcuts import render
from reviewPage.models import reviewMovie,reviewGame,reviewTV
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def reviews(request,type,id,pid):
    if type == "m":
        cmmtList = reviewMovie.objects.filter(contentsId=id).order_by('-score')
    if type == "g":
        cmmtList = reviewGame.objects.filter(contentsId=id).order_by('-score')
    if type == "t":
        cmmtList = reviewTV.objects.filter(contentsId=id).order_by('-score')

    lenCmmtList = len(cmmtList)
    pageHeadIdx = (int(pid)-1)*20
    pageTailIdx = pageHeadIdx+20
    if pageTailIdx > lenCmmtList:
        pageTailIdx = lenCmmtList

    return render(request,'reviewPage/reviewPage_scorelow.html',{"reviewList":cmmtList[pageHeadIdx:pageTailIdx]})
