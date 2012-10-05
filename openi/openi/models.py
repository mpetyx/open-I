__author__ = 'mpetyx'


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

import datetime
from random import random
from tastypie.models import create_api_key
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models import signals
from django.template.loader import render_to_string
from django.utils.hashcompat import sha_constructor
from django.contrib.sites.models import Site

from imagekit.models import ImageSpecField
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from django.core.files.storage import FileSystemStorage
from django.core.files import File
import os


# ###############################
#Credits go to http://djangosnippets.org/snippets/1976/
#and
#http://wavesandmaps.com/utilizing-s3-for-a-heroku-django-app/
# ###############################
#class S3Storage(FileSystemStorage):
#    def __init__(self, bucket=None, location=None, base_url=None):
#        assert bucket
#        if location is None:
#            location = settings.MEDIA_ROOT
#        if base_url is None:
#            base_url = settings.MEDIA_URL
#        self.location = os.path.abspath(location)
#        self.bucket = bucket
#        self.base_url = base_url
#
#    def _open(self, name, mode='rb'):
#        class S3File(File):
#            def __init__(self, key):
#                self.key = key
#
#            def size(self):
#                return self.key.size
#
#            def read(self, *args, **kwargs):
#                return self.key.read(*args, **kwargs)
#
#            def write(self, content):
#                self.key.set_contents_from_string(content)
#
#            def close(self):
#                self.key.close()
#
#        return S3File(Key(self.bucket, name))
#
#    def _save(self, name, content):
#        key = Key(self.bucket, name)
#        if hasattr(content, 'temporary_file_path'):
#            key.set_contents_from_filename(content.temporary_file_path())
#        elif isinstance(content, File):
#            key.set_contents_from_file(content)
#        else:
#            key.set_contents_from_string(content)
#
#        return name
#
#    def delete(self, name):
#        self.bucket.delete_key(name)
#
#    def exists(self, name):
#        return Key(self.bucket, name).exists()
#
#    def listdir(self, path):
#        return [key.name for key in self.bucket.list()]
#
#    def path(self, name):
#        raise NotImplementedError
#
#    def size(self, name):
#        return self.bucket.get_key(name).size
#
#    def url(self, name):
#        return Key(self.bucket, name).generate_url(100000)
#
#    def get_available_name(self, name):
#        return name
#
#
#class S3EnabledImageField(models.ImageField):
#    def __init__(self, bucket=settings.AWS_STORAGE_BUCKET_NAME, verbose_name=None, name=None, width_field=None, height_field=None, **kwargs):
#        self.connection = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
#        if not self.connection.lookup(bucket):
#            self.connection.create_bucket(bucket)
#        self.bucket = self.connection.get_bucket(bucket)
#        kwargs['storage'] = S3Storage(self.bucket)
#        super(S3EnabledImageField, self).__init__(verbose_name, name, width_field, height_field, **kwargs)


class Photo(models.Model):
    # code here http://django-imagekit.readthedocs.org/en/latest/index.html

    """
        Photo model
    """
    name = models.CharField(max_length=100)
    original_image = models.ImageField(upload_to='photos')
    formatted_image = ImageSpecField(image_field='original_image', format='JPEG',
        options={'quality': 90})
    #    original_image = models.CharField(max_length=100)
    #    formatted_image = models.CharField(max_length=100)
    published = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%d"%self.id


class IKOptions:
    spec_module = 'specs'
    cache_dir = 'photos'
    image_field = 'original_image'


#############################################
#############################################
# BASIC OPENI TABLES
#############################################
#############################################

class FacebookProfile(models.Model):
    username  = models.CharField(max_length=255,null=True, blank=True)
    credentials  = models.CharField(max_length=255,null=True, blank=True)

class TwitterProfile(models.Model):
    username  = models.CharField(max_length=255,null=True, blank=True)
    credentials  = models.CharField(max_length=255,null=True, blank=True)

class Person( User ):

#    photo = S3EnabledImageField(blank=True,upload_to='media/persons')
    facebook = models.OneToOneField( FacebookProfile )
    twitter = models.OneToOneField( TwitterProfile )
