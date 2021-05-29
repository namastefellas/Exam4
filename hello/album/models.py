from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db.models.fields import related
import uuid

# Create your models here.

status = [('private', 'Приватно'), ('public', 'Публично')]

class Photo(models.Model):
    signature = models.CharField(
        max_length=120, 
        null=False, 
        blank=False, 
        verbose_name='Подпись'
        )
    author = models.ManyToManyField(
        get_user_model(), 
        related_name='photos',
        verbose_name='Автор',
        default=1
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    img = models.ImageField(
        upload_to='user_pics', 
        null=False,
        blank=False,
        verbose_name='Фото',
        )
    album = models.ForeignKey(
        'album.Albums',
        on_delete=CASCADE,
        verbose_name='Альбом',
        null=True,
        blank=True

    )
    category = models.CharField(max_length=100, null=True, blank=True, default='public', choices=status)
    eyw_transactionref=models.CharField(max_length=100, null=True, blank=True, unique=True)

    favourites = models.ManyToManyField(
        get_user_model(),
        related_name='fav_pic',
        db_table='pic_favs'
    )



    class Meta:
        db_table = 'photos'
        verbose_name = 'Фотография'
        verbose_name = 'Фотографии'



class Albums(models.Model):
    name = models.CharField(
        max_length=120, 
        null=False, 
        blank=False, 
        verbose_name='Название'
        )
    description = models.TextField(
        max_length=400,
        null=True,
        blank=True,
        verbose_name='Описание'
    )
    album_author = models.ManyToManyField(
        get_user_model(), 
        default=1,
        related_name='albums',
        verbose_name='Автор Альбома'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    category = models.CharField(max_length=100, null=True, blank=True, default='public', choices=status)

    favourites = models.ManyToManyField(
        get_user_model(),
        related_name='fav_alb',
        db_table='alb_fav'
    )


    class Meta:
        db_table = 'albums'
        verbose_name = 'Альбом'
        verbose_name = 'Альбомы'