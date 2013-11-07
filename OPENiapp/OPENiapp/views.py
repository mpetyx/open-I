__author__ = 'mpetyx'


from Objects.Photo.facebook import provider
from django.http import HttpResponse



def facebook_get_photos(request):

    connector = provider(access_token=request.token)

    photos = connector.get_photos()

    return HttpResponse(photos,status=201)