from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from playlist.models import Playlist

# Create your views here.

def index(request):
	playlist_list = Playlist.objects.order_by('-pub_date')
	template = loader.get_template('index.html')
	context = {
		'playlist_list' : playlist_list,
	}
	return HttpResponse(template.render(context, request))


def playlist(request, playlist_id):
	template = loader.get_template('playlist_detail.html')
	play_list = Playlist.objects.get(pk=playlist_id)
	music_list = play_list.items.all()

	context = {
		'playlist' : play_list,
		'music_list' : music_list,
	}
	return HttpResponse(template.render(context, request))