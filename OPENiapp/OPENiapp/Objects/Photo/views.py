__author__ = 'romdim'

from Facebook.views import *
from Twitter.views import *
from photo_form import PhotoForm

def photo_choose_media(request):
    """ Post a Photo to Different Social Services """
    if request.method == 'POST': # If the form has been submitted...
        form = PhotoForm(request.POST) # A form bound to the POST data

        fb_post = None
        tw_post = None

        facebook = request.GET.get("facebook")
        if form.is_valid():
            if form.cleaned_data['facebook']:
                fbconnector = make_fb_connection(request)
                fbconnector.post_photo(form.cleaned_data['path'])
                fb_post = True

            if form.cleaned_data['twitter']:
                twconnector = make_tw_connection(request, 'Twitter')
                twconnector.post_photo(form.cleaned_data['path'])
                tw_post = True

            #     access_token=SocialToken.objects.filter(account__user=request.user.id, account__provider='twitter')
            #     if access_token is []:
            #
            #     else:
            #         token = access_token[0].token
            #         token_secret = access_token[0].token_secret
            #         # access_token=SocialToken.objects.filter(account__user=2, account__provider='twitter')
            #         post_on_twitter
            if (fb_post and tw_post):
                return render_to_response('posted_to_both.html')
            elif (fb_post):
                return render_to_response('posted_to_fb.html')
            elif (tw_post):
                return render_to_response('posted_to_tw.html')
            elif (not form.cleaned_data['facebook'] and not  form.cleaned_data['twitter']):
                return render_to_response('check_one_box.html')
            else:
                return render_to_response('something_wrong.html')
    else:
        form = PhotoForm()
        return render(request, 'post-photo.html', {
            'form': form,
        })
