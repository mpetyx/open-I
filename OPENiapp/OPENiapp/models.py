'''
Created on Oct 24, 2013

@author: mpetyx
'''

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from OPENiapp.APIS.Context.models import OpeniContext
from OPENiapp.APIS.Media.Article.models import OpeniArticle


class Person(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=255, null=True, default='', blank=True)
    surname = models.CharField(max_length=255, null=True, default='', blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    birthday = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)
    phonenumber = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True)
    #the correct photo id is 1095


    class Admin:
        pass

    #    def getImage(self):
    #        return "<img src='%s' width=97 height=72/>" % self.photo.url
    #
    #    getImage.allow_tags = True


    def __unicode__(self):
        return "%d <-> %s" % (self.id, self.user.username)

    def full_name(self):
        return " %s %s" % (self.user.first_name, self.user.last_name)


class OAuthConsumer(models.Model):
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "api_oauth_consumer"

    def __unicode__(self):
        return u'%s' % (self.name)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = Person.objects.get_or_create(user=instance)


post_save.connect(create_user_profile, sender=User)