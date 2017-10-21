# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Album, Song, Artist
from .forms import *
from django.http import HttpResponse
import json
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

def add_album(request):
	if (request.method == 'POST'):
		form = NewAlbumForm(request.POST)

		if form.is_valid():
			form.save()

			return index(request)
		else:
			print form.errors
	else:
		form = NewAlbumForm()
	return render(request, 'new_album.html', {'form' : form})

def add_song(request, qs=None):
	if (request.method == 'POST'):
		form = NewSongForm(request.POST)

		if form.is_valid():
			form.save()

			return index(request)
		else:
			print form.errors

	elif (request.method == 'GET' and request.GET.get('artist_name')):
		if qs is None:
			qs = Album.objects.values_list('title', flat=True).all()
		if request.GET.get('artist_name'):
			artist_name=request.GET.get('artist_name')
			artist = Artist.objects.filter(title=artist_name)
			if artist.count() > 0:
				artist = artist[0]
			qs = Album.objects.filter(artist=artist.id).order_by('title')
		# create an empty list to hold the results
		results = []
		# iterate over each album and append to results list
		for album in qs:
			results.append({"id" : album.id, "title" : album.title})
		# if no results found then append a relevant message to results list
		if not results:
			results.append(("No album found"))
		# return JSON object
		return HttpResponse(json.dumps(results))
	else:
		form = NewSongForm()
	return render(request, 'new_song.html', {'form' : form})
