from OPENiapp.Providers.base.media import bcMedia
from OPENiapp.Providers.base.common import *

class fbMedia(bcMedia):
    """ This class is used to:
        1. Make the connection to the Facebook connector API
        2. Get user's Photos
        3. Get OPENi album Photos
        4. Post Photos to OPENi album
    """
    #   region Media API
    
    #   region Photo Object

    def get_a_photo(self, data):
        """ Get a photo by its id """
        # /photo_id (ie /10153665526210315)
        raw_data = self.connector.get('/' + data['photo_id'])


        names = ['id', 'object_type', 'service', 'url', 'file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'from_id', 'from_name', 'from_surname', 'from_middlename', 'from_birthdate', 'from_organizations', 'location_latitude', 'location_longtitude', 'location_height', 'tags', 'created_time', 'edited_time', 'deleted_time', 'height', 'width']

        fields = ['id', 'object_type', 'service', 'link', 'name', 'description', 'format', 'size', 'icon', 'from.id', 'from.name', 'from.surname', 'from.middlename', 'from.birthdate', 'from.organizations', 'place.location.latitude', 'place.location.longtitude', 'place.location.height', 'tags.data', 'created_time', 'updated_time', 'deleted_time', 'height', 'width']

        alternatives = ['', 'album', 'facebook', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

        data = self.get_fields(raw_data, names, fields, alternatives)
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'next': None
                        },
                    'data': self.format_photo_response(data)
                    }

        # Curate tag array from Facebook
        tag_array = []
        for tag in raw_data['tags']['data']:
            tag_array.append(format_tags(tag['id'], tag['name'], tag['created_time'], '', '', tag['x'], tag['y']))
        response['data']['tags'] = tag_array
        
        return { 'response': response }
    
    def get_all_photos_for_account(self, data):
        """ Get all photos for an account """
        return self.connector.get(self.data.user_id+'/photos')

    def post_photo_to_account(self, data):
        """ Post a photo to a simple account """
        return self.connector.post(path = self.data.user_id+'/photos', source = open(self.data.path_string, 'rb'))

    def post_photo_to_account(self, data):
        """ Post a photo to an album """
        return self.connector.post(path = self.data.album_id+'/photos', source = open(self.data.path_string, 'rb'))

    def share_photo(self, data):
        """ Share a photo """
        return {'result': 'Not applicable'}

    def edit_photo_object(self, data):
        """ Edit a photo object """
        return {'result': 'Not applicable'}

    def delete_photo_object(self, data):
        """ Delete a photo object """
        return self.connector.delete(self.data.photo_id)
    

    #   region Connections
    
    def get_comments(self, data):
        """ Get comments for a photo by its id """
        return self.connector.get(self.data.photo_id+'/comments')
    
    def post_comment(self, data):
        """ Post a comment to a photo by its id """
        return self.connector.post(path = self.data.photo_id+'/comments', data = self.data.comment)
    
    def delete_comment(self, data):
        """ Delete a comment by its id """
        return self.connector.delete(self.data.comment_id)
    
    def edit_comment(self, data):
        """ Edit a comment by its id """
        # This would be possible only by deleting the comment and creating a new one.
        return {'result': 'Not applicable'}
    
    def like_photo(self, data):
        """ Like a photo by its id """
        return self.connector.post(self.data.photo_id + '/likes')
    
    def get_likes_for_photo(self, data):
        """ Get like for a photo by its id """
        return self.connector.get(self.data.photo_id + '/likes')
    
    def unlike_photo(self, data):
        """ Unlike a photo by its id """
        return self.connector.delete(self.data.photo_id + '/likes')
    
    def dislike_photo(self, data):
        """ Dislike a photo by its id """
        return {'result': 'Not applicable'}
    
    def get_dislikes_for_article(self, data):
        """ Get dislikes for an article """
        return {'result': 'Not applicable'}
    
    def delete_photo_from_article(self, data):
        """ Delete a photo from an article """
        return {'result': 'Not applicable'}

    #   endregion Connections

    #   endregion Photo Object
    


    #   region Folder Aggregation 
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Folder%20Mapping

    def get_a_folder(self, data):
        """ GET API_PATH/[FOLDER_ID] """
        # /album_id (ie /10153665525255315)
        raw_data = self.connector.get('/' + data['album_id'])
        raw_data2 = self.connector.get('/' + data['album_id'] + '/photos')

        names = ['id', 'object_type', 'service', 'url', 'file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'from_id', 'from_name', 'from_surname', 'from_middlename', 'from_birthdate', 'from_organizations', 'created_time', 'edited_time', 'deleted_time', 'data']
        fields = ['id', 'object_type', 'service', 'link', 'name', 'description', 'format', 'size', 'icon', 'from.id', 'from.name', 'from.surname', 'from.middlename', 'from.birthdate', 'from.organizations', 'created_time', 'updated_time', 'deleted_time', 'data']
        alternatives = ['', 'album', 'facebook', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

        data = self.get_fields(raw_data, names, fields, alternatives)
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'next': None
                        },
                    'data': self.format_folder_response(data)
                    }
        return { 'response': response }

    #   endregion Folder Aggregation

    #   endregion Media API