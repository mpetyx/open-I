__author__ = 'mpetyx'

#from facepy import utils
from facepy import GraphAPI

# Get the access_token somehow
# For testing purposes go to https://developers.facebook.com/tools/explorer/ and play
#access_token = utils.get_application_access_token(application_id, application_secret_key)
class provider:

    def __init__(self, access_token):
        self.graph = GraphAPI(access_token)

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



# OLD TRY! DOESN'T WORK
#from facepy import utils
#from facepy import GraphAPI

#application_id = '116224591864093'
#application_secret_key = '9e5c5993a5d70f7ceecf96be0be74a5b'
#short_lived_access_token = utils.get_application_access_token(application_id, application_secret_key)
##long_lived_access_token, expires_at = utils.get_extended_access_token(short_lived_access_token, application_id, application_secret_key)
#try:
#    long_lived_access_token, expires_at = utils.get_extended_access_token(short_lived_access_token, application_id, application_secret_key)
#except OAuthError as error:
#    print error.message

#graph = GraphAPI(long_lived_access_token)
#graph.get('/me')

class Connector:
    def Get_comments(self):
        """"""""