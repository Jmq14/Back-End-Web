from django.conf.urls import patterns, url
from online import views

urlpatterns = patterns('',
	url(r'^$',views.index, name='index'),
	url(r'^login/$',views.login, name='login'),
	url(r'^regist/$',views.regist, name='regist'),
	url(r'^person_info/$',views.person_info, name='person_info'),
	url(r'^logout/$',views.logout, name='logout'),
	url(r'^mymusic/$',views.mymusic, name='mymusic'),
	url(r'^discover_ranklist/$',views.discover_ranklist, name='discover_ranklist'),
	url(r'^discover_playlist/$',views.discover_playlist, name='discover_playlist'),
	url(r'^active/(?P<activecode>.+)/$',views.active, name='active')
)