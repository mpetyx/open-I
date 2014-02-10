__author__ = 'mpetyx'


from tastypie.authorization import DjangoAuthorization
from .models import OpeniEvent

from OPENiapp.APIS.OpeniGenericResource import GenericResource


class EventResource(GenericResource):
    class Meta:
        queryset = OpeniEvent.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'event'
        authorization = DjangoAuthorization()
        # filtering = {
        #     'slug': ALL,
        #     'user': ALL_WITH_RELATIONS,
        #     'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        # }


        extra_actions = [
            {
                "name": "search",
                "http_method": "GET",
                "resource_type": "list",
                "description": "Seach endpoint",
                "fields": {
                    "q": {
                        "type": "string",
                        "required": True,
                        "description": "Search query terms"
                    }
                }
            },

            {
                "name": "get fb event",
                "http_method": "GET",
                "resource_type": "list",
                "description": "facebook event",
                "fields": {
                    "q": {
                        "type": "string",
                        "required": True,
                        "description": "retrieve fb event"
                    }
                }
            }
        ]