__author__ = 'mpetyx'

# Twython implementation

import json

from twython import Twython
from allauth.socialaccount.models import SocialToken, SocialApp

class TWprovider:
    """ This class is used to:
        1. Make the connection to the Twitter API
        2. Get user's Photos
        3. Get OPENi album Photos
        4. Post Photos to OPENi album
    """
    def __init__(self, app, user):
        """ Initiate the connector """
        access_token = SocialToken.objects.filter(account__user=user.id, account__provider='twitter')
        application = SocialApp.objects.filter(name=app, provider='twitter')

        self.connector = None
        if application and access_token:
            self.connector = Twython(application[0].client_id, application[0].secret, access_token[0].token,
                                     access_token[0].token_secret)
    
    def check_if_connected(self):
        if self.connector is not None:
            return True
        else:
            return False

    def home_timeline(self):
        """ Return the home timeline in json """
        return json.dumps(self.connector.get_home_timeline(), sort_keys=True, indent=4)
    
    def post_photo(self, path):
        """ Post a photo as a status """
        if self.check_if_connected():
            photo = open(path, 'rb')
            self.connector.update_status_with_media(status='Testing!!!', media=photo)
        else:
            return "Not connected"