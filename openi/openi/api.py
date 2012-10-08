__author__ = 'mpetyx'


from django.conf.urls.defaults import patterns, url
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.http import HttpResponse, HttpResponseNotFound, SimpleCookie, QueryDict
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization, DjangoAuthorization#, ApiKeyAuthentication
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication
#from tastypie_Alpha_authentication import MultiAuthentication
from django.core.exceptions import ObjectDoesNotExist
from tastypie.cache import SimpleCache
from tastypie.validation import Validation
from tastypie.utils import trailing_slash
from tastypie.models import create_api_key
from tastypie.exceptions import ImmediateHttpResponse, NotFound
from tastypie.http import HttpForbidden, HttpCreated, HttpConflict, HttpUnauthorized
from tastypie.serializers import Serializer
from tastypie.utils.mime import build_content_type
from tastypie.bundle import Bundle
from tastypie import http, fields as t_fields
from django.db import models, IntegrityError
from django.core.files.base import ContentFile
import time
#from authentication import *
import string, random, hashlib
import json
#import logging
import django
from django.conf import settings
from tastypie import fields

from b64custom import Base64FileField
from form_data_resources import ModelResource


#from CamelCaseJSONSerializer import CamelCaseJSONSerializer
from models import *
from sorl.thumbnail import get_thumbnail


class PhotoResource(ModelResource):
# test query working
# curl --form "name=koukli" --form "original_image=@mike.jpg" http://openi.herokuapp.com/api/openi/photo/
    class Meta:
        queryset = Photo.objects.all()
        authorization = Authorization()


    def override_urls(self):

        return [
            url(r"^(?P<resource_name>%s)/resize%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('resize'), name="resize"),

            url(r"^(?P<resource_name>%s)/handler%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('handler'), name="handler"),

        ]


    def resize(self, request, **kwargs):

        self.is_authorized(request)

        if 'photo_id' in kwargs:
            photo_id = kwargs['photo_id']
        else:
            photo_id   = request.REQUEST.get('photo_id', '')

        bundle = Photo.objects.get(name = photo_id)
        from s3fs import S3FS
        lol =  S3FS( "openiphotos","photos",'AKIAJWJD4LJWZ4PMCWTA','mwuo3YgUVrNoCW+XXvGr/Fk8YIpx+AmAZITMFX+L')

        picture = lol.open(bundle)
        im = get_thumbnail(picture.photo_original, '100x100', crop='center', quality=99)
        return self.create_response(request, im)

#class PhotoSearchResource(ModelResource):
#
#    class Meta:
#        queryset = Photo.objects.filter(status='PU', date_published__lt=datetime.datetime.now).order_by('-date_published')
#        resource_name = 'news'
#
