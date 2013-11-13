__author__ = 'mpetyx'

from Objects.Photo.facebook import provider
from Objects.Photo.photo_form import PhotoForm

# Romanos' implementation
from allauth.socialaccount.models import SocialToken
from django.shortcuts import render_to_response, render, redirect


# me/photos Implementation
def make_connection(request):
    return provider(
        access_token=SocialToken.objects.filter(account__user=request.user.id, account__provider='facebook'))


def get_previous(photos):
    return 'since=' + photos['paging']['previous'].split('&since=')[1].split('&')[0]


def get_next(photos):
    return 'until=' + photos['paging']['next'].split('&until=')[1]


def photo_choose_media(request):
    return 1


def facebook_get_photos(request):
    connector = make_connection(request)
    photos = connector.get_photos()

    return render_to_response('fb-photos.html',
                              {"result": photos, 'previous': get_previous(photos), 'next': get_next(photos)})


def facebook_get_photos_since(request, strDigit):
    connector = make_connection(request)

    digit = int(strDigit.split("since=")[1])
    photos = connector.get_photos_since(digit)

    if (photos['data'] == []):
        return render_to_response('no-photo.html')
    else:
        return render_to_response('fb-photos.html',
                                  {"result": photos, 'previous': get_previous(photos), 'next': get_next(photos)})


def facebook_get_photos_until(request, strDigit):
    connector = make_connection(request)

    digit = int(strDigit.split("until=")[1])
    photos = connector.get_photos_until(digit)

    if (photos['data'] == []):
        return render_to_response('no-photo.html')
    else:
        return render_to_response('fb-photos.html',
                                  {"result": photos, 'previous': get_previous(photos), 'next': get_next(photos)})


# Album Implementation
def get_before(photos):
    return photos['paging']['cursors']['before']


def get_after(photos):
    return photos['paging']['cursors']['after']


def facebook_post_photos(request):
    if request.method == 'POST': # If the form has been submitted...
        form = PhotoForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            connector = make_connection(request)
            connector.post_photo(form.cleaned_data['path'])
            photos = connector.get_album_photos()

            return redirect('facebook_get_album_photos')
            #return render_to_response('fb-album.html', {"result": photos, 'previous': get_before(photos), 'next': get_after(photos)})
    else:
        form = PhotoForm()
        return render(request, 'post-photo.html', {
            'form': form,
        })


def facebook_get_album_photos(request):
    connector = make_connection(request)
    photos = connector.get_album_photos()

    if not photos:
        return render_to_response('no-photo.html')
    else:
        previous = get_before(photos)
        next = get_after(photos)

        return render_to_response('fb-album.html', {"result": photos, 'previous': previous, 'next': next})


def facebook_get_photos_before(request, str):
    connector = make_connection(request)

    if not "before=" in str:
        return render_to_response('no-photo.html')
    else:
        str = int(str.split("before=")[1])
        photos = connector.get_album_photos_before(str)

        if (photos['data'] == []):
            return render_to_response('no-photo.html')
        else:
            return render_to_response('fb-album.html',
                                      {"result": photos, 'previous': get_before(photos), 'next': get_after(photos)})


def facebook_get_photos_after(request, str):
    connector = make_connection(request)

    if not "after=" in str:
        return render_to_response('no-photo.html')
    else:
        str = int(str.split("after=")[1])
        photos = connector.get_album_photos_after(str)

        if (photos['data'] == []):
            return render_to_response('no-photo.html')
        else:
            return render_to_response('fb-album.html',
                                      {"result": photos, 'previous': get_before(photos), 'next': get_after(photos)})