__author__ = 'mpetyx'

from django.conf import settings
from django.contrib.auth.models import User
from django.test import RequestFactory

from OPENiapp.allauth.socialaccount.models import SocialAccount, SocialLogin, SocialToken, SocialApp
from OPENiapp.allauth.socialaccount.adapter import get_adapter
from OPENiapp.allauth.socialaccount.providers.twitter.views import TwitterAPI, TwitterProvider, TwitterOAuthAdapter
from OPENiapp.allauth.account.utils import send_email_confirmation


class App():
    def __init__(self, secret, client_id):
        self.secret = secret
        self.client_id = client_id
        self.provide = "twitter"
        self.name = "openi"


app = App(client_id=settings.TWITTER_CONSUMER_KEY, secret=settings.TWITTER_CONSUMER_SECRET)
token = None

request_factory = RequestFactory()
request = request_factory.get('/path', data={'name': u'test'},
                              session={"access_token": "95257276-yRoHvRIxvcNluK1cwurlhBuvS9QRtt4Z1VTw3sqA",
                                       "access_token_secret": "vCSMwCB8Y9s7FyoVP0qhuO3LWEka5dezxGYuN8gILRE"})

request.session = {}

# request.session["access_token"]="95257276-yRoHvRIxvcNluK1cwurlhBuvS9QRtt4Z1VTw3sqA"
# request.session["access_token_secret"]="vCSMwCB8Y9s7FyoVP0qhuO3LWEka5dezxGYuN8gILRE"
# request.session["oauth_api_twitter_com_access_token"] ="95257276-yRoHvRIxvcNluK1cwurlhBuvS9QRtt4Z1VTw3sqA"
request.session["oauth_api.twitter.com_access_token"] = {}
request.session["oauth_api.twitter.com_access_token"][
    "oauth_token"] = "95257276-yRoHvRIxvcNluK1cwurlhBuvS9QRtt4Z1VTw3sqA"
request.session["oauth_api.twitter.com_access_token"][
    'oauth_token_secret'] = "vCSMwCB8Y9s7FyoVP0qhuO3LWEka5dezxGYuN8gILRE"


class openiTwitterAdapter(TwitterOAuthAdapter):
    def complete_login(self, request, app, token, email_addresses=[]):

        client = TwitterAPI(request, app.client_id, app.secret,
                            self.request_token_url)
        extra_data = client.get_user_info()
        uid = extra_data['id']

        user = User.objects.filter(username=extra_data.get('screen_name'))

        if user:
            return user
        else:

            user = get_adapter() \
                .populate_new_user(username=extra_data.get('screen_name'),
                                   name=extra_data.get('name'))
            user.save()
            account = SocialAccount(user=user,
                                    uid=uid,
                                    provider=TwitterProvider.id,
                                    extra_data=extra_data)
            account.save()
            application = SocialApp.objects.get(secret=app.secret)
            sample_token = SocialToken.objects.filter(app=application, account=account)
            if sample_token:
                token = sample_token[0]
            else:
                token = SocialToken(app=application,
                                    account=account,
                                    token=request.session["oauth_api.twitter.com_access_token"]["oauth_token"],
                                    token_secret=request.session["oauth_api.twitter.com_access_token"][
                                        "oauth_token_secret"])
                token.save()

            mail = send_email_confirmation(request=request, user=user, signup=True)
            return SocialLogin(account=account, token=token, email_addresses=email_addresses)

# from openiHeroku.providers.twitter.SignIn import openiTwitterAdapter
# user = openiTwitterAdapter().complete_login(request=request, app=app, token=token)
#
# user.save(request)
