__author__ = 'mpetyx'

import python_rest_handler
from python_rest_handler import DataManager

from tastypie.resources import ModelResource
from tastypie.authorization import Authorization

from django.contrib.auth.models import User




class Handler(object, python_rest_handler.RestRequestHandler):
    """
    this is implemented following https://github.com/paulocheque/python-rest-handler
    """

    data_manager = DataManager

    def raise403(self): pass
    def raise404(self): pass
    def get_request_uri(self): pass
    def get_request_data(self): return {}
    def render(self, template_name, **kwargs): pass
    def redirect(self, url, permanent=False, status=None, **kwargs): pass


    def get(self, instance_id=None, edit=False): # or other method here
        # next line is the required link
        return self.rest_handler.get(instance_id=instance_id, edit=edit)

    def post(self, instance_id=None, action=None): # or other method here
        # next line is the required link
        return self.rest_handler.post(instance_id=instance_id, action=action)

    def put(self, instance_id): # or other method here
        # next line is the required link
        return self.rest_handler.put(instance_id=instance_id)

    def delete(self, instance_id): # or other method here
        # next line is the required link
        return self.rest_handler.delete(instance_id=instance_id)

class DjangoHandler(ModelResource):

    class Meta:
        resource_name = 'users'
        queryset = User.objects.all()
        authorization = Authorization()
