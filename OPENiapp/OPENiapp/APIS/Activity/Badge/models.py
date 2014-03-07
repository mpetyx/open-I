__author__ = 'mpetyx'


from django.db import models


class OpeniBadge(models.Model):
    # id is missing because it is the default
    url = models.TextField()
    object_type = models.TextField()
    service = models.TextField()
    From = models.TextField()
    place = models.TextField()
    duration = models.TextField()
    title = models.TextField()
    description = models.TextField()
    picture = models.TextField()
