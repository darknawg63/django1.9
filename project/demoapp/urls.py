from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.MusicianList.as_view(), name='index'),
    url(r'^detail/(?P<pk>\d+)/$', views.MusicianDetail.as_view(), name='musician_detail'),
    url(r'add/$', views.musician_create, name='musician_create'),
]
