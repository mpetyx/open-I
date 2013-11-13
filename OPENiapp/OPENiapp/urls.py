from django.conf.urls import patterns, include, url

from django.contrib import admin

from django.views.generic.base import TemplateView

from user_management.SignIn import facebook, twitter

from views import facebook_get_photos, facebook_get_photos_since, facebook_get_photos_until

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

                       url(r'^facebook/photos/$', facebook_get_photos, name='facebook_get_photos'),

                       url(r'^facebook/photos/(since=\d+)$', facebook_get_photos_since, name='facebook_get_photos_since'),

                       url(r'^facebook/photos/(until=\d+)$', facebook_get_photos_until, name='facebook_get_photos_until')

)
