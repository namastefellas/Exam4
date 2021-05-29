from album.models import Photo
from typing import List
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import (
    View, 
    TemplateView, 
    RedirectView, 
    FormView, 
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from album.forms import SearchForm, PhotoForm
from django.db.models import Q
from django.utils.http import urlencode


class PhotoListView(ListView):
    template_name = 'photo/index.html'
    model = Photo
    context_object_name = 'photos'
    ordering = ('-created_at')
    paginate_by = 3
    paginate_orphans = 1

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(PhotoListView, self).get(request, **kwargs)
    
    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(signature__icontains=self.search_data) 
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})

        return context

class PhotoView(DetailView):
    template_name = 'photo/photo_view.html'
    model = Photo


class PhotoCreate(CreateView):
    template_name = 'photo/photo_create.html' 
    model = Photo
    form_class = PhotoForm

    def form_valid(self, form):
        user = self.request.user
        photos = form.save()
        photos.author.add(user)
        return redirect('album:photoview', pk=photos.pk)


class PhotoEdit(UpdateView):
    template_name = 'photo/photo_edit.html'
    model = Photo
    form_class = PhotoForm
    context_object_name = 'photo'

    def get_success_url(self):
        return reverse('album:photoedit', kwargs={'pk': self.kwargs.get('pk')})


class PhotoDelete(DeleteView):
    model = Photo
    template_name = 'photo/photo_delete.html'
    context_object_name = 'photo'
    success_url = reverse_lazy('album:photolist')