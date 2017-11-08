"""beekave URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from mainPage import views
from reviewPage import views as reviewViews
from detail import views as detailViews
from beekave.views import UserCreateView, UserCreateDoneTV

app_name = 'index'
urlpatterns = [
    url(r'^$',views.index, name ='index'),
    url(r'^movie/',include('detail.urls',namespace ="movieDetail")),
    url(r'^game/',include('detail.urls',namespace ="gameDetail")),
    url(r'^tv/',include('detail.urls',namespace ="tvDetail")),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),
    url(r'^review/like/$',reviewViews.review_like,name = 'review_like'),
    url(r'^reivew/dislike/$',reviewViews.review_dislike,name = 'review_dislike'),
    url(r'^reivew/post/$',detailViews.postReview,name = 'postReview'),
    url(r'^admin/', admin.site.urls),
]
