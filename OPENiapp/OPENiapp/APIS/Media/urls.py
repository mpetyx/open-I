__author__ = 'mpetyx'

from django.conf.urls import patterns, include, url

from django.contrib import admin

from django.views.generic.base import TemplateView

from tastypie.api import Api
from Photo.urls import urlpatterns as photo_urls

urlpatterns = patterns('',
  # ...more URLconf bits here...
  # Then add:
  # (r'^Photo/', include(v1_api.urls)),
)

urlpatterns = urlpatterns + photo_urls
