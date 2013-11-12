__author__ = 'mpetyx'


from Objects.Photo.facebook import provider
from django.http import HttpResponse

# Romanos' implementation
from allauth.socialaccount.models import SocialToken
from django.shortcuts import render_to_response


#def facebook_get_photos(request):

#    connector = provider(access_token=request.token)

#    photos = connector.get_photos()

#    return HttpResponse(photos,status=201)


def facebook_get_photos(request, strDigit):

    #from facepy import GraphAPI

    #graph = GraphAPI(SocialToken.objects.filter(account__provider='facebook'))
    #result = graph.get('me/photos', limit=10)
    #access_token = request.GET.get("access_token","")
    connector = provider(access_token=SocialToken.objects.filter(account__user=request.user.id, account__provider='facebook'))
    if strDigit == "/" or strDigit == None :
        photos = connector.get_photos()
    else :
        digit = int(strDigit.split("/")[1])
        photos = connector.get_photos(digit)
    previous = '/' + photos['paging']['previous'].split('&since=')[1].split('&')[0]
    next = '/' + photos['paging']['next'].split('&until=')[1]
    return render_to_response('fb-photos.html', {"result": photos, 'previous': previous, 'next': next})