from OPENiapp.APIS.Context.models import OpeniContextAwareModel
from OPENiapp.APIS.Context.models import OpeniContext

__author__ = 'mpetyx'


from django.db import models

__all__ = ["OpeniArticle",]
class OpeniArticle(OpeniContextAwareModel):
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
    class Meta:
        app_label = "OPENiapp"
