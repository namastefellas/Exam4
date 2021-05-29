from django.contrib import admin
from album.models import Photo, Albums

# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'img', 'signature', 'album']
    readonly_fields = ['id', 'created_at']


class AlbumsAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'name', 'description']
    readonly_fields = ['id', 'created_at']

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Albums, AlbumsAdmin)