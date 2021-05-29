from django import forms
from django.forms import widgets
from album.models import Photo, Albums

class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Search')

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('signature', 'img', 'album', 'category')


class AlbumsForm(forms.ModelForm):
    class Meta:
        model = Albums
        fields = ('name', 'description', 'category')