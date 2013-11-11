__author__ = 'mpetyx'


from Objects.Photo.facebook import provider
from django.http import HttpResponse



def facebook_get_photos(request):

    access_token = request.GET.get("access_token","")

    connector = provider(access_token=access_token)

    photos = connector.get_photos()

    return HttpResponse(photos,status=201)