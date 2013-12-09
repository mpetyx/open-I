__author__ = 'romdim'

from Facebook.views import *
from Twitter.views import *
from photo_form import PhotoForm

import json
from django.http import HttpResponse

def photo_choose_media(request):
    """ Post a Photo to Different Social Services """
    if request.method == 'POST': # If the form has been submitted...
        form = PhotoForm(request.POST) # A form bound to the POST data

        json_return_fb_photo_post = None
        json_return_tw_photo_post = None

        facebook = request.GET.get("facebook")
        if form.is_valid():
            if form.cleaned_data['facebook']:
                fbconnector = make_fb_connection(request)
                json_return_fb_photo_post = fbconnector.post_photo(form.cleaned_data['path'])

            if form.cleaned_data['twitter']:
                twconnector = make_tw_connection(request, 'Twitter')
                json_return_tw_photo_post = twconnector.post_photo(form.cleaned_data['path'])

            if json_return_fb_photo_post is None:
                json_return_fb_photo_post = {}
            if json_return_tw_photo_post is None:
                json_return_tw_photo_post = {}

            response_data = {}
            response_data['fb'] = json_return_fb_photo_post
            response_data['tw'] = json_return_tw_photo_post
            
            # return response_data
            return HttpResponse(json.dumps(response_data, sort_keys=True, indent=4), content_type="application/json")

    else:
        form = PhotoForm()
        return render(request, 'post-photo.html', {
            'form': form,
        })
