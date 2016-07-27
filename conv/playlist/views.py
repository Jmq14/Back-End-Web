from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.utils import timezone


from models import Playlist
from music.models import Track
from online.models import User

# Create your views here.

def index(request):
	playlist_list = Playlist.objects.order_by('-pub_date')
	template = loader.get_template('index.html')
	context = {
		'playlist_list' : playlist_list,
	}
	return HttpResponse(template.render(context, request))


def playlist(request, playlist_id):
	template = loader.get_template('detail.html')
	play_list = Playlist.objects.get(id=playlist_id)
	music_list = play_list.tracks.all()

	context = {
		'playlist' : play_list,
		'music_list' : music_list,
	}
	return HttpResponse(template.render(context, request))

def mark(request, track_id):
	template = loader.get_template('mark.html')
	track = Track.objects.get(id=track_id)
	user_id = request.COOKIES.get('user_id')
	try:
		user = User.objects.get(id=user_id)
	except:
		return HttpResponse(template.render({'login' : False}, request))
	else:
		context = {
			'login' : True,
			'user' : user,
			'track' : track
		}
		return HttpResponse(template.render(context, request))
		

def addTrackToList(request, track_id, playlist_id):
	play_list = Playlist.objects.get(id=playlist_id)
	track = Track.objects.get(id=track_id)
	if track in play_list.tracks:
		context = {
			'track' : track,
			'playlist' : play_list,
			'msg' : "is already existed in this playlist. "
		}
	else:
		playlist.add(track)
		playlist.save()
		context = {
			'track' : track,
			'playlist' : play_list,
			'msg' : "has been added into this playlist! "
		}
	return HttpResponseRedirect(reverse('playlist:detail', args=(play_list.id,)))

def createPlaylist(request, track_id, playlist_name, owner_id):
	created_by = User.objects.get(id=owner_id)
	new_list = Playlist(
		name = playlist_name,
		owner = created_by,
		pub_date = timezone.now(),
	)
	new_list.save()
	track = Track.objects.get(id=track_id)
	new_list.tracks.add(track)
	context = {
		'track' : track,
		'playlist' : new_list,
		'msg' : "has been added into the new playlist! "
	}
	return HttpResponseRedirect('/playlist/')


def choose(request, track_id):
	#template = loader.get_template('mark.html')
	track = Track.objects.get(id=track_id)
	user_id = request.COOKIES.get('user_id')
	user = User.objects.get(id=user_id)
	playlist_list = user.created_list
	try:
		selected_playlist = playlist_list.get(pk=request.POST['playlist']) 
	except (KeyError, Playlist.DoesNotExist):
		playlist_name = request.POST['new_playlist_name']
		return createPlaylist(request, track_id, playlist_name, user_id)
		#return createPlaylist(request, track_id, playlist_name, user_id)
	else:
		return addTrackToList(request, track_id, selected_playlist.id)