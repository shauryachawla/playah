# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Album, Song, Artist
# Create your views here.
def index(request):
	return render(request, 'index.html', {})

def show_albums(request):
	albums = Album.objects.all().order_by('artist')
	return render(request, 'albums.html', {'albums' : albums})

def show_songs(request):
	songs = Song.objects.all()
	return render(request, 'songs.html', {'songs' : songs})

def show_album_page(request, album_title):
	print str(album_title)
	album = Album.objects.get(title=album_title)
	return render(request, 'album_page.html', {'album' : album})