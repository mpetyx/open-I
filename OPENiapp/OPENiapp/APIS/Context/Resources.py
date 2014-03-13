from django.conf.urls import url
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
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
    pass


class ContextResource(GenericResource):

    class Meta:
        queryset = OpeniContext.objects.all().prefetch_related("group_set","locationvisit_set")

    def dehydrate(self,bundle):
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
    # def prepend_urls(self):
    #     print("hello")
    #     return [
    #         url(r"^(?P<resource_name>%s)/(?P<pk>\w[\w/-]*)/location%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_location'), name="api_get_location"),
    #     ]
    #
    # def get_location(self, request, **kwargs):
    #     print("hello 2")
    #     try:
    #         bundle = self.build_bundle(data={'pk': kwargs['pk']}, request=request)
    #         obj = self.cached_obj_get(bundle=bundle, **self.remove_api_resource_names(kwargs))
    #         return self.create_response()
    #         return {}
    #     except ObjectDoesNotExist:
    #         return HttpGone()
    #     except MultipleObjectsReturned:
    #         return HttpMultipleChoices("More than one resource is found at this URI.")
