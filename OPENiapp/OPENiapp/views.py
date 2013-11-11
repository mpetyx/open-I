__author__ = 'mpetyx'


from Objects.Photo.facebook import provider
from django.http import HttpResponse

# Romanos' implementation
from allauth.socialaccount.models import SocialToken, SocialAccount
from django.shortcuts import render_to_response


#def facebook_get_photos(request):

#    connector = provider(access_token=request.token)

#    photos = connector.get_photos()

#    return HttpResponse(photos,status=201)


def facebook_get_photos(request):

    #from facepy import GraphAPI

    #graph = GraphAPI(SocialToken.objects.filter(account__provider='facebook'))
    #result = graph.get('me/photos', limit=10)
    #access_token = request.GET.get("access_token","")
    connector = provider(access_token=SocialToken.objects.filter(account__user=request.user.id, account__provider='facebook'))
    photos = connector.get_photos()
    return render_to_response('fb-photos.html', {"result": photos})