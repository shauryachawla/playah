from django import forms
from .models import Artist, Album, Song

class NewArtistForm(forms.ModelForm):
	title = forms.CharField(max_length = 20, help_text = "Please enter the name of the artist/band.")

	class Meta:
		model = Artist
		fields = ('title',)

class NewAlbumForm(forms.ModelForm):
	title = forms.CharField(max_length = 30, help_text = "Please enter the name of the album.")
	artist = forms.ModelChoiceField(Artist.objects.all())

	class Meta:
		model = Album
		fields = ('title','artist')

class NewSongForm(forms.ModelForm):
	title = forms.CharField(max_length = 30)
	artist = forms.ModelChoiceField(queryset=Artist.objects.all(),
									empty_label='Not Specified',
									widget=forms.Select(attrs=
										{
											"onChange":'getAlbum()'
										}))
	album = forms.ModelChoiceField(Album.objects.all())

	class Meta:
		model = Song
		fields = ('title', 'artist', 'album')