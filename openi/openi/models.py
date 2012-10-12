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
from django.core.files.storage import default_storage as s3_storage
from django.core.files import File
import os


import urllib2 as urllib
from cStringIO import StringIO


#class Photo(models.Model):
#    # code here http://django-imagekit.readthedocs.org/en/latest/index.html
#
#    """
#        Photo model
#    """
#    name = models.CharField(max_length=100)
#    original_image = models.ImageField(upload_to='photos')
#    formatted_image = ImageSpecField(image_field='original_image', format='JPEG',
#        options={'quality': 90})
#    #    original_image = models.CharField(max_length=100)
#    #    formatted_image = models.CharField(max_length=100)
#    published = models.DateTimeField(auto_now_add=True)
#
#    def __unicode__(self):
#        return "%d"%self.id


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
#    content_date = models.DateField(blank=True,null=True)
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
        photopath = str(s3_storage.open(self.photo_original.name))  # this returns the full system path to the original file

        #custom handling of s3
#        url= "http://s3-eu-west-1.amazonaws.com/openiphotos/photos/"+self.photo_original.name
#
#        img_file = urllib.urlopen(url)
#        original_image = StringIO(img_file.read())
#        im = Image.open( original_image )

#        im = Image.open(photopath)  # open the image using PIL


        # pull a few variables out of that full path
        extension = photopath.rsplit('.', 1)[1]  # the file extension
        filename = photopath.rsplit('/', 1)[1].rsplit('.', 1)[0]  # the file name only (minus path or extension)
        fullpath = photopath.rsplit('/', 1)[0]  # the path only (minus the filename.extension)


        from s3fs import S3FS
        lol =  S3FS( "openiphotos","photos",'AKIAJWJD4LJWZ4PMCWTA','mwuo3YgUVrNoCW+XXvGr/Fk8YIpx+AmAZITMFX+L')

        picture = lol.open(filename+"."+extension)
        im = Image.open(picture)

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
        ordering = ['-created_at']


from athumb.fields import ImageWithThumbsField
from athumb.backends.s3boto import S3BotoStorage_AllPublic

# It is generally good to keep these stored in their own module, to allow
# for other models.py modules to import the values. This assumes that more
# than one model stores stuff in the same bucket.
PUBLIC_MEDIA_BUCKET = S3BotoStorage_AllPublic(bucket='openiphotos')

class YourModel(models.Model):
    photo_original = ImageWithThumbsField(
    upload_to="photos",
    thumbs=(
        ('50x50_cropped', {'size': (50, 50), 'crop': True}),
        ('60x60', {'size': (60, 60)}),
        ('80x1000', {'size': (80, 1000)}),
        ('front_page', {'size': (120, 1000)}),
        ('medium', {'size': (161, 1000)}),
        ('large', {'size': (200, 1000)}),
        ),
    blank=True, null=True,
    storage=PUBLIC_MEDIA_BUCKET)