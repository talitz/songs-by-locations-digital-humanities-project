from django.http import HttpResponse
from .models import Song
from django.shortcuts import render


def cityName(request, song_cities):
    return HttpResponse("You're looking at song")

def results(request, song_id):
    response = "You're looking at the cities of song %s."
    return HttpResponse(response % song_id)


def song_list(request):
    return HttpResponse(Song.objects.all())


def index(request):
    all_songs = Song.objects.all()
    songs_ids = [q.id for q in all_songs]
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'songs_name': Song.objects.all(),'songs_id': songs_ids},
    )


def find_song_by_id(request, song_id):
    # Render the HTML template index.html with the data in the context variable
    _song = Song.get_song_by_id(song_id)
    return render(
        request,
        'song.html',
        context={'song': _song},
    )


def find_song_by_name(request, song_name):
    # Render the HTML template index.html with the data in the context variable
    _song = Song.get_song_by_name(song_name)
    return render(
        request,
        'song.html',
        context={'song': _song},
    )


def find_song_by_artist(request, song_artist):
    # Render the HTML template index.html with the data in the context variable
    _song = Song.get_song_by_artist(song_artist)
    return render(
        request,
        'searc.html',
        context={'song': _song},
    )