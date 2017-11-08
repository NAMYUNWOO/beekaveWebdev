from django.conf.urls import include, url
from detail  import views
app_name = 'detail'
urlpatterns = [
    url(r'^(?P<type>[m|g|t]{1})(?P<id>\d+)/$',views.contentsInfo,name = 'contentsInfo'),
    url(r'^(?P<type>[m|g|t]{1})(?P<id>\d+)/post/$',views.postReview,name = 'postReview'),
    url(r'^(?P<type>[m|g|t]{1})(?P<id>\d+)/',include('reviewPage.urls',namespace ='reviews')),
]
