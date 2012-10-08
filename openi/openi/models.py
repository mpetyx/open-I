__author__ = 'mpetyx'


from django.db import models
import time
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
from PIL import Image
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from django.core.files.storage import FileSystemStorage
from django.core.files import File
import os


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


#class Photo(models.Model):
#
#    name = models.CharField(max_length=100)
#    original_image = models.FileField(upload_to='photos')
#    #    original_image = models.ImageField(upload_to='photos')
#    #    formatted_image = ImageSpecField(image_field='original_image', format='JPEG',
#    #        options={'quality': 90})
#    #    original_image = models.CharField(max_length=100)
#    #    formatted_image = models.CharField(max_length=100)
#    published = models.DateTimeField(auto_now_add=True)
#
#    def __unicode__(self):
#        return "%d"%self.id


#class Person( User ):
#
##    photo = S3EnabledImageField(blank=True,upload_to='media/persons')
#    facebook = models.OneToOneField( FacebookProfile )
#    twitter  = models.OneToOneField( TwitterProfile )
#    photo    = models.ForeignKey(Photo)


class Photo(models.Model):
    """
    three size sets:
        thumbnail (photo_thumb)
        medium (photo_medium)
        original (photo_original)
    """

    now = str(int(time.time()))
    filepath = 'photos/'+now+'/'

    photo_original = models.FileField('original file upload', upload_to="photos")
    photo_medium = models.CharField(max_length=255, blank=True)
    photo_thumb = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    content_date = models.DateField()
    permissions = models.CharField(max_length=255)
    photo_credits = models.CharField(max_length=255, blank=True)
    approved = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_thumb(self):
        return "/site_media/%s" % self.photo_thumb

    def get_medium(self):
        return "/site_media/%s" % self.photo_medium

    def get_original(self):
        return "/site_media/%s" % self.photo_original

    def save(self):
        sizes = {'thumbnail': {'height': 100, 'width': 100}, 'medium': {'height': 300, 'width': 300},}

        super(Photo, self).save()
        photopath = str(self.photo_original.path)  # this returns the full system path to the original file
        im = Image.open(photopath)  # open the image using PIL

        # pull a few variables out of that full path
        extension = photopath.rsplit('.', 1)[1]  # the file extension
        filename = photopath.rsplit('/', 1)[1].rsplit('.', 1)[0]  # the file name only (minus path or extension)
        fullpath = photopath.rsplit('/', 1)[0]  # the path only (minus the filename.extension)

        # use the file extension to determine if the image is valid before proceeding
        if extension not in ['jpg', 'jpeg', 'gif', 'png']: sys.exit()

        # create medium image
        im.thumbnail((sizes['medium']['width'], sizes['medium']['height']), Image.ANTIALIAS)
        medname = filename + "_" + str(sizes['medium']['width']) + "x" + str(sizes['medium']['height']) + ".jpg"
        im.save(fullpath + '/' + medname)
        self.photo_medium = self.filepath + medname

        # create thumbnail
        im.thumbnail((sizes['thumbnail']['width'], sizes['thumbnail']['height']), Image.ANTIALIAS)
        thumbname = filename + "_" + str(sizes['thumbnail']['width']) + "x" + str(sizes['thumbnail']['height']) + ".jpg"
        im.save(fullpath + '/' + thumbname)
        self.photo_thumb = self.filepath + thumbname

        super(Photo, self).save()

    class Meta:
        ordering = ['-content_date']