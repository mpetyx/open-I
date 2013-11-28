__author__ = 'mpetyx'

from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import  ALL, ALL_WITH_RELATIONS
from .models import OpeniPhoto

from OPENiapp.APIS.OpeniGenericResource import GenericResource


class PhotoResource(GenericResource):


    class Meta:
        queryset = OpeniPhoto.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'photo'
        authorization = DjangoAuthorization()
        filtering = {
            'slug': ALL,
            'user': ALL_WITH_RELATIONS,
            'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }


