from django.conf.urls import patterns, include, url

urlpatterns = patterns('music.views',
    url(r'^track-music-files/$', 'load_tracks_view', name='load-tracks_page'),
    url(r'^delete-queue-item/$', 'delete_queue_item_view', name='delete_queue_item_page'),
    url(r'^queue-track/$', 'queue_track_view', name='queue_track_page'),
    url(r'^instant-search/$', 'instant_search_view', name='instant_search_page'),
    url(r'^search/$', 'search_view', name='search_page'),
    url(r'^profile/$', 'profile_view', name='my_profile_page'),
    url(r'^profile/(?P<user_id>.*)/$', 'profile_view', name='profile_page'),
    url(r'^logout/$', 'logout_view', name='logout_page'),
    url(r'^$', 'index_view', name='index_page'),
)
