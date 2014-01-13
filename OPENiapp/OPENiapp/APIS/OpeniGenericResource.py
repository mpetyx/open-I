__author__ = 'mpetyx'

from tastypie.resources import ModelResource

from OPENiapp.Objects.Photo.post_form import PhotoForm
from django.http import HttpResponse
from django.shortcuts import render

from OPENiapp.Providers.Facebook.connector import provider as FBprovider
from allauth.socialaccount.models import SocialToken

from OPENiapp.Providers.generic import execution


class GenericResource(ModelResource):
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
        
    def make_fb_connection(self, user):
        """ Use facepy to make a Graph API call """
        return FBprovider(
            access_token=SocialToken.objects.filter(account__user=user.id, account__provider='facebook'))
    
    def get_list(self, request, **kwargs):
        """
        Returns a serialized list of resources.

        Calls ``obj_get_list`` to provide the data, then handles that result
        set and serializes it.

        Should return a HttpResponse (200 OK).
        """

        if (request.GET.get("newway") == "on"):
            executable = execution(request.user, [{"cbs": "instagram", "app_name": "OPENi"}], "get_a_photo", {"media_id": "628147512937366504_917877895"})
            #executable = execution(request.user, [{"cbs": "instagram", "app_name": "OPENi"}], "get_all_photos_for_account", {"account_id": "917877895"})
            result = executable.make_all_connections()
            return self.create_response(request, result)

        # TODO: Uncached for now. Invalidation that works for everyone may be
        #       impossible.
        if (request.GET.get("facebook") == 'on'):
            fbconnector = self.make_fb_connection(request.user)
            limit = 1
            if request.GET.get("limit"):
                limit = int(request.GET.get("limit"))
            photos = fbconnector.get_photos(limit)
            result = { "meta": 
                        {
                         "limit": limit,
                         "total_count": len(photos["data"]),
                         },
                       "obj" : [] }
            for photo in photos["data"]:
                if "name" in photo:
                    name = photo["name"]
                else:
                    name = ""
                if "place" in photo:
                    location = photo["place"]
                else:
                    location = ""
                result["obj"].append({
                                "objectType": "photo",
                                "service":"openi",
                                "id": photo["id"],
                                "url": photo["source"],
                                "profile":{
                                    "title": name,
                                    "description": "Doesn't Exist",
                                    "format": "Doesn't Exist",
                                    "size": "Doesn't Exist - Various Sizes"
                                },
                                "properties":{
                                    "width": photo["width"],
                                    "height": photo["height"],
                                    "tags" : location
                                }
                            })
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
