from OPENiapp.Providers.base.media import bcMedia
from OPENiapp.Providers.base.common import *
import os

class dropboxMedia(bcMedia):
    """ This class is used to:
        1. Make the connection to the Dropbox connector API
        2. Get user's Photos
        3. Get OPENi album Photos
        4. Post Photos to OPENi album
    """
    #   region Media API
    
    #   region Photo Object

    def get_a_photo(self, data):
        """ Get a photo by its id """
        # /photo_id (ie /cat.jpg --> has to be the full filename, no ID) 
        f, metadata = self.connector.get_file_and_metadata('/' + data['photo_id'])
        out = open(data['photo_id'], 'wb')
        out.write(f.read())
        out.close()
        print metadata
                       
        raw_data = metadata
         
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longtitude', 'location_height', 'tags', 'height', 'width'])
 
        fields = ['rev', 'mime_type', 'service', 'path', '', '', '', '', 'created_time', 'client_mtime', '', 'path', '', 'mime_type', 'size', 'icon', '', '', '', '', '', '']
 
        alternatives = ['', 'photo', 'dropbox', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
 
        data = self.get_fields(raw_data, names, fields, alternatives)
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'next': None
                        },
                    'data': self.format_photo_response(data)
                    }
                 
        return { 'response': response }
    
    def get_all_photos_for_account(self, data):
        """ Get all photos for an account """
        return {'result': 'Not applicable'}

    def post_photo_to_account(self, data):
        """ Post a photo to a simple account """
        return {'result': 'Not applicable'}


    def edit_photo_object(self, data):
        """ Edit a photo object """
        return {'result': 'Not applicable'}

    def delete_photo_object(self, params):
        """ Delete a photo object """
        if (check_if_exists(params, 'photo_id') != defJsonRes):
            return self.connector.file_delete(params['photo_id'])
        return "Insufficient Parameters"


    #   endregion Connections

    #   endregion Photo Object
    


    #   region Folder Aggregation 
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Folder%20Mapping

    def get_a_folder(self, data):
        """ GET API_PATH/[FOLDER_ID] """
        # /album_id (ie /10153665525255315)
        raw_data = self.connector.get_file_and_metadata('/' + data['album_id'])
        raw_data2 = self.connector.get_file_and_metadata('/' + data['album_id'] + '/')

        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longtitude', 'location_height', 'tags', 'height', 'width'])
 
        fields = ['rev', 'mime_type', 'service', 'path', '', '', '', '', 'created_time', 'client_mtime', '', 'path', '', 'mime_type', 'size', 'icon', '', '', '', '', '', '']
 
        alternatives = ['', 'photo', 'dropbox', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

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