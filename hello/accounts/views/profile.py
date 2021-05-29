from django.views.generic import DetailView
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from accounts.models import Profile
from album.models import Photo

class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'user_profile.html'
    context_object_name = 'user'
    paginate_related_by = 3
    paginate_related_orphans = 1

    def get_context_data(self, **kwargs):
        photos = self.object.photos.all().order_by('-created_at')
        paginator = Paginator(photos, self.paginate_related_by, orphans=self.paginate_related_orphans)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
  
        kwargs['page_obj'] = page
        kwargs['projects'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()
        kwargs['profile'] = get_object_or_404(Profile, user__pk=self.kwargs.get('pk'))
        print(kwargs['profile'])
        return super().get_context_data(**kwargs)