from twython import Twython
from OPENiapp.Providers.baseConnector import basicProvider

class provider(basicProvider):
    """ This class is used to:
        1. Make the connection to the Twitter API
        2. Get user's Photos
        3. Get OPENi album Photos
        4. Post Photos to OPENi album
    """
    def __init__(self, application, access_token):
        """ Initiate the connector """
        self.connector = Twython(application[0].client_id, application[0].secret, access_token[0].token,
                                 access_token[0].token_secret)

    #   region Media API
    #   As described here: http://redmine.openi-ict.eu/projects/openi/wiki/Media_API
    
    #   region Photo Object
    #   As described here: http://redmine.openi-ict.eu/projects/openi/wiki/Photo_Mapping
    
    def get_a_photo(self):
        """ GET API_PATH/[PHOTO_ID] """
        return "Not supported by this service"

    def get_all_photos_for_account(self):
        """ GET API_PATH/[ACCOUNT_ID]/photos """
        return "Not supported by this service"

    def post_photo_to_account(self):
        """ POST API_PATH/[ACCOUNT_ID]/photos """
        return "Not supported by this service"
        
    def post_photo_to_album(self):
        """ POST API_PATH/[ALBUM_ID]/photos """
        return "Not supported by this service"

    def share_a_photo(self):
        """ Share a photo (not available for OPENi - only Tumblr) """
        return "Not supported by this service"

    def edit_a_photo(self):
        """ PUT API_PATH/[PHOTO_ID] """
        return "Not supported by this service"

    def delete_a_photo(self):
        """ DELETE API_PATH/[PHOTO_ID] """
        return "Not supported by this service"
    
    #   region Connections

    def get_photo_comments(self):
        """ GET API_PATH/[PHOTO_ID]/comments """
        return "Not supported by this service"

    def post_comment(self):
        """ POST API_PATH/[PHOTO_ID]/comments """
        return "Not supported by this service"

    def delete_comment(self):
        """ DELETE API_PATH/[COMMENT_ID] """
        return "Not supported by this service"

    def edit_comment(self):
        """ PUT API_PATH/[COMMENT_ID] """
        return "Not supported by this service"

    def like_a_photo(self):
        """ POST API_PATH/[PHOTO_ID]/likes """
        return "Not supported by this service"

    def get_photo_likes(self):
        """ GET API_PATH/[PHOTO_ID]/likes """
        return "Not supported by this service"

    def unlike_photo(self):
        """ DELETE API_PATH/[PHOTO_ID]/likes """
        return "Not supported by this service"

    def dislike_photo(self):
        """ POST API_PATH/[PHOTO_ID]/dislikes """
        return "Not supported by this service"

    def get_photo_dislikes(self):
        """ GET API_PATH/[PHOTO_ID]/dislikes """
        return "Not supported by this service"

    def delete_photo_dislikes(self):
        """ DELETE API_PATH/[PHOTO_ID]/dislikes """
        return "Not supported by this service"


    #   endregion Connections

    #   endregion Photo Object

    #   endregion Media API

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