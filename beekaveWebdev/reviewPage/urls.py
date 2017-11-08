from django.conf.urls import include, url
from reviewPage  import views
urlpatterns = [

    url(r'^(?P<filter>[-]{0,1}[a-z]+([&]{0,1}[a-z|A-Z|가-힣|0-9|_])*)/p(?P<pid>\d+)/$',views.reviews,name = 'reviews'),

]

#url(r'^(?P<filter>[-]{0,1}[a-z]+)/p(?P<pid>\d+)/$',views.reviews,name = 'reviews'),
