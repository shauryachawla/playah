# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Artist(models.Model):
	title = models.CharField(max_length = 25)

	def __unicode__(self):
		return self.title

class Album(models.Model):
	title = models.CharField(max_length = 20)
	artist = models.ForeignKey(Artist)
	
	def __unicode__(self):
		return self.title + " - " + self.artist.title

class Song(models.Model):
	title = models.CharField(max_length = 30)
	album = models.ForeignKey(Album)
	artist = models.ForeignKey(Artist, default='')

	def __unicode__(self):
		return self.title + " - " +self.album.title