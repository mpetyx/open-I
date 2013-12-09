__author__ = 'mpetyx'

from tastypie.authorization import DjangoAuthorization
from .models import OpeniAudio

from OPENiapp.APIS.OpeniGenericResource import GenericResource


class AudioResource(GenericResource):
    class Meta:
        queryset = OpeniAudio.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'audio'
        authorization = DjangoAuthorization()
        # filtering = {
        #     'slug': ALL,
        #     'user': ALL_WITH_RELATIONS,
        #     'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        # }