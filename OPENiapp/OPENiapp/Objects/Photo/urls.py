from django.conf.urls import patterns, url

from views import *

urlpatterns = patterns('',

                       url(r'^post', photo_choose_media, name='photo_choose_media'),

                       url(r'^facebook/photos/$', facebook_get_photos, name='facebook_get_photos'),

                       url(r'^facebook/photos/(since=\d+)$', facebook_get_photos_since,
                           name='facebook_get_photos_since'),

                       url(r'^facebook/photos/(until=\d+)$', facebook_get_photos_until,
                           name='facebook_get_photos_until'),


                       url(r'^facebook/album/Openi/post/$', facebook_post_photos, name='facebook_post_photos'),

                       url(r'^facebook/album/Openi/photos/$', facebook_get_album_photos,
                           name='facebook_get_album_photos'),

                       url(r'^facebook/album/Openi/photos/before=(.+)$', facebook_get_photos_before,
                           name='facebook_get_photos_before'),

                       url(r'^facebook/album/Openi/photos/after=(.+)$', facebook_get_photos_after,
                           name='facebook_get_photos_after'),
                       
                       url(r'^facebook/album/Openi/delete/(.+)$', facebook_delete_photo, name='facebook_delete_photo')
)
