"""convmusic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  


urlpatterns = [
    url(r'^index/','online.views.index'),
    url(r'^admin/', admin.site.urls),
    url(r'^online/',include('online.urls')),
<<<<<<< HEAD
    url(r'^playlist/',include('playlist.urls',namespace="playlist")),
=======
>>>>>>> fae7cd3e25cc500fa9bef78f4ad738bf773a54d1
    url(r'', include('upload_avatar.urls')),
    url(r'^music/',include('music.urls')),

]
urlpatterns += staticfiles_urlpatterns()  
