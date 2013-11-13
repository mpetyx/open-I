__author__ = 'mpetyx'

import os

module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, '../../photos')


#from facepy import utils
from facepy import GraphAPI
from allauth.socialaccount.models import SocialApp

# Get the access_token somehow
# For testing purposes go to https://developers.facebook.com/tools/explorer/ and play
#access_token = utils.get_application_access_token(application_id, application_secret_key)
class provider:
    def __init__(self, access_token):
        self.graph = GraphAPI(access_token)
        self.find_album_openi = self.graph.fql('SELECT object_id  FROM album WHERE owner=me() AND name="OPENi photos"')

    def examples(self):
        # Profile pic
        self.graph.get('me/picture')

        # Get all photos in file
        text_file = open("all_photos.txt", "w")
        result = self.graph.get('me/photos')
        s = str(result)
        text_file.write(s)
        text_file.close()

        # Get 1st photo
        result = self.graph.get('me/photos', limit=1)
        # Access results: ie the whole data
        result['data']

        # Get photos id:
        result['data'][0]['id']

        # Get from:id
        result['data'][0]['from']['id']

        # Get from:name
        result['data'][0]['from']['name']

        # Get name (they propably mean picture here, there is no name field)
        result['data'][0]['picture']

        # Get icon (this is the source of the file)
        result['data'][0]['source']

        # Get created_time
        result['data'][0]['created_time']

        # Get updated_time
        result['data'][0]['updated_time']

        # Get name_tags (this retrieves the whole tag system, not only names)
        result['data'][0]['tags']['data']

        # Get width
        result['data'][0]['width']

        # Get height
        result['data'][0]['height']

    def get_photos(self):
        result = self.graph.get('me/photos', limit=1)
        return result

    def get_photos_since(self, since="now"):
        result = self.graph.get('me/photos', limit=1, since=since)
        return result

    def get_photos_until(self, until="now"):
        result = self.graph.get('me/photos', limit=1, until=until)
        return result

    def post_photo(self):
        self.graph.post(path='me/photos', source=open(file_path + '/parrot2.jpg', 'rb'))

    def get_album_photos(self):
        if not self.find_album_openi['data']:
            return []
        else:
            result = self.graph.get('/' + self.find_album_openi['data'][0]['object_id'] + '/photos', limit=1)
            return result

    def get_album_photos_before(self, before):
        if not self.find_album_openi['data']:
            return []
        else:
            result = self.graph.get('/' + self.find_album_openi['data'][0]['object_id'] + '/photos', limit=1,
                                    before=before)
            return result

    def get_album_photos_after(self, after):
        if not self.find_album_openi['data']:
            return []
        else:
            result = self.graph.get('/' + self.find_album_openi['data'][0]['object_id'] + '/photos', limit=1,
                                    after=after)
            return result


class Connector:
    def Get_comments(self):
        """"""""