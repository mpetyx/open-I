from facepy import GraphAPI
from OPENiapp.Providers.baseConnector import basicProvider

# For testing purposes go to https://developers.facebook.com/tools/explorer/ and play
class provider(basicProvider):
    """ This class is used to:
        1. Make the connection to the Graph API
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

    def get_photos(self, limit = 1):
        """ Return user's photos """
        result = self.graph.get('me/photos', limit=limit)
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
        return self.graph.post(path = 'me/photos', source = open(path, 'rb'))

    def get_album_photos(self, data):
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



    # This should be just right!

    # PHOTO API
    def get_photo(self, data):
        """ Get a photo by its id """
        return self.graph.get(self.data.photo_id)
    
    def get_all_photos_for_account(self, data):
        """ Get all photos for an account """
        return self.graph.get(self.data.user_id+'/photos')

    def post_photo_to_account(self, data):
        """ Post a photo to a simple account """
        return self.graph.post(path = self.data.user_id+'/photos', source = open(self.data.path_string, 'rb'))

    def post_photo_to_account(self, data):
        """ Post a photo to an album """
        return self.graph.post(path = self.data.album_id+'/photos', source = open(self.data.path_string, 'rb'))

    def share_photo(self, data):
        """ Share a photo """
        return {'result': 'Not applicable'}

    def edit_photo_object(self, data):
        """ Edit a photo object """
        return {'result': 'Not applicable'}

    def delete_photo_object(self, data):
        """ Delete a photo object """
        return self.graph.delete(self.data.photo_id)

    
    def get_comments(self, data):
        """ Get comments for a photo by its id """
        return self.graph.get(self.data.photo_id+'/comments')
    
    def post_comment(self, data):
        """ Post a comment to a photo by its id """
        return self.graph.post(path = self.data.photo_id+'/comments', data = self.data.comment)
    
    def delete_comment(self, data):
        """ Delete a comment by its id """
        return self.graph.delete(self.data.comment_id)
    
    def edit_comment(self, data):
        """ Edit a comment by its id """
        # This would be possible only by deleting the comment and creating a new one.
        return {'result': 'Not applicable'}
    
    def like_photo(self, data):
        """ Like a photo by its id """
        return self.graph.post(self.data.photo_id + '/likes')
    
    def get_likes_for_photo(self, data):
        """ Get like for a photo by its id """
        return self.graph.get(self.data.photo_id + '/likes')
    
    def unlike_photo(self, data):
        """ Unlike a photo by its id """
        return self.graph.delete(self.data.photo_id + '/likes')
    
    def dislike_photo(self, data):
        """ Dislike a photo by its id """
        return {'result': 'Not applicable'}
    
    def get_dislikes_for_article(self, data):
        """ Get dislikes for an article """
        return {'result': 'Not applicable'}
    
    def delete_photo_from_article(self, data):
        """ Delete a photo from an article """
        return {'result': 'Not applicable'}