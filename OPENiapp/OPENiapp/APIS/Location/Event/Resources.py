__author__ = 'mpetyx'

from django.conf.urls import url
from tastypie.utils import trailing_slash
from tastypie.authorization import DjangoAuthorization
from .models import OpeniEvent

from OPENiapp.APIS.OpeniGenericResource import GenericResource
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

class EventResource(GenericResource):
    class Meta:
        queryset = OpeniEvent.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'event'
        authentication = Authentication()
        authorization = Authorization()
        # filtering = {
        #     'slug': ALL,
        #     'user': ALL_WITH_RELATIONS,
        #     'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        # }


        extra_actions = [

            {
                "name": "get_an_event",
                "http_method": "GET",
                "resource_type": "list",
                "description": "Get an Event",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": True,
                        "description": "The user required for this action"
                    },
                    "apps": {
                        "type": "string",
                        "required": True,
                        "description": "The CBS along with the App we want to do a request to"
                    },
                    "method": {
                        "type": "string",
                        "required": True,
                        "description": "Get an Event"
                    },
                    "data": {
                        "type": "string",
                        "required": True,
                        "description": "The required data"
                    },
                }
            },

            {
                "name": "comments",
                "http_method": "GET",
                "resource_type": "list",
                "description": "comments from CBS",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": True,
                        "description": "list of selected CBS"
                    }
                }
            },

            {
                "name": "likes",
                "http_method": "GET",
                "resource_type": "list",
                "description": "likes from CBS",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": True,
                        "description": "list of selected CBS"
                    }
                }
            },

            {
                "name": "dislikes",
                "http_method": "GET",
                "resource_type": "list",
                "description": "dislikes from CBS",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": True,
                        "description": "list of selected CBS"
                    }
                }
            }
        ]

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/get_an_event%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_an_event'), name="get_an_event"),
        ]

    def get_an_event(self, request, **kwargs):
        return self.get_list(request)