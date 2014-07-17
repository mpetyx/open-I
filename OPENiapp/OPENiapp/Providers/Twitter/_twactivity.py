from OPENiapp.Providers.base.activity import bcActivity
from OPENiapp.Providers.base.common import *

class twActivity(bcActivity):
    """ This class is used to:
        1. Get a Facebook Event
        2. Get all Events for a Facebook Account

        3. Get a Status
        4. Get all Statuses for an Account
        5. Post Status to Account
        6. Post Status to Aggregation
        7. Delete a Status

        8. Get all Comments for a Status
        9. Post a Comment to a Status
        10. Get all Likes for a Status
        11. Post a Like to a Status
        12. Post an Unlike to a Status

        13. Delete a Comment

        14. Get all Comments for a Checkin

        15. Get all RSVP for an Event
        16. Post an RSVP to an Event
    """
    #   region Activity API
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Activity_API
    
    #   region Status Object

    def get_a_status(self, params):
        """ GET API_PATH/{STATUS_ID} """
        # /statuses/show/ (ie /statuses/show/483539224545984500)
        raw_data = self.connector.show_status(id = params['status_id'])
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['title', 'text'])

        fields = ['id', 'object_type', 'service', 'entities.urls[0].url', 'user.id', 'user.category', 'user.url', 'user.name', 'created_at', 'updated_time', 'time.deleted_time']
        fields.extend(['title', 'text'])
        
        alternatives = ['', 'status', 'twitter', '', '', 'user', '', '', '', '', '']
        alternatives.extend(['', ''])

        data = self.get_fields(raw_data, names, fields, alternatives)
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'previous': defJsonRes,
                         'next': defJsonRes
                        },
                    'data': [self.format_status_response(data)]
                    }
        return response

    def get_all_statuses_for_account(self, params):
        """ GET API_PATH/[ACCOUNT_ID]/STATUSES """
        # /statuses/user_timeline (ie statuses/user_timeline/10876852)
        raw_datas = self.connector.get_user_timeline(id = params['user_id'])
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['title', 'text'])

        fields = ['id', 'object_type', 'service', 'entities.urls[0].url', 'user.id', 'user.category', 'user.url', 'user.name', 'created_at', 'updated_time', 'time.deleted_time']
        fields.extend(['title', 'text'])
        
        alternatives = ['', 'status', 'twitter', '', '', 'user', '', '', '', '', '']
        alternatives.extend(['', ''])

        response = {
                    'meta':
                        {
                            'total_count': len(raw_datas),
                            'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                            'next': self.check_if_exists(raw_datas, 'paging.next')
                        },
                    'data': []
                    }
        for raw_data in raw_datas:
            data = self.get_fields(raw_data, names, fields, alternatives)
            response['data'].append(self.format_status_response(data))
        return response

    def post_status_to_account(self, params):
        """ POST API_PATH/[ACCOUNT_ID]/feed """
        # /statuses/update (ie statuses/update/)
        # NOTE: ONLY FOR THE AUTHENTICATED USER!!!
        if (check_if_exists(params, 'status') != defJsonRes):
            return self.connector.post('statuses/update', params = { "status" : params['status'] })
        return "Insufficient Parameters"

    def delete_a_status(self, params):
        """ DELETE API_PATH/{STATUS_ID} """
        # statuses/destroy/status_id (ie statuses/destroy/483547228670537700)
        if (check_if_exists(params, 'status_id') != defJsonRes):
            return self.connector.post('statuses/destroy', { "id" : params['status_id'] })
        return "Insufficient Parameters"
    
    #   region Connections

    def get_status_comments(self, params):
        """ GET API_PATH/[STATUS_ID]/comments """
        # /status_id/comments (ie /10154016839520315/comments)
        raw_datas = self.connector.get('/' + params['status_id'] + '/comments')

        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['title', 'text', 'target_id'])

        fields = ['id', 'object_type', 'service', 'link', 'owner.id', 'owner.category', 'owner.url', 'owner.name', 'time.created_time', 'time.edited_time', 'time.deleted_time']
        fields.extend(['title', 'text', 'target_id'])

        alternatives = ['', 'comment', 'facebook', '', '', '', '', '', '', '', '']
        alternatives.extend(['', '', params['status_id']])

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

    def post_status_comment(self, params):
        """ POST API_PATH/[STATUS_ID]/comments """
        # /status_id/comments (ie /10154016839520315/comments)
        if (check_if_exists(params, 'status_id') != defJsonRes):
            if (check_if_exists(params, 'message') != defJsonRes):
                return self.connector.post(path = params['status_id'] +'/comments', message = params['message'])
            elif (check_if_exists(params, 'attachment_id') != defJsonRes):
                return self.connector.post(path = params['status_id'] +'/comments', attachment_id = params['attachment_id'])
            elif (check_if_exists(params, 'attachment_url') != defJsonRes):
                return self.connector.post(path = params['status_id'] +'/comments', attachment_url = params['attachment_url'])
            elif (check_if_exists(params, 'source') != defJsonRes):
                return self.connector.post(path = params['status_id'] +'/comments', source = params['source'])
        return "Insufficient Parameters"

    #   endregion Connections
    
    #   endregion Status Object

    
    #   region Secondary Objects

    #   region Comment Object

    def delete_a_comment(self, params):
        """ DELETE API_PATH/[COMMENT_ID] """
        # /comment_id (ie /10154016839520315_49048872)
        response = self.connector.delete(
            '/' + params['comment_id']
            )
        return response

    #   Checkins

    def get_comments_for_checkin(self, params):
        """ GET API_PATH/[POST_ID]/comments """
        # /post_id/comments (ie /675350314_10154201196440315/comments)
        raw_datas = self.connector.get('/' + params['post_id'] + '/comments')

        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['title', 'text', 'target_id'])

        fields = ['id', 'object_type', 'service', 'link', 'owner.id', 'owner.category', 'owner.url', 'owner.name', 'time.created_time', 'time.edited_time', 'time.deleted_time']
        fields.extend(['title', 'text', 'target_id'])

        alternatives = ['', 'comment', 'facebook', '', '', '', '', '', '', '', '']
        alternatives.extend(['', '', ''])

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

    #   endregion Comment Object

    #   region Favorite Object

    def format_favorite_response(self, params):
        response = {
                        "target_id": params['target_id']
                   }
        response.update(format_generic(params))
        return response

    def get_favorites_for_user(self, params):
        """ GET API_PATH/[USER_ID]/favorites """
        # /favorites/list (ie favorites/list/10876852)
        raw_datas = self.connector.get_favorites(id = params['user_id'])
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['target_id'])

        fields = ['id', 'object_type', 'service', 'entities.urls[0].url', 'user.id', 'user.category', 'user.url', 'user.name', 'created_at', 'updated_time', 'time.deleted_time']
        fields.extend(['target_id'])
        
        alternatives = ['', 'status', 'twitter', '', '', 'user', '', '', '', '', '']
        alternatives.extend([''])

        response = {
                    'meta':
                        {
                            'total_count': len(raw_datas),
                            'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                            'next': self.check_if_exists(raw_datas, 'paging.next')
                        },
                    'data': []
                    }
        for raw_data in raw_datas:
            data = self.get_fields(raw_data, names, fields, alternatives)
            response['data'].append(self.format_favorite_response(data))
        return response

    def post_favorite_to_status(self, params):
        """ POST API_PATH/[STATUS_ID]/favorites """
        # /favorites/create/status_id (ie /favorites/create/458974978155614209)
        if (check_if_exists(params, 'status_id') != defJsonRes):
            return self.connector.post('favorites/create', params = { "status_id" : params['status_id'] })
        return "Insufficient Parameters"

    def delete_favorite_from_status(self, params):
        """ DELETE API_PATH/[USER_ID]/favorites """
        # /favorites/destroy/status_id (ie /favorites/destroy/458974978155614209)
        if (check_if_exists(params, 'status_id') != defJsonRes):
            return self.connector.post('favorites/destroy', params = { "status_id" : params['status_id'] })
        return "Insufficient Parameters"

    #   endregion Favorite Object

    #   endregion Secondary Objects

    #   endregion Activity API