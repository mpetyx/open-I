from OPENiapp.Providers.baseConnector import basicProvider

from foursquare import Foursquare

class provider(basicProvider):
    ''' This class is used to:
        1. Make the connection to the Foursquare API
        2. Get user's Photos
        3. Get OPENi album Photos
        4. Post Photos to OPENi album
    '''
    def __init__(self, application, access_token):
        ''' Initiate the connector '''
        self.connector = Foursquare(access_token=access_token, version='20140116')
    
    #   region Media API
    #   As described here: http://redmine.openi-ict.eu/projects/openi/wiki/Media_API
    
    #   region Photo Object
    #   As described here: http://redmine.openi-ict.eu/projects/openi/wiki/Photo_Mapping

    def get_user(self, data):
        return self.connector.users()
    
    def get_a_photo(self, data):
        ''' GET API_PATH/[PHOTO_ID] '''
        # /media/media-id (ie media/628147512937366504_917877895)
        raw_data = self.connector.media(data['media_id'])
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'next': None
                        },
                    'data': [self.format_photo_response(
                                        raw_data.id,
                                        self.check_if_exists(raw_data, 'type', 'image'),
                                        'openi',
                                        raw_data.link,
                                        raw_data.user.id,
                                        raw_data.user.username,
                                        raw_data.user.website,
                                        raw_data.caption.text,
                                        raw_data.link,
                                        self.defJsonRes,
                                        self.check_if_exists(raw_data, 'location'),
                                        raw_data.created_time,
                                        self.defJsonRes,
                                        self.check_if_exists(raw_data, 'tags'),
                                        self.defJsonRes,
                                        self.defJsonRes
                                        )]
                    }
        return { 'response': response }

    def get_all_photos_for_account(self, data):
        ''' GET API_PATH/[ACCOUNT_ID]/photos '''
        # /users/user-id (ie users/917877895)
        raw_datas, next = self.connector.user_recent_media(data['account_id'])
        response = {
                    'meta': 
                        {
                        'total_count': len(raw_datas),
                        'next': next
                        },
                    'data' : [] }
        for raw_data in raw_datas:
            response['data'].append(self.format_photo_response(
                                         raw_data.id,
                                         self.check_if_exists(raw_data, 'type', 'image'),
                                         'openi',
                                         raw_data.link,
                                         raw_data.user.id,
                                         raw_data.user.username,
                                         raw_data.user.website,
                                         raw_data.caption.text,
                                         raw_data.link,
                                         self.defJsonRes,
                                         self.check_if_exists(raw_data, 'location'),
                                         raw_data.created_time,
                                         self.defJsonRes,
                                         self.check_if_exists(raw_data, 'tags'),
                                         self.defJsonRes,
                                         self.defJsonRes
                                         ))
        return { 'response': response }

    #   region Connections

    def get_photo_comments(self, data):
        ''' GET API_PATH/[PHOTO_ID]/comments '''
        # /media/media-id/comments (ie media/628147512937366504_917877895/comments)
        raw_datas = self.connector.media_comments(data['media_id'])
        response = {
                    'meta': 
                        {
                        'total_count': len(raw_datas['data'])
                        },
                    'data' : [] }
        for raw_data in raw_datas['data']:
            response['data'].append(self.format_comment_response(
                                         raw_data['id'],
                                         'Photo Comment',
                                         'openi',
                                         defJsonRes,
                                         raw_data['from']['id'],
                                         raw_data['from']['username'],
                                         defJsonRes,
                                         raw_data['created_time'],
                                         defJsonRes,
                                         defJsonRes,
                                         raw_data['text'],
                                         defJsonRes
                                         ))
        return { 'response': response }

    def post_comment(self, data):
        ''' POST API_PATH/[PHOTO_ID]/comments '''
        # /media/media-id/comments (ie media/628147512937366504_917877895/comments)
        # 'error_message': 'Please visit http://bit.ly/instacomments for commenting access' Please email apidevelopers[at]instagram.com for access.
        return defaultMethodResponse

    def delete_comment(self, data):
        ''' DELETE API_PATH/[COMMENT_ID] '''
        # /media/media-id/comments/comment-id (ie media/628147512937366504_917877895/comments/628902539272471262)
        response = self.connector.delete_comment(data['media_id'], data['comment_id'])
        return { 'response': response }

    def like_a_photo(self, data):
        ''' POST API_PATH/[PHOTO_ID]/likes '''
        # /media/media-id/likes (ie media/628147512937366504_917877895/likes)
        response = self.connector.like_media(data['media_id'])
        return { 'response': response }

    def get_photo_likes(self, data):
        ''' GET API_PATH/[PHOTO_ID]/likes '''
        # /media/media-id/likes (ie media/628147512937366504_917877895/likes)
        raw_datas = self.connector.media_likes(data['media_id'])
        response = {
                    'meta': 
                        {
                        'total_count': len(raw_datas['data'])
                        },
                    'data' : [] }
        for raw_data in raw_datas['data']:
            response['data'].append(self.format_comment_response(
                                         defJsonRes,#id
                                         'Photo Like',#obj_type
                                         'openi',#service
                                         defJsonRes,#url
                                         raw_data['id'],#from:id
                                         raw_data['username'],#from:username
                                         defJsonRes,#from:url
                                         defJsonRes,#time:created_time
                                         defJsonRes,#time:edited_time
                                         defJsonRes#target_id
                                         ))
        return 'Not supported by this service'

    def unlike_photo(self, data):
        ''' DELETE API_PATH/[PHOTO_ID]/likes '''
        # /media/media-id/likes (ie media/628147512937366504_917877895/likes)
        response = self.connector.unlike_media(data['media_id'])
        return { 'response': response }


    #   endregion Connections

    #   endregion Photo Object

    #   endregion Media API

    

    #   region Location API
    #   As described here: http://redmine.openi-ict.eu/projects/openi/wiki/Location_API
    
    #   region Event Object
    #   As described here: http://redmine.openi-ict.eu/projects/openi/wiki/Event_Mapping
        
    def get_an_event(self, data):
        """ GET API_PATH/[EVENT_ID] """
        response = self.connector.Events(data['event_id'])
        return defaultMethodResponse

    def get_all_events_for_account(self, data):
        """ GET API_PATH/[VENUE_ID]/events """
        response = self.connector.venues.events(data['venue_id'])
        return defaultMethodResponse

    def post_event_to_account(self, data):
        """ POST API_PATH/[ACCOUNT_ID]/events """
        return defaultMethodResponse
        
    def post_event_to_aggregation(self, data):
        """ POST API_PATH/[AGGREGATION_ID]/events """
        return defaultMethodResponse

    def edit_an_event(self, data):
        """ PUT API_PATH/[EVENT_ID] """
        return defaultMethodResponse

    def delete_an_event(self, data):
        """ DELETE API_PATH/[EVENT_ID] """
        return defaultMethodResponse
    
    #   region Connections

    def get_event_comments(self, data):
        """ GET API_PATH/[EVENT_ID]/comments """
        return defaultMethodResponse

    def post_event_comment(self, data):
        """ POST API_PATH/[EVENT_ID]/comments """
        return defaultMethodResponse

    def delete_event_comment(self, data):
        """ DELETE API_PATH/[COMMENT_ID] """
        return defaultMethodResponse

    def edit_event_comment(self, data):
        """ PUT API_PATH/[COMMENT_ID] """
        return defaultMethodResponse

    def like_an_event(self, data):
        """ POST API_PATH/[EVENT_ID]/likes """
        return defaultMethodResponse

    def get_event_likes(self, data):
        """ GET API_PATH/[EVENT_ID]/likes """
        return defaultMethodResponse

    def unlike_event(self, data):
        """ DELETE API_PATH/[EVENT_ID]/likes """
        return defaultMethodResponse

    def dislike_event(self, data):
        """ POST API_PATH/[EVENT_ID]/dislikes """
        return defaultMethodResponse

    def get_event_dislikes(self, data):
        """ GET API_PATH/[EVENT_ID]/dislikes """
        return defaultMethodResponse

    def delete_event_dislikes(self, data):
        """ DELETE API_PATH/[EVENT_ID]/dislikes """
        return defaultMethodResponse


    #   endregion Connections

    #   endregion Event Object

    #   endregion Location API