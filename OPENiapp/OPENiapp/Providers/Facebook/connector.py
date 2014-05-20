from facepy import GraphAPI
from OPENiapp.Providers.baseConnector import basicProvider
from _fbmedia import fbMedia
#from OPENiapp.Providers.Facebook import _fbmedia

# For testing purposes go to https://developers.facebook.com/tools/explorer/ and play
class provider(basicProvider, fbMedia):
    """ This class is used to:
        1. Make the connection to the Facebook Graph API
        2. Get user's Photos
        3. Get OPENi album Photos
        4. Post Photos to OPENi album
    """
    def __init__(self, application, access_token):#, data):
        """ Initiate the graph and find the OPENi album """
        self.connector = GraphAPI(access_token)

    #   region Location API
    #   As described here: http://redmine.openi-ict.eu/projects/openi/wiki/Location_API
    
    #   region Event Object
    #   As described here: http://redmine.openi-ict.eu/projects/openi/wiki/Event_Mapping

    #format_event_response(self, id, obj_type, service, url, from_id, from_username, from_url, place_text, place_add_street, place_add_num, place_loc_lat, place_loc_lon, duration_starts_time, duration_ends_time, title, description, picture)

    def get_an_event(self, data):
        """ GET API_PATH/[EVENT_ID] """
        # /event_id (ie /577733618968497)
        raw_data = self.connector.get(data['event_id'])
        fields = ['id', 'object_type', 'service', 'link', 'owner.id', 'owner.username', 'owner.url', 'location', 'venue.location.street', 'venue.location.number', 'venue.location.latitude', 'venue.location.longtitude', 'start_time', 'end_time', 'name', 'description', 'picture']
        alternatives = ['', 'event', 'openi', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        data = self.get_fields(raw_data, fields, alternatives)
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'next': None
                        },
                    'data': [self.format_event_response(data)]
                    }
        return { 'response': response }

    def get_all_events_for_account(self, data):
        """ GET API_PATH/[ACCOUNT_ID]/events """
        request_string = "/" + data['account_id'] + "/events"
        raw_datas = self.connector.get(request_string)
        fields = ['id', 'object_type', 'service', 'link', 'owner.id', 'owner.username', 'owner.url', 'location', 'venue.location.street', 'venue.location.number', 'venue.location.latitude', 'venue.location.longtitude', 'start_time', 'end_time', 'name', 'description', 'picture']
        alternatives = ['', 'event', 'openi', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        response = {
                    'meta':
                        {
                            'total_count': len(raw_datas['data']),
                            'next': raw_datas['paging']['next']
                        },
                    'data': []
                    }
        for raw_data in raw_datas['data']:
            data = self.get_fields(raw_data, fields, alternatives)
            response['data'].append(self.format_event_response(data))
        return { 'response': response }

    def post_event_to_account(self, data):
        """ POST API_PATH/[ACCOUNT_ID]/events """
        request_string = "/" + data['account_id'] + "/events"
        # As described here: https://developers.facebook.com/docs/graph-api/reference/user/events/#publish
        fields = ['name', 'start_time', 'end_time', 'description', 'location', 'locations_id', 'privacy_type']
        request_data = self.match_if_exists(fields, data)
        raw_data = self.connector.post(request_string, 0, **request_data)
        response = {
                    'data': raw_data
                    }
        return { 'response': response }

    def edit_an_event(self, data):
        """ PUT API_PATH/[EVENT_ID] """
        # /event_id (ie /235785719933823)
        fields = ['name', 'start_time', 'end_time', 'description', 'location', 'locations_id', 'privacy_type']
        request_data = self.match_if_exists(fields, data)
        raw_data = self.connector.post(data['event_id'], 0, **request_data)
        response = {
                    'data': raw_data
                    }
        return { 'response': response }

    def delete_an_event(self, data):
        """ DELETE API_PATH/[EVENT_ID] """
        # /event_id (ie /235785719933823)
        raw_data = self.connector.delete(data['event_id'])
        response = {
                    'data': raw_data
                    }
        return { 'response': response }
    
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
    

