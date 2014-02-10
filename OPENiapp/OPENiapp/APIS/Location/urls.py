__author__ = 'mpetyx'

from tastypie.api import Api

from .Event.Resources import EventResource



api = Api(api_name='location')
api.register(EventResource())


urlpatterns = api.urls
