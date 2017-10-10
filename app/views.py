# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Album, Song, Artist
from .forms import NewArtistForm
# Create your views here.
def index(request):
	return render(request, 'index.html', {})

def show_albums(request):
	albums = Album.objects.all().order_by('artist')
	return render(request, 'albums.html', {'albums' : albums})

def show_artists(request):
	artists = Artist.objects.all().order_by('title')
	return render(request, 'artists.html', {'artists' : artists})

def show_songs(request):
	songs = Song.objects.all()
	return render(request, 'songs.html', {'songs' : songs})

def show_album_page(request, album_title):
	print str(album_title)
	album = Album.objects.get(title=album_title)
	songs = Song.objects.filter(album__title__exact = album.title)
	return render(request, 'album_page.html', {'album' : album, 'songs' : songs})

def add_artist(request):
	if (request.method == 'POST'):
		form = NewArtistForm(request.POST)

		if form.is_valid():
			form.save(commit=True)

			return index(request)
		else:
			print form.errors
	else:
		form = NewArtistForm()

	return render(request, 'new_artist.html', {'form' : form})