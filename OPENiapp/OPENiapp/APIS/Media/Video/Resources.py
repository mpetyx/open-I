__author__ = 'mpetyx'

from tastypie.authorization import DjangoAuthorization
from .models import OpeniVideo

from OPENiapp.APIS.OpeniGenericResource import GenericResource


class VideoResource(GenericResource):
    class Meta:
        queryset = OpeniVideo.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'video'
        authorization = DjangoAuthorization()
        # filtering = {
        #     'slug': ALL,
        #     'user': ALL_WITH_RELATIONS,
        #     'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        # }