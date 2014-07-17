from OPENiapp.Providers.base.media import bcMedia
from OPENiapp.Providers.base.common import *

class fbMedia(bcMedia):
    """ This class is used to:
        1. Get a Facebook  Photo
        2. Get all Facebook Photos for an Account
        3. Post a Photo to a Facebook Account
        4. Get all Photos from an album
        4. Post a Photo to an album
        5. Delete a Photo

        6. Get all Comments for a Photo
        7. Post a Comment to a Photo
        8. Like a Photo
        9. Get Likes for a Photo
        10. Unlike a Photo

        11. Get a Video
        12. Get all Videos for an Account
        13. Post a Video to an Account
        14. Post a Video to an Aggregation
        15. Delete a Video
        
        16. Get all Comments for a Video
        17. Post a Comment to a Video
        18. Like a Video
        19. Get Likes for a Video
        20. Unlike a Video

        21. Get a Facebook Album as OPENi's folder
        22. Post a Folder to an Account
    """
    #   region Media API
    
    #   region Photo Object

    def get_a_photo(self, params):
        """ GET API_PATH/[PHOTO_ID] """
        # /photo_id (ie /10153665526210315)
        raw_data = self.connector.get('/' + params['photo_id'])
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longtitude', 'location_height', 'tags', 'height', 'width'])

        fields = ['id', 'object_type', 'service', 'link', 'from.id', '', '', 'from.name', 'created_time', 'updated_time', 'deleted_time', 'name', 'description', 'format', 'size', 'icon', 'place.location.latitude', 'place.location.longtitude', 'place.location.height', 'tags.data', 'height', 'width']

        alternatives = ['', 'photo', 'facebook', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

        data = self.get_fields(raw_data, names, fields, alternatives)
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'previous': defJsonRes,
                         'next': defJsonRes
                        },
                    'data': [self.format_photo_response(data)]
                    }

        # Curate tag array from Facebook
        tag_array = []
        if (check_if_exists(raw_data, 'tags.data') != defJsonRes):
            for tag in raw_data['tags']['data']:
                    tag_names = ['tags_id', 'tags_name', 'tags_time_created_time', 'tags_time_edited_time', 'tags_time_deleted_time', 'tags_x-location', 'tags_y-location']
                    tag_fields = ['id', 'name', 'created_time', '', '', 'x', 'y']
                    tag_alternatives = ['', '', '', '', '', '', '']
                    tag_data = self.get_fields(tag, tag_names, tag_fields, tag_alternatives)
                    tag_array.append(format_tags(tag_data))
        response['data'][0]['tags'] = tag_array
        
        return response
    
    def get_all_photos_for_account(self, params):
        """ GET API_PATH/[ACCOUNT_ID]/photos """
        # /account_id/photos (ie /675350314/photos)
        raw_datas = self.connector.get(params['user_id'] +'/photos')
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longtitude', 'location_height', 'tags', 'height', 'width'])

        fields = ['id', 'object_type', 'service', 'link', 'from.id', '', '', 'from.name', 'created_time', 'updated_time', 'deleted_time', 'name', 'description', 'format', 'size', 'icon', 'place.location.latitude', 'place.location.longtitude', 'place.location.height', 'tags.data', 'height', 'width']

        alternatives = ['', 'photo', 'facebook', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

        response = {
                    'meta':
                        {
                         'total_count': len(raw_datas['data']),
                         'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                         'next': self.check_if_exists(raw_datas, 'paging.next')
                        },
                    'data': []
                    }

        for idx, raw_data in enumerate(raw_datas['data']):
            data = self.get_fields(raw_data, names, fields, alternatives)
            response['data'].append(self.format_photo_response(data))

            # Curate tag array from Facebook
            tag_array = []
            if (check_if_exists(raw_data, 'tags.data') != defJsonRes):
                for tag in raw_data['tags']['data']:
                    tag_names = ['tags_id', 'tags_name', 'tags_time_created_time', 'tags_time_edited_time', 'tags_time_deleted_time', 'tags_x-location', 'tags_y-location']
                    tag_fields = ['id', 'name', 'created_time', '', '', 'x', 'y']
                    tag_alternatives = ['', '', '', '', '', '', '']
                    tag_data = self.get_fields(tag, tag_names, tag_fields, tag_alternatives)
                    tag_array.append(format_tags(tag_data))
            response['data'][idx]['tags'] = tag_array
        
        return response

    def post_photo_to_account(self, params):
        """ POST API_PATH/[ACCOUNT_ID]/photos """
        # /account_id/photos (ie /675350314/photos)
        if (check_if_exists(params, 'user_id') != defJsonRes):
            if (check_if_exists(params, 'source') != defJsonRes):
                return self.connector.post(path = params['user_id'] +'/photos', source = open(self.params.path_string, 'rb'))
            elif (check_if_exists(params, 'url') != defJsonRes):
                return self.connector.post(path = params['user_id'] +'/photos', url = open(self.params.url, 'rb'))
        return "Insufficient Parameters"
    
    def get_all_photos_for_album(self, params):
        """ Get all photos for an album """
        # /album_id/photos (ie /10150259489830315/photos)
        raw_datas = self.connector.get(params['album_id'] +'/photos')
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longtitude', 'location_height', 'tags', 'height', 'width'])

        fields = ['id', 'object_type', 'service', 'link', 'from.id', '', '', 'from.name', 'created_time', 'updated_time', 'deleted_time', 'name', 'description', 'format', 'size', 'icon', 'place.location.latitude', 'place.location.longtitude', 'place.location.height', 'tags.data', 'height', 'width']

        alternatives = ['', 'photo', 'facebook', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

        response = {
                    'meta':
                        {
                         'total_count': len(raw_datas['data']),
                         'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                         'next': self.check_if_exists(raw_datas, 'paging.next')
                        },
                    'data': []
                    }

        for idx, raw_data in enumerate(raw_datas['data']):
            data = self.get_fields(raw_data, names, fields, alternatives)
            response['data'].append(self.format_photo_response(data))

            # Curate tag array from Facebook
            tag_array = []
            if (check_if_exists(raw_data, 'tags.data') != defJsonRes):
                for tag in raw_data['tags']['data']:
                    tag_names = ['tags_id', 'tags_name', 'tags_time_created_time', 'tags_time_edited_time', 'tags_time_deleted_time', 'tags_x-location', 'tags_y-location']
                    tag_fields = ['id', 'name', 'created_time', '', '', 'x', 'y']
                    tag_alternatives = ['', '', '', '', '', '', '']
                    tag_data = self.get_fields(tag, tag_names, tag_fields, tag_alternatives)
                    tag_array.append(format_tags(tag_data))
            response['data'][idx]['tags'] = tag_array
        
        return response
        
    def post_photo_to_album(self, data):
        """ POST API_PATH/[ALBUM_ID]/photos """
        # /album_id/photos (ie /10150259489830315/photos)
        if (check_if_exists(params, 'album_id') != defJsonRes):
            if (check_if_exists(params, 'source') != defJsonRes):
                return self.connector.post(path = params['album_id'] +'/photos', source = open(params['source'], 'rb'))
            elif (check_if_exists(params, 'url') != defJsonRes):
                return self.connector.post(path = params['album_id'] +'/photos', url = open(params['url'], 'rb'))
        return "Insufficient Parameters"

    def delete_a_photo(self, params):
        """ DELETE API_PATH/[PHOTO_ID] """
        # /photo_id (ie /10153665526210315)
        if (check_if_exists(params, 'photo_id') != defJsonRes):
            return self.connector.delete(params['photo_id'])
        return "Insufficient Parameters"
    

    #   region Connections
    
    def get_comments_for_photo(self, params):
        """ GET API_PATH/[PHOTO_ID]/comments """
        # /photo_id/comments (ie /10153665526210315/comments)
        raw_datas = self.connector.get('/' + params['photo_id'] + '/comments')

        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['title', 'text', 'target_id'])

        fields = ['id', 'object_type', 'service', 'link', 'from.id', 'from.category', 'from.url', 'from.name', 'created_time', 'edited_time', 'deleted_time']
        fields.extend(['title', 'message', 'target_id'])

        alternatives = ['', 'comment', 'facebook', '', '', '', '', '', '', '', '']
        alternatives.extend(['', '', params['photo_id']])

        response = {
                    'meta':
                        {
                            'total_count': len(raw_datas['data']),
                            'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                            'next': self.check_if_exists(raw_datas, 'paging.next')
                        },
                    'data': []
                    }
        for raw_data in raw_datas['data']:
            data = self.get_fields(raw_data, names, fields, alternatives)
            response['data'].append(self.format_comment_response(data))
        return response
    
    def post_comment_to_photo(self, params):
        """ POST API_PATH/[PHOTO_ID]/comments """
        # /photo_id/comments (ie /10153665526210315/comments)
        if (check_if_exists(params, 'photo_id') != defJsonRes):
            if (check_if_exists(params, 'message') != defJsonRes):
                return self.connector.post(path = params['photo_id'] +'/comments', message = params['message'])
            elif (check_if_exists(params, 'attachment_id') != defJsonRes):
                return self.connector.post(path = params['photo_id'] +'/comments', attachment_id = params['attachment_id'])
            elif (check_if_exists(params, 'attachment_url') != defJsonRes):
                return self.connector.post(path = params['photo_id'] +'/comments', attachment_url = params['attachment_url'])
            elif (check_if_exists(params, 'source') != defJsonRes):
                return self.connector.post(path = params['photo_id'] +'/comments', source = params['source'])
        return "Insufficient Parameters"
    
    def like_photo(self, params):
        """ POST API_PATH/[PHOTO_ID]/likes """
        # /photo_id/likes (ie /10153665526210315/likes)
        if (check_if_exists(params, 'photo_id') != defJsonRes):
            return self.connector.post(path = params['photo_id'] +'/likes')
        return "Insufficient Parameters"
    
    def get_likes_for_photo(self, params):
        """ GET API_PATH/[PHOTO_ID]/likes """
        # /photo_id/likes (ie /10153665526210315/likes)
        raw_datas = self.connector.get('/' + params['photo_id'] + '/likes')

        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['target_id'])

        fields = ['id', 'object_type', 'service', 'link', 'id', 'category', 'url', 'name', 'time.created_time', 'time.edited_time', 'time.deleted_time']
        fields.extend(['target_id'])

        alternatives = ['', 'comment', 'facebook', '', '', '', '', '', '', '', '']
        alternatives.extend([params['photo_id']])

        response = {
                    'meta':
                        {
                            'total_count': len(raw_datas['data']),
                            'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                            'next': self.check_if_exists(raw_datas, 'paging.next')
                        },
                    'data': []
                    }
        for raw_data in raw_datas['data']:
            data = self.get_fields(raw_data, names, fields, alternatives)
            response['data'].append(self.format_like_response(data))
        return response
    
    def unlike_photo(self, data):
        """ DELETE API_PATH/[PHOTO_ID]/likes """
        # /photo_id/likes (ie /10153665526210315/likes)
        if (check_if_exists(params, 'photo_id') != defJsonRes):
            return self.connector.delete(path = params['photo_id'] +'/likes')
        return "Insufficient Parameters"

    #   endregion Connections

    #   endregion Photo Object

    
    
    #   region Video Object
    
    def get_a_video(self, params):
        """ GET API_PATH/[VIDEO_ID] """
        # /video_id (ie /1708014064955)
        raw_data = self.connector.get('/' + params['video_id'])
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon'])
        names.extend(['location_latitude', 'location_longtitude', 'location_height'])
        names.extend(['tags', 'duration'])

        fields = ['id', 'object_type', 'service', 'link', 'from.id', '', '', 'from.name', 'created_time', 'updated_time', 'deleted_time']
        fields.extend(['name', 'description', 'file_format', 'size', 'picture'])
        fields.extend(['place.location.latitude', 'place.location.longtitude', 'place.location.height'])
        fields.extend(['tags.data', 'duration'])

        alternatives = ['', 'video', 'facebook', '', '', '', '', '', '', '', '']
        alternatives.extend(['', '', '', '', ''])
        alternatives.extend(['', '', ''])
        alternatives.extend(['', ''])

        data = self.get_fields(raw_data, names, fields, alternatives)
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'previous': defJsonRes,
                         'next': defJsonRes
                        },
                    'data': [self.format_photo_response(data)]
                    }

        # Curate tag array from Facebook
        tag_array = []
        if (check_if_exists(raw_data, 'tags.data') != defJsonRes):
            for tag in raw_data['tags']['data']:
                    tag_names = ['tags_id', 'tags_name', 'tags_time_created_time', 'tags_time_edited_time', 'tags_time_deleted_time', 'tags_x-location', 'tags_y-location']
                    tag_fields = ['id', 'name', 'created_time', '', '', 'x', 'y']
                    tag_alternatives = ['', '', '', '', '', '', '']
                    tag_data = self.get_fields(tag, tag_names, tag_fields, tag_alternatives)
                    tag_array.append(format_tags(tag_data))
        response['data'][0]['tags'] = tag_array
        
        return response

    def get_all_videos_for_account(self, params):
        """ GET API_PATH/[ACCOUNT_ID]/videos """
        # account_id/videos (ie /675350314/videos)
        raw_datas = self.connector.get('/' + params['account_id'] + '/videos')
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon'])
        names.extend(['location_latitude', 'location_longtitude', 'location_height'])
        names.extend(['tags', 'duration'])

        fields = ['id', 'object_type', 'service', 'link', 'from.id', '', '', 'from.name', 'created_time', 'updated_time', 'deleted_time']
        fields.extend(['name', 'description', 'file_format', 'size', 'picture'])
        fields.extend(['place.location.latitude', 'place.location.longtitude', 'place.location.height'])
        fields.extend(['tags.data', 'duration'])

        alternatives = ['', 'video', 'facebook', '', '', '', '', '', '', '', '']
        alternatives.extend(['', '', '', '', ''])
        alternatives.extend(['', '', ''])
        alternatives.extend(['', ''])

        data = self.get_fields(raw_data, names, fields, alternatives)
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'previous': defJsonRes,
                         'next': defJsonRes
                        },
                    'data': []
                    }

        for idx, raw_data in enumerate(raw_datas['data']):
            data = self.get_fields(raw_data, names, fields, alternatives)
            response['data'].append(self.format_video_response(data))

            # Curate tag array from Facebook
            tag_array = []
            if (check_if_exists(raw_data, 'tags.data') != defJsonRes):
                for tag in raw_data['tags']['data']:
                    tag_names = ['tags_id', 'tags_name', 'tags_time_created_time', 'tags_time_edited_time', 'tags_time_deleted_time', 'tags_x-location', 'tags_y-location']
                    tag_fields = ['id', 'name', 'created_time', '', '', 'x', 'y']
                    tag_alternatives = ['', '', '', '', '', '', '']
                    tag_data = self.get_fields(tag, tag_names, tag_fields, tag_alternatives)
                    tag_array.append(format_tags(tag_data))
            response['data'][idx]['tags'] = tag_array
        
        return response

    def post_video_to_account(self, params):
        """ POST API_PATH/[ACCOUNT_ID]/videos """
        # /account_id/videos (ie /675350314/videos)
        if (check_if_exists(params, 'user_id') != defJsonRes):
            if (check_if_exists(params, 'source') != defJsonRes):
                return self.connector.post(path = params['user_id'] +'/videos', source = open(self.params.path_string, 'rb'))
            elif (check_if_exists(params, 'url') != defJsonRes):
                return self.connector.post(path = params['user_id'] +'/videos', url = open(self.params.url, 'rb'))
        return "Insufficient Parameters"
        
    def post_video_to_aggregation(self, params):
        """ POST API_PATH/[AGGREGATION_ID]/videos """
        # /aggregation_id/videos (ie /sth/videos)
        if (check_if_exists(params, 'aggregation_id') != defJsonRes):
            if (check_if_exists(params, 'source') != defJsonRes):
                return self.connector.post(path = params['aggregation_id'] +'/videos', source = open(self.params.path_string, 'rb'))
            elif (check_if_exists(params, 'url') != defJsonRes):
                return self.connector.post(path = params['aggregation_id'] +'/videos', url = open(self.params.url, 'rb'))
        return "Insufficient Parameters"

    def delete_a_video(self, params):
        """ DELETE API_PATH/[VIDEO_ID] """
        # /video_id (ie /1708014064955)
        if (check_if_exists(params, 'video_id') != defJsonRes):
            return self.connector.delete('/' + params['video_id'])
        return "Insufficient Parameters"
    
    #   region Connections

    def get_comments_for_video(self, params):
        """ GET API_PATH/[VIDEO_ID]/comments """
        # /video_id/comments (ie /1708014064955/comments)
        raw_datas = self.connector.get('/' + params['video_id'] + '/comments')

        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['title', 'text', 'target_id'])

        fields = ['id', 'object_type', 'service', 'link', 'from.id', 'from.category', 'from.url', 'from.name', 'created_time', 'edited_time', 'deleted_time']
        fields.extend(['title', 'message', 'target_id'])

        alternatives = ['', 'comment', 'facebook', '', '', '', '', '', '', '', '']
        alternatives.extend(['', '', params['video_id']])

        response = {
                    'meta':
                        {
                            'total_count': len(raw_datas['data']),
                            'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                            'next': self.check_if_exists(raw_datas, 'paging.next')
                        },
                    'data': []
                    }
        for raw_data in raw_datas['data']:
            data = self.get_fields(raw_data, names, fields, alternatives)
            response['data'].append(self.format_comment_response(data))
        return response

    def post_comment_to_video(self, params):
        """ POST API_PATH/[VIDEO_ID]/comments """
        # /video_id/comments (ie /1708014064955/comments)
        if (check_if_exists(params, 'video_id') != defJsonRes):
            if (check_if_exists(params, 'message') != defJsonRes):
                return self.connector.post(path = params['video_id'] +'/comments', message = params['message'])
            elif (check_if_exists(params, 'attachment_id') != defJsonRes):
                return self.connector.post(path = params['video_id'] +'/comments', attachment_id = params['attachment_id'])
            elif (check_if_exists(params, 'attachment_url') != defJsonRes):
                return self.connector.post(path = params['video_id'] +'/comments', attachment_url = params['attachment_url'])
            elif (check_if_exists(params, 'source') != defJsonRes):
                return self.connector.post(path = params['video_id'] +'/comments', source = params['source'])
        return "Insufficient Parameters"

    def like_video(self, params):
        """ POST API_PATH/[VIDEO_ID]/likes """
        # /video_id/likes (ie /1708014064955/likes)
        if (check_if_exists(params, 'video_id') != defJsonRes):
            return self.connector.post(path = params['video_id'] +'/likes')
        return "Insufficient Parameters"

    def get_likes_for_video(self, params):
        """ GET API_PATH/[VIDEO_ID]/likes """
        # /video_id/likes (ie /1708014064955/likes)
        raw_datas = self.connector.get('/' + params['video_id'] + '/likes')

        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['target_id'])

        fields = ['id', 'object_type', 'service', 'link', 'id', 'category', 'url', 'name', 'time.created_time', 'time.edited_time', 'time.deleted_time']
        fields.extend(['target_id'])

        alternatives = ['', 'comment', 'facebook', '', '', '', '', '', '', '', '']
        alternatives.extend([params['photo_id']])

        response = {
                    'meta':
                        {
                            'total_count': len(raw_datas['data']),
                            'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                            'next': self.check_if_exists(raw_datas, 'paging.next')
                        },
                    'data': []
                    }
        for raw_data in raw_datas['data']:
            data = self.get_fields(raw_data, names, fields, alternatives)
            response['data'].append(self.format_like_response(data))
        return response

    def unlike_video(self, params):
        """ DELETE API_PATH/[VIDEO_ID]/likes """
        # /video_id/likes (ie /1708014064955/likes)
        if (check_if_exists(params, 'video_id') != defJsonRes):
            return self.connector.delete(path = params['video_id'] +'/likes')
        return "Insufficient Parameters"

    #   endregion Connections

    #   endregion Video Object
    


    #   region Folder Aggregation 
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Folder%20Mapping

    def get_a_folder(self, params):
        """ GET API_PATH/[FOLDER_ID] """
        # /album_id (ie /10153665525255315)
        raw_data = self.connector.get('/' + params['album_id'])
        raw_data2 = self.connector.get('/' + params['album_id'] + '/photos')
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'data'])

        fields = ['id', 'object_type', 'service', 'link', 'from.id', '', '', 'from.name', 'created_time', 'updated_time', 'deleted_time', 'name', 'description', 'format', 'size', 'icon', 'data']

        alternatives = ['', 'album', 'facebook', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

        data = self.get_fields(raw_data, names, fields, alternatives)
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'previous': defJsonRes,
                         'next': defJsonRes
                        },
                    'data': [self.format_folder_response(data)]
                    }
        response['data'][0]['data'] = self.get_all_photos_for_album({'album_id': params['album_id']})
        return response
    
    def post_folder_to_account(self, params):
        """ POST API_PATH/[ACCOUNT_ID] """
        # /account_id (ie /675350314)
        if (check_if_exists(params, 'account_id') != defJsonRes):
            return self.connector.post(
                    '/' + params['account_id'] + '/albums',
                    name = data['name'],
                    message = check_if_exists(params, 'message', ''),
                    privacy = check_if_exists(params, 'privacy', {}))
        return "Insufficient Parameters"

    #   endregion Folder Aggregation

    #   endregion Media API