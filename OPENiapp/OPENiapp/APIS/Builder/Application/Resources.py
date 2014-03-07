__author__ = 'mpetyx'

from tastypie.authorization import DjangoAuthorization
from .models import OpeniAudio

from OPENiapp.APIS.OpeniGenericResource import GenericResource
from OPENiapp.APIS.Authorization import Authorization
from OPENiapp.APIS.Authentication import Authentication

from allauth.socialaccount.models import SocialApp


class CBSResource(GenericResource):
    class Meta:
        queryset = SocialApp.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'cbsconnector'
        authentication = Authentication()
        authorization = Authorization()
        # filtering = {
        #     'slug': ALL,
        #     'user': ALL_WITH_RELATIONS,
        #     'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        # }