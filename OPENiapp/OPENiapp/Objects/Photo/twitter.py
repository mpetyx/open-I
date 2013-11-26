__author__ = 'mpetyx'

# Twython implementation

import json

from twython import Twython
from allauth.socialaccount.models import SocialToken, SocialApp
# from OPENiapp.allauth.socialaccount.models import SocialToken, SocialApp


# twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
# print json.dumps(twitter.verify_credentials(), sort_keys=True, indent=4)
# print json.dumps(twitter.get_home_timeline(), sort_keys=True, indent=4)

class TWprovider:
    def __init__(self, app, user):
        access_token = SocialToken.objects.filter(account__user=user.id, account__provider='twitter')
        application = SocialApp.objects.filter(name=app, provider='twitter')

        if application and access_token:
            self.connector = Twython(application[0].client_id, application[0].secret, access_token[0].token,
                                     access_token[0].token_secret)


    def home_timeline(self):

        return json.dumps(self.connector.get_home_timeline(), sort_keys=True, indent=4)
    
    def post_photo(self, path):
        photo = open(path, 'rb')
        self.connector.update_status_with_media(status='Testing!!!', media=photo)

# from OPENiapp.Objects.Photo.twitter import TWprovider
# lol = TWprovider('Twitter', 3)
# print json.dumps(lol.connector.verify_credentials(), sort_keys=True, indent=4)
# access_token = SocialToken.objects.filter(account__user=4, account__provider='twitter')