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

def make_connection(request):
    return provider(access_token=SocialToken.objects.filter(account__user=request.user.id, account__provider='facebook'))

def get_previous(photos):
    previous = photos['paging']['previous'].split('&since=')[1].split('&')[0]
    return 'since=' + previous
    
def get_next(photos):
    return 'until=' + photos['paging']['next'].split('&until=')[1]


def facebook_get_photos(request):
    connector = make_connection(request)
    photos = connector.get_photos()

    return render_to_response('fb-photos.html', {"result": photos, 'previous': get_previous(photos), 'next': get_next(photos)})


def facebook_get_photos_since(request, strDigit):
    connector = make_connection(request)

    digit = int(strDigit.split("since=")[1])
    photos = connector.get_photos_since(digit)

    if (photos['data'] == []):
        return render_to_response('no-photo.html')
    else:
        return render_to_response('fb-photos.html', {"result": photos, 'previous': get_previous(photos), 'next': get_next(photos)})


def facebook_get_photos_until(request, strDigit):
    connector = make_connection(request)

    digit = int(strDigit.split("until=")[1])
    photos = connector.get_photos_until(digit)

    if (photos['data'] == []):
        return render_to_response('no-photo.html')
    else:
        return render_to_response('fb-photos.html', {"result": photos, 'previous': get_previous(photos), 'next': get_next(photos)})