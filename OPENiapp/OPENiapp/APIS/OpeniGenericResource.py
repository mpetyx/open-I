__author__ = 'mpetyx'

from OPENiapp.APIS.Context.BaseResource import ContextAwareResource

from django.http import HttpResponse
from django.shortcuts import render
import ast

from allauth.socialaccount.models import SocialToken

from django.contrib.auth.models import User

from OPENiapp.Providers.generic import execution

from django.conf.urls import url
from tastypie.utils import trailing_slash
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

class GenericResource(ContextAwareResource):
    def applications_asked(self, bundle):

        return 1

    def http_headers_in_request(self, bundle):

        return 1

    def request_method(self, bundle):

        return bundle.request.method()

    def dehydrate(self, bundle):
    #    """
    #    A hook to allow a final manipulation of data once all fields/methods
    #    have built out the dehydrated data.

    #    Useful if you need to access more than one dehydrated field or want
    #    to annotate on additional data.

    #    Must return the modified bundle.
    #    """
    #    if bundle.request.method == 'POST': # If the form has been submitted...
    #        # form = PhotoForm(bundle.request.POST) # A form bound to the POST data

    #        json_return_fb_photo_post = None
    #        json_return_tw_photo_post = None

    #        facebook = bundle.request.GET.get("facebook")
    #        path = bundle.request.GET.get("path")

    #        if facebook == true:
    #            fbconnector = make_fb_connection(bundle.request)
    #            json_return_fb_photo_post = fbconnector.post_photo(path)
    #        #if form.is_valid():
    #        #    if form.cleaned_data['facebook']:
    #        #        fbconnector = make_fb_connection(bundle.request)
    #        #        json_return_fb_photo_post = fbconnector.post_photo(form.cleaned_data['path'])

    #        #    if form.cleaned_data['twitter']:
    #        #        twconnector = make_tw_connection(bundle.request, 'Twitter')
    #        #        json_return_tw_photo_post = twconnector.post_photo(form.cleaned_data['path'])

    #        #    if json_return_fb_photo_post is None:
    #        #        json_return_fb_photo_post = {}
    #        #    if json_return_tw_photo_post is None:
    #        #        json_return_tw_photo_post = {}

    #            response_data = {}
    #            response_data['fb'] = json_return_fb_photo_post
    #            response_data['tw'] = json_return_tw_photo_post

    #            bundle.data["apantisi"] = response_data

    #            print bundle
    #            print bundle.data["apantisi"]

    #            return bundle
            
    #            # return response_data
    #            # return HttpResponse(json.dumps(response_data, sort_keys=True, indent=4), content_type="application/json")

    #    else:
    #        #form = PhotoForm()
    #        #return render(bundle.request, 'post-photo.html', {
    #        #    'form': form,
    #        #})

    #        smConnectors = ['facebook', 'twitter']

    #        apps = ['app1', 'app2']

    #        for connector in smConnectors:

    #            res = {}

    #            for app in apps:
    #                res[app] = {'test': True}

    #            bundle.data[connector] = res

    #        bundle.data["koukli"] = {"lol": 1}

        return bundle
    
    def get_list(self, request, **kwargs):
        """
        Returns a serialized list of resources.

        Calls ``obj_get_list`` to provide the data, then handles that result
        set and serializes it.

        Should return a HttpResponse (200 OK).
        """
        try:
            user = request.GET.get("user")
            u = User.objects.filter(username=user)

            apps = ast.literal_eval(request.GET.get("apps"))
            method = request.GET.get("method")
            data = ast.literal_eval(request.GET.get("data"))
        except:
            return 1

        if (user and apps and method and data):
            #executable = execution(u, [{"cbs": "instagram", "app_name": "OPENi"}], "get_a_photo", {"media_id": "628147512937366504_917877895"})
            #executable = execution(u, [{"cbs": "instagram", "app_name": "OPENi"}], "get_all_photos_for_account", {"account_id": "917877895"})
            #executable = execution(u, [{"cbs": "foursquare", "app_name": "OPENi"}], "get_user", {})
            #executable = execution(u, [{"cbs": "facebook", "app_name": "OPENi"}], "get_an_event", {"event_id": "577733618968497"})
            #executable = execution(u, [{"cbs": "facebook", "app_name": "OPENi"}], "get_all_events_for_account", {"account_id": "1266965453"})
            #executable = execution(u, [{"cbs": "facebook", "app_name": "OPENi"}], "post_event_to_account", {"account_id": "me", 'name': 'kati', 'start_time': '2014-01-24T23:30:00+0200'})
            #executable = execution(u, [{"cbs": "facebook", "app_name": "OPENi"}], "edit_an_event", {"event_id": "235785719933823", 'name': 'kati_allo', 'start_time': '2014-01-24T23:30:00+0200'})
            #executable = execution(u, [{"cbs": "facebook", "app_name": "OPENi"}], "delete_an_event", {"event_id": "235785719933823"})
            executable = execution(u, apps, method, data)
            
            result = executable.make_all_connections()
            return self.create_response(request, result)
        
        # Default actions down here, for get_list (that is if there is no fb or other CBS request!
        base_bundle = self.build_bundle(request=request)
        objects = self.obj_get_list(bundle=base_bundle, **self.remove_api_resource_names(kwargs))
        sorted_objects = self.apply_sorting(objects, options=request.GET)

        paginator = self._meta.paginator_class(request.GET, sorted_objects, resource_uri=self.get_resource_uri(), limit=self._meta.limit, max_limit=self._meta.max_limit, collection_name=self._meta.collection_name)
        to_be_serialized = paginator.page()

        # Dehydrate the bundles in preparation for serialization.
        bundles = []

        for obj in to_be_serialized[self._meta.collection_name]:
            bundle = self.build_bundle(obj=obj, request=request)
            bundles.append(self.full_dehydrate(bundle, for_list=True))

        to_be_serialized[self._meta.collection_name] = bundles
        to_be_serialized = self.alter_list_data_to_serialize(request, to_be_serialized)
        return self.create_response(request, to_be_serialized)

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/generic%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_list'), name="generic"),
        ]

class GenericMeta:
    list_allowed_methods = ['get', 'post']
    detail_allowed_methods = ['get', 'post', 'put', 'delete']
    authentication = Authentication()
    authorization = Authorization()
    # filtering = {
    #     'slug': ALL,
    #     'user': ALL_WITH_RELATIONS,
    #     'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
    # }


    extra_actions = [

        {
            "name": "generic",
            "http_method": "GET",
            "resource_type": "list",
            "description": "Apply Method",
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
                    "description": "Method needed"
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