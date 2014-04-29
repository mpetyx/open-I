
__author__ = 'mpetyx'

from django.db import models
from OPENiapp.APIS.Context.models import OpeniContextAwareModel

__all__ = ["OpeniPhoto",]
class OpeniPhoto(OpeniContextAwareModel):
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

    class Meta:
        app_label = "OPENiapp"