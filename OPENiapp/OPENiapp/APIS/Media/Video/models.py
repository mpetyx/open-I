
__author__ = 'mpetyx'

from django.db import models
from OPENiapp.APIS.Context.models import OpeniContextAwareModel


class OpeniVideo(OpeniContextAwareModel):
    # id is missing because it is the default
    url = models.TextField()
    object_type = models.TextField()
    service = models.TextField()
    From = models.TextField()
    profile = models.TextField()
    location = models.TextField()
    time = models.TextField()
    tags = models.TextField()
    width = models.TextField()
    height = models.TextField()