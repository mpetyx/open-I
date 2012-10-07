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



#from CamelCaseJSONSerializer import CamelCaseJSONSerializer
from models import *
#import fields


class PhotoResource(ModelResource):
    original_image = fields.FileField(attribute="original_image", null=True, blank=True)
    class Meta:
        queryset = Photo.objects.all()
        authorization = Authorization()

