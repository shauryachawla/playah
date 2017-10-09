# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Song, Artist, Album
# Register your models here.
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Artist)