from django.conf.urls import url
from . import views

#  create url patterns.

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^id=(?P<playlist_id>[0-9]+)/$', views.playlist, name='detail'),
	url(r'^trackid=(?P<track_id>[0-9]+)/mark/$', views.mark, name='mark'),
	url(r'^trackid=(?P<track_id>[0-9]+)/mark/choose/$', views.choose, name='choose'),
]