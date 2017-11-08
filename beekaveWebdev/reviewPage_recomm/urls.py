from django.conf.urls import include, url
from reviewPage  import views
urlpatterns = [
    url(r'order_by_recomm/$',views.reviews,name = 'reviews'),
]
