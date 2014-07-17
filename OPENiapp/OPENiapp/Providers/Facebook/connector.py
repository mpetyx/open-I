from facepy import GraphAPI
from OPENiapp.Providers.baseConnector import basicProvider
from _fbactivity import fbActivity
from _fbmedia import fbMedia
from _fbproductsServices import fbProductsServices
from _fbprofiles import fbProfiles

# For testing purposes go to https://developers.facebook.com/tools/explorer/ and play
class provider(basicProvider, fbActivity, fbMedia, fbProductsServices, fbProfiles):
    """ This class is used to:
        1. Make the connection to the Facebook Graph API
    """
    def __init__(self, access_token):#, data):
        """ Initiate the graph and find the OPENi album """
        self.connector = GraphAPI(access_token)

    

