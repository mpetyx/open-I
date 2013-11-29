__author__ = 'mpetyx'

from django.db import models


class OpeniFile(models.Model):
    # id is missing because it is the default
    url = models.TextField()
    object_type = models.TextField()
    service = models.TextField()
    From = models.TextField() #a set of properties defining the owner of the object (account)
    profile = models.TextField()
    location = models.TextField()
    time = models.TextField()
    tags = models.TextField()
    width = models.TextField()
    height = models.TextField()