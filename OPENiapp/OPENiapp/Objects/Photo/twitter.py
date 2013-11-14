__author__ = 'mpetyx'

# Twython implementation

import json

from twython import Twython
from allauth.socialaccount.models import SocialToken, SocialApp
# from OPENiapp.allauth.socialaccount.models import SocialToken, SocialApp


APP_KEY = 'Uifi6oR2hXaDaUGtTT61hw'
APP_SECRET = 'UyCcdRcYO4Ls084dGZ5FaQVG1Il3FL1EnQI7doMs'
OAUTH_TOKEN = '95257276-erB33trzmvpc27G0hQhMT9j8QNfWAJx8mML3uVQKU'
OAUTH_TOKEN_SECRET = 'z0HTviJNm7iRXnTDbKNI9iJ5PSrRW7FnXgjh4tCVGuAJ1'

# twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
# print json.dumps(twitter.verify_credentials(), sort_keys=True, indent=4)
# print json.dumps(twitter.get_home_timeline(), sort_keys=True, indent=4)

class TWprovider:
    def __init__(self, app, user):
        access_token = SocialToken.objects.filter(account__user=user, account__provider='twitter')
        application = SocialApp.objects.filter(name=app, provider='twitter')

        if application and access_token:
            self.connector = Twython(application[0].client_id, application[0].secret, access_token[0].token,
                                     access_token[0].token_secret)

    def home_timeline(self):

        return json.dumps(self.connector.get_home_timeline(), sort_keys=True, indent=4)

# from OPENiapp.Objects.Photo.twitter import TWprovider
# lol = TWprovider('Twitter', 3)
# print json.dumps(lol.connector.verify_credentials(), sort_keys=True, indent=4)