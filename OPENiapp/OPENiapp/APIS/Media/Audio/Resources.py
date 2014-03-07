__author__ = 'mpetyx'

from tastypie.authorization import DjangoAuthorization
from .models import OpeniAudio

from OPENiapp.APIS.OpeniGenericResource import GenericResource
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

class AudioResource(GenericResource):
    class Meta:
        queryset = OpeniAudio.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'audio'
        authentication = Authentication()
        authorization = Authorization()
        # filtering = {
        #     'slug': ALL,
        #     'user': ALL_WITH_RELATIONS,
        #     'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        # }