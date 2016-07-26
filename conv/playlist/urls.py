from django.conf.urls import url
from . import views

#  create url patterns.

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^id=(?P<playlist_id>[0-9]+)/$', views.playlist, name='playlist_detail'),
]