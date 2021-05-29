from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from album.models import Albums
from django.views.generic import View, TemplateView, RedirectView, FormView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.utils.http import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User



from album.forms import AlbumsForm, SearchForm



class AlbumView(DetailView):
    model = Albums
    template_name = 'album/albumview.html'





class AlbumCreate(CreateView):
    template_name = 'album/album_create.html' 
    model = Albums
    form_class = AlbumsForm

    def form_valid(self, form):
        user = self.request.user
        albums = form.save()
        albums.album_author.add(user)
        return redirect('album:photoview', pk=albums.pk)






class AlbumUpdate(UpdateView):
    form_class = AlbumsForm
    model = Albums
    template_name = 'album/album_edit.html'
    context_object_name = 'album'

    def get_success_url(self):
        return reverse('album:albumview', kwargs={'pk': self.kwargs.get('pk')})


class AlbumDelete(DeleteView):
    model = Albums
    template_name = 'album/album_delete.html'
    context_object_name = 'album'
    success_url = reverse_lazy('album:photolist')