__author__ = 'mpetyx'

import time
import string
import hashlib
from random import choice

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# from django.contrib.auth.models import User
import simplejson

import allauth

from OPENiapp.Providers import Login
from django.contrib.auth.models import User
# from OPENiapp.api.Responses import *
from OPENiapp.models import *
from LoggedUserResponse import profileJson

from OPENiapp.Providers.Facebook.SignIn import fb_complete_login2


@csrf_exempt
def facebook(request):
    """
    curl -v -X POST -d 'access_token=CAABptKWDIR0BAGNroFCrirAH7PhVZCpE2ztmUCES9ZAWbjVO3M4VdiHBIZCKcP5j66vGA7znefomEZBuK8UZCOjHKV0aE0A3T1OdInMB0ThEgInASGln0AEaE80AtmCzH8JZAfjnr6g9Tom9xrsZAKsywcChqp88tFzECnydq71FziDhqRccV8SWRzlylYUofpZBjIZA1manAHq03Nm4KGpIwPZC9I5kl3e2QZD' http://openi.herokuapp.com/person/signin/facebook
    curl -v -X POST -d 'access_token=CAABptKWDIR0BAGNroFCrirAH7PhVZCpE2ztmUCES9ZAWbjVO3M4VdiHBIZCKcP5j66vGA7znefomEZBuK8UZCOjHKV0aE0A3T1OdInMB0ThEgInASGln0AEaE80AtmCzH8JZAfjnr6g9Tom9xrsZAKsywcChqp88tFzECnydq71FziDhqRccV8SWRzlylYUofpZBjIZA1manAHq03Nm4KGpIwPZC9I5kl3e2QZD' http://127.0.0.1:8000/person/signin/facebook

    """
    # app = request.app
    # token = request.token

    access_token = request.POST.get('access_token', '')

    if access_token is '':
        return "wrong credentials"
    else:
    # try:
        user = fb_complete_login2(None, access_token)
        if type(user) == allauth.socialaccount.models.SocialLogin:
            user = User.objects.get(username=user.account.user.username)
        elif list(user) != []:
            user = user[0]
        else:
            user = None
            # except:
            #     user = None

    if user is not None:
        if user.is_active:
            # login(request, user)
            consumer, created = OAuthConsumer.objects.get_or_create(key=user.username, name=user.username,
                                                                    active=True)
            N = 32
            random_string = ''.join(choice(string.ascii_letters + string.digits) for x in range(N))
            secret_string = user.username + str(time.time()) + random_string
            consumer.secret = hashlib.sha1(secret_string.encode("UTF-8")).hexdigest()

            person = Person.objects.filter(user=user)[0]

            response = profileJson(person, person)
            response["authentication"] = {}
            response["authentication"]["key"] = consumer.key
            response["authentication"]["secret"] = consumer.secret

            response = simplejson.dumps(response)

            consumer.save()

            return HttpResponse(response)
        else:
            return HttpResponse({'error': 'Your account has been disabed'}, status=404)
    else:
        return HttpResponse(request, {'error': 'Failed to login. Please make sure you provided valid credentials.'},
                            status=401)


@csrf_exempt
def twitter(request):
    """
    example request
    curl -v -X POST -d 'access_token=95257276-yRoHvRIxvcNluK1cwurlhBuvS9QRtt4Z1VTw3sqA&access_token_secret=vCSMwCB8Y9s7FyoVP0qhuO3LWEka5dezxGYuN8gILRE' http://127.0.0.1:8000/person/signin/twitter
    curl -v -X POST -d 'access_token=95257276-yRoHvRIxvcNluK1cwurlhBuvS9QRtt4Z1VTw3sqA&access_token_secret=vCSMwCB8Y9s7FyoVP0qhuO3LWEka5dezxGYuN8gILRE' http://www.openi.com/person/signin/twitter

    @param request:
    @return:
    """
    access_token = request.POST.get('access_token', '')
    access_token_secret = request.POST.get('access_token_secret', '')

    if access_token is '' or access_token_secret is '':
        return "wrong credentials"
    else:
        user = Login.Twitter().authenticate(access_token=access_token, access_token_secret=access_token_secret)

    if user is not None:
        if user.is_active:
            # login(request, user)
            consumer, created = OAuthConsumer.objects.get_or_create(key=user.username, name=user.username,
                                                                    active=True)
            N = 32
            random_string = ''.join(choice(string.ascii_letters + string.digits) for x in range(N))
            secret_string = user.username + str(time.time()) + random_string
            consumer.secret = hashlib.sha1(secret_string.encode("UTF-8")).hexdigest()

            person = Person.objects.filter(user=user)[0]

            response = profileJson(person, person)
            response["authentication"] = {}
            response["authentication"]["key"] = consumer.key
            response["authentication"]["secret"] = consumer.secret

            response = simplejson.dumps(response)

            consumer.save()

            return HttpResponse(response)
        else:
            return HttpResponse({'error': 'Your account has been disabed'}, status=404)
    else:
        return HttpResponse(request, {'error': 'Failed to login. Please make sure you provided valid credentials.'},
                            status=401)
