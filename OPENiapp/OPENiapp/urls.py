from django.conf.urls import patterns, include, url

from django.contrib import admin

from django.views.generic.base import TemplateView

from user_management.SignIn import facebook, twitter

from views import *

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'OPENiapp.views.home', name='home'),
                       # url(r'^OPENiapp/', include('OPENiapp.foo.urls')),

                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^accounts/', include('allauth.urls')),

                       # url(r'^media/', include('OPENIapp.APIS.Media.urls')),

                       #https://github.com/mpetyx/moodeet/wiki/Facebook
                       url(r'^person/signin/facebook$', facebook, name='facebook'),

                       #https://github.com/mpetyx/moodeet/wiki/Twitter
                       url(r'^person/signin/twitter$', twitter, name='twitter'),

                       url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html'), name='profile'),

                       url(r'^facebook/photos/media', photo_choose_media, name='photo_choose_media'),

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
                           name='facebook_get_photos_after')

)
