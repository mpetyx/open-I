__author__ = 'mpetyx'

from tastypie.resources import ModelResource
from tastypie.bundle import Bundle
from django.core.exceptions import ObjectDoesNotExist




class GenericResource(ModelResource):

    def applications_asked(self, bundle):

        return 1

    def http_headers_in_request(self, bundle):

        return 1

    def request_method(self, bundle):

        return bundle.request.method()

    def dehydrate(self, bundle):
        """
        A hook to allow a final manipulation of data once all fields/methods
        have built out the dehydrated data.

        Useful if you need to access more than one dehydrated field or want
        to annotate on additional data.

        Must return the modified bundle.
        """

        smConnectors  = ['facebook','twitter']

        apps = ['app1','app2']

        for connector in smConnectors:

            res = {}

            for app in apps:

                res[app] = { 'test':True}

            bundle.data[connector] = res

        bundle.data["koukli"] = {"lol":1}

        return bundle
