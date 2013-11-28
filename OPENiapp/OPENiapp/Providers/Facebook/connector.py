__author__ = 'mpetyx'


from facepy import GraphAPI
from allauth.socialaccount.models import SocialApp

# For testing purposes go to https://developers.facebook.com/tools/explorer/ and play
class provider:
    """ This class is used to:
        1. Make the connection to the Graph API
        2. Get user's Photos
        3. Get OPENi album Photos
        4. Post Photos to OPENi album
    """
    def __init__(self, access_token):
        """ Initiate the graph and find the OPENi album """
        self.graph = GraphAPI(access_token)
        self.find_album_openi = self.graph.fql('SELECT object_id  FROM album WHERE owner=me() AND name="OPENi photos"')

    def get_photos(self):
        """ Return user's photos """
        result = self.graph.get('me/photos', limit=1)
        return result

    def get_photos_since(self, since="now"):
        """ Return user's photos since.. """
        result = self.graph.get('me/photos', limit=1, since=since)
        return result

    def get_photos_until(self, until="now"):
        """ Return user's photos until.. """
        result = self.graph.get('me/photos', limit=1, until=until)
        return result

    def post_photo(self, path):
        """ Post a photo to OPENi album """
        self.graph.post(path = 'me/photos', source = open(path, 'rb'))

    def get_album_photos(self):
        """ If there is an OPENi album return its first photo, else return nada """
        if not self.find_album_openi['data']:
            return []
        else:
            result = self.graph.get('/' + self.find_album_openi['data'][0]['object_id'] + '/photos', limit=1)
            return result

    def get_album_photos_before(self, before):
        """ If there is an OPENi album return its first photo before.., else return nada """
        if not self.find_album_openi['data']:
            return []
        else:
            result = self.graph.get('/' + self.find_album_openi['data'][0]['object_id'] + '/photos', limit=1,
                                    before=before)
            return result

    def get_album_photos_after(self, after):
        """ If there is an OPENi album return its first photo after.., else return nada """
        if not self.find_album_openi['data']:
            return []
        else:
            result = self.graph.get('/' + self.find_album_openi['data'][0]['object_id'] + '/photos', limit=1,
                                    after=after)
            return result

    def delete_album_photo(self, id):
        """ Delete an Album Photo by its facebook id. Unfortunately not allowed. """
        # NOT ALLOWED
        #print self.graph.fql('SELECT can_delete FROM photo WHERE object_id='+id)
        #self.graph.fql('DELETE FROM photo WHERE object_id='+id)
        #self.graph.delete()

class Connector:
    def Get_comments(self):
        """"""""