__author__ = 'mpetyx'

import time
import string
import hashlib
from random import choice

from django.contrib.auth import authenticate, login
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.http import HttpForbidden, HttpCreated, HttpConflict
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
import simplejson
from django.contrib.auth.models import User

from OPENiapp.api.Responses import *
from OPENiapp.models import *
from OPENiapp.api.v2 import *
from OPENiapp import models
from ..Person.Profile import profileJson


@csrf_exempt
def signin(request):
    if request.method == "POST":
        # Per https://docs.djangoproject.com/en/1.3/topics/auth/#django.contrib.auth.login...
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if '@' in username:
            username = User.objects.get(email=username).username
            user = authenticate(username=username, password=password)
        else:
            user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                consumer, created = OAuthConsumer.objects.get_or_create(key=user.username, name=user.username,
                                                                        active=True)
                N = 32
                random_string = ''.join(choice(string.ascii_letters + string.digits) for x in range(N))
                secret_string = user.username + str(time.time()) + random_string
                consumer.secret = hashlib.sha1(secret_string.encode("UTF-8")).hexdigest()

                person = models.Person.objects.filter(user=user)[0]

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
    else:
        return HttpResponse(status=405)


@csrf_exempt
def signup(request):
    try:
        username = request.POST.get("username")
        mail = request.POST.get("mail")
        password = request.POST.get("password")
        salt = 'predefined_key' # Possibly version specific?
        random_str = request.POST.get('skey')[:14]
        security_key = salt + hashlib.sha1(mail[::-1]).hexdigest().upper() + username.upper() + hashlib.sha1(
            hashlib.md5(password).hexdigest().upper()).hexdigest().upper()
        security_key = hashlib.sha1(random_str + security_key).hexdigest().upper() + '-' + hashlib.md5(
            security_key + random_str[::-1]).hexdigest().upper()
        security_key = security_key[:-1]
        security_key = random_str + security_key + "."

        skey = request.POST.get("skey")

        if skey == security_key:

            # Check if the user already exists
            existing = User.objects.filter(username__iexact=request.POST.get('username'))
            existing_mail = User.objects.filter(email__iexact=request.POST.get('mail'))
            if existing.exists():
                raise IntegrityError()
            elif existing_mail.exists():
                raise IntegrityError()
            else:
                temp = True
                try:
                    user_check = User.objects.get(username=request.POST.get('username'))
                except:
                    temp = False

            if temp == True:
                raise IntegrityError()

            user = User.objects.create_user(request.POST.get('username'), request.POST.get('mail'),
                                            request.POST.get('password'))
            user.groups.add(1)
            current_id = user.id
            user.save()

            person = Person.objects.get(user=user)

            from mailsnake import MailSnake

            mandrill = MailSnake('MshPu_5BxMs40_usJijM9Q', api='mandrill')

            message = {
                'subject': 'Welcome to openi',
                'to': [{'email': request.POST.get('mail')}],
                'from_name': 'openi',
                'from_email': 'contact@openi.com',
            }

            content = [{'name': 'content1', 'content': '<p>email body</p>'}]
            mandrill.messages.send_template(template_name='signup', message=message, template_content=content)

            raise ImmediateHttpResponse(
                openiResponse({'username': request.POST.get('username'), 'user_id': current_id}, HttpCreated))
        else:
            raise ImmediateHttpResponse(
                openiResponse({'error': 'The specified key could not be verified.'}, HttpForbidden))
    except IntegrityError:
        raise ImmediateHttpResponse(openiResponse({'error': 'Username or Email is already in-use'}, HttpConflict))
