__author__ = 'mpetyx'

from tastypie.authorization import DjangoAuthorization
from .models import OpeniFile

from OPENiapp.APIS.OpeniGenericResource import GenericResource


class FileResource(GenericResource):
    class Meta:
        queryset = OpeniFile.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'file'
        authorization = DjangoAuthorization()
        # filtering = {
        #     'slug': ALL,
        #     'user': ALL_WITH_RELATIONS,
        #     'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        # }