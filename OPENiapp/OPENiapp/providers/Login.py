__author__ = 'mpetyx'

from django.conf import settings
from django.contrib.auth.models import User
from django.test import RequestFactory

from allauth.account.utils import send_email_confirmation
import allauth
from twitter.SignIn import openiTwitterAdapter



#useful functions to complete signin/up


def login(request, user):
    mail = send_email_confirmation(request=request, user=user, signup=False)


# http://justcramer.com/2008/08/23/logging-in-with-email-addresses-in-django/
# http://www.micahcarrick.com/django-email-authentication.html
class EmailOrUsernameModelBackend(object):
    def authenticate(self, username=None, password=None):
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class AppTwitter():
    def __init__(self, secret, client_id):
        self.secret = secret
        self.client_id = client_id
        self.provide = "twitter"
        self.name = "openi"


class AppFacebook():
    def __init__(self, secret, client_id):
        self.secret = secret
        self.client_id = client_id
        self.provide = "facebook"
        self.name = "openiFacebook"


class Twitter(object):
    def authenticate(self, access_token, access_token_secret):


        app = AppTwitter(client_id=settings.TWITTER_CONSUMER_KEY, secret=settings.TWITTER_CONSUMER_SECRET)
        token = None

        request_factory = RequestFactory()
        request = request_factory.get('/path', data={'name': u'test'},
                                      session={"access_token": access_token,
                                               "access_token_secret": access_token_secret})

        request.session = {}
        request.session["oauth_api.twitter.com_access_token"] = {}
        request.session["oauth_api.twitter.com_access_token"][
            "oauth_token"] = access_token
        request.session["oauth_api.twitter.com_access_token"][
            'oauth_token_secret'] = access_token_secret

        try:
            user = openiTwitterAdapter().complete_login(request=request, app=app, token=token)
            if type(user) == allauth.socialaccount.models.SocialLogin:
                user = user.account.user
            elif list(user) != []:
                user = user[0]
            else:
                user = None
            return user
        except:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class Facebook(object):
    def authenticate(self, username=None, password=None):
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
