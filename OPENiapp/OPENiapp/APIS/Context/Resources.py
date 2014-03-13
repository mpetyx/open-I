from django.conf.urls import url
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from tastypie import fields
from tastypie.http import HttpGone, HttpMultipleChoices
from tastypie.resources import Resource
from tastypie.utils import trailing_slash
from .models import OpeniContext, Person
from OPENiapp.APIS.OpeniGenericResource import GenericResource

__author__ = 'amertis'
def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]
from django.forms.models import model_to_dict
class LocationResource(Resource):

    def get_list(self,request, **kwargs):
        base_bundle = self.build_bundle(request=request)
        locations = OpeniContext.objects.all().values('location_latitude','location_longitude','location_height')
        if len(locations) > 0:
            base_bundle.data['location'] = locations[0]
        return self.create_response(request, base_bundle)

class ContextResource(GenericResource):

    class Meta:
        queryset = OpeniContext.objects.all().prefetch_related("group_set","locationvisit_set")
        location = fields.DictField()
        extra_actions = [
            {
                "name": "location",
                "http_method": "GET",
                "description": "Get context location of an object",
                "fields": {
                }
            }
        ]

    def prepend_urls(self):
        print("hello")
        return [
              url(r"^(?P<resource_name>%s)/(?P<pk>\d+)/location%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_location'), name="api_get_location"),
        ]
    def dehydrate(self,bundle):
        bundle.data['location'] = {
            'location_longitude': bundle.data['location_longitude'],
            'location_latitude':bundle.data['location_latitude'],
            'location_height':bundle.data['location_height']
        }
        del bundle.data['location_longitude']
        del bundle.data['location_latitude']
        del bundle.data['location_height']
        location_visits = bundle.obj.locationvisit_set.values()
        location_visits_list = ValuesQuerySetToDict(location_visits)
        groups = bundle.obj.group_set.values()
        groups_list = ValuesQuerySetToDict(groups)
        group_ids = []
        for group in groups_list:
            group['persons'] = []
            group_ids.append(group['id'])
        if len(group_ids) > 0:
            persons = Person.objects.filter(group__in = group_ids).order_by("group").values()
            persons_list = ValuesQuerySetToDict(persons)
            for group in groups_list:
                for person in persons_list:
                    if group['id'] == person['group_id']:
                        group['persons'].append(person)
        bundle.data['groups'] = groups_list
        bundle.data['location_visits'] = location_visits_list
        return bundle

    def get_location(self, request, **kwargs):
        child_resource = LocationResource()
        return child_resource.get_list(request)


