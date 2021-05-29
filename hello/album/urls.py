from django.urls import path
from album.views.photo import PhotoListView, PhotoView, PhotoCreate, PhotoEdit, PhotoDelete
from album.views.album import AlbumView, AlbumCreate, AlbumUpdate, AlbumDelete
from album.views.favs import FavsAdd, FavsDelete, FavsAddAlb, FavsDeleteAlb

app_name = 'album'

urlpatterns = [
    path('', PhotoListView.as_view(), name='photolist'),
    path('gallery/<int:pk>', PhotoView.as_view(), name='photoview'),
    path('gallery/create/', PhotoCreate.as_view(), name='photoadd'),
    path('gallery/<int:pk>/edit/', PhotoEdit.as_view(), name='photoedit'),
    path('gallery/<int:pk>/delete/', PhotoDelete.as_view(), name='photodelete'),
    path('gallery/<int:pk>/album/', AlbumView.as_view(), name='albumview'),
    path('gallery/album/create/', AlbumCreate.as_view(), name='albumcreate'),
    path('gallery/<int:pk>/album/edit/', AlbumUpdate.as_view(), name='albumedit'),
    path('gallery/<int:pk>/album/delete', AlbumDelete.as_view(), name='albumdelete'),
    path('<int:pk>/favs_add', FavsAdd.as_view(), name='favsadd'),
    path('<int:pk>/favs_delete', FavsDelete.as_view(), name='favsdelete'),
    path('<int:pk>/favs_add_alb', FavsAddAlb.as_view(), name='favsaddalb'),
    path('<int:pk>/favs_delete_add', FavsDeleteAlb.as_view(), name='favsdeletealb')
]