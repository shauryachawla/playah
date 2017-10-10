from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^albums/$', views.show_albums, name='show_albums'),
    url(r'^songs/', views.show_songs, name='show_songs'),
    url(r'^albums/(?P<album_title>[\w|\W]+)/$', views.show_album_page, name='show_album_page'),
    url(r'^add_artist/', views.add_artist, name='add_artist'),
]
