from twython import Twython
from OPENiapp.Providers.baseConnector import basicProvider
from _twactivity import twActivity
#from _twmedia import twMedia
#from _twproductsServices import twProductsServices
#from _twprofiles import twProfiles

class provider(basicProvider, twActivity):
    """ This class is used to:
        1. Make the connection to the Twitter API
    """
    def __init__(self, access_token):
        """ Initiate the connector """
        self.connector = Twython(access_token.app.client_id, access_token.app.secret, access_token.token,
                                 access_token.token_secret)

    #def home_timeline(self):
    #    """ Return the home timeline in json """
    #    return json.dumps(self.connector.get_home_timeline(), sort_keys=True, indent=4)
    
    #def post_photo(self, path):
    #    """ Post a photo as a status """
    #    if self.check_if_connected():
    #        photo = open(path, 'rb')
    #        self.connector.update_status_with_media(status='Testing!!!', media=photo)
    #    else:
    #        return "Not connected"