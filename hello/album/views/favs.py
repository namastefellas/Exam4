from django.shortcuts import redirect
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    View
)
from django.urls import reverse, reverse_lazy
]from django.utils.http import urlencode
from django.shortcuts import render, get_object_or_404, redirect
from article.models import Photo, Albums
from django.http import JsonResponse



class FavsAdd(View):
    def get(self, request, *args, **kwargs):
        photos = get_object_or_404(Photo, pk=kwargs.get('pk'))
        user = self.request.user
        if user in photos.favoutires.all():
            raise ValueError("Already in favs")
        else :
            photos.favourites.add(user)
            photos.save()
        return JsonResponse({"data": "www"})

class FavsDelete(View):
    def get(self, request, *args, **kwargs):
        photos = get_object_or_404(Photo, pk=kwargs.get('pk'))
        user = self.request.user
        photos.favourites.remove(user)
        photos.save()
        return JsonResponse({"data": "www"})

class FavsAddAlb(View):
    def get(self, request, *args, **kwargs):
        album = get_object_or_404(Albums, pk=kwargs.get('pk'))
        user = self.request.user
        album.favourites.add(user)
        album.save()
        return JsonResponse({"data": "www"})

class FavsDeleteAlb(View):
    def get(self, requset, *args, **kwargs):
        album = get_object_or_404(Albums, pk=kwargs.get('pk'))
        user = self.request.user
        album.likes.remove(user)
        album.save()
        return JsonResponse({"data": "www"})
