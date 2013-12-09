__author__ = 'mpetyx'


from django.conf.urls import patterns, include, url

from django.contrib import admin

from django.views.generic.base import TemplateView

from tastypie.api import Api
from .Resources import PhotoResource

api = Api(api_name='media')
api.register(PhotoResource())

urlpatterns = api.urls