from django.conf.urls import patterns, url
from online import views
from upload_avatar.app_settings import UPLOAD_AVATAR_URL_PREFIX_CROPPED, UPLOAD_AVATAR_URL_PREFIX_ORIGINAL


urlpatterns = patterns('',
	url(r'^$',views.login, name='login'),
	url(r'^login/$',views.login, name='login'),
	url(r'^regist/$',views.regist, name='regist'),
	url(r'^index/$',views.index, name='index'),
	url(r'^logout/$',views.logout, name='logout'),
	url(r'^active/(?P<activecode>.+)/$',views.active, name='active'),
	url(r'^upload/?$', views.upload, name="upload"),
	url(r'^implement/?$', views.implement, name="implement"),
    url(r'%s(?P<filename>.+)/?$' % UPLOAD_AVATAR_URL_PREFIX_ORIGINAL,
        views.get_upload_images
        ),
    url(r'^%s(?P<filename>.+)/?$' % UPLOAD_AVATAR_URL_PREFIX_CROPPED,
        views.get_avatar
        )
)