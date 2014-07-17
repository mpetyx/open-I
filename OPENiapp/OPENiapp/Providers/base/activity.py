from common import *

class bcActivity:
    #   region Activity API
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Activity%20API/
    
    #   region Event Object
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Event%20Mapping/

    def format_event_response(self, params):
        response = {
                        "description": params['description'],
                        "picture": params['picture'],
                        "title": params['title']
                   }
        response.update(format_duration(params))
        response.update(format_place(params))
        response.update(format_generic(params))
        return response
    
    def get_an_event(self, params):
        """ GET API_PATH/[EVENT_ID] """
        return defaultMethodResponse

    def get_all_events_for_account(self, params):
        """ GET API_PATH/[ACCOUNT_ID]/events """
        return defaultMethodResponse

    def post_event_to_account(self, params):
        """ POST API_PATH/[ACCOUNT_ID]/events """
        return defaultMethodResponse
        
    def post_event_to_aggregation(self, params):
        """ POST API_PATH/[AGGREGATION_ID]/events """
        return defaultMethodResponse

    def edit_an_event(self, params):
        """ PUT API_PATH/[EVENT_ID] """
        return defaultMethodResponse

    def delete_an_event(self, params):
        """ DELETE API_PATH/[EVENT_ID] """
        return defaultMethodResponse

    #   endregion Event Object
    
    #   region Status Object
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Status%20Mapping/

    def format_status_response(self, params):
        response = {
                        "title": params['title'],
                        "text": params['text']
                   }
        response.update(format_generic(params))
        return response

    def get_a_status(self, params):
        """ GET API_PATH/{STATUS_ID} """
        return defaultMethodResponse

    def get_all_statuses_for_account(self, params):
        """ GET API_PATH/{STATUS_ID} """
        return defaultMethodResponse

    def post_status_to_account(self, params):
        """ GET API_PATH/{STATUS_ID} """
        return defaultMethodResponse

    def post_status_to_aggregation(self, params):
        """ GET API_PATH/{STATUS_ID} """
        return defaultMethodResponse

    def edit_a_status(self, params):
        """ GET API_PATH/{STATUS_ID} """
        return defaultMethodResponse

    def delete_a_status(self, params):
        """ GET API_PATH/{STATUS_ID} """
        return defaultMethodResponse
    
    #   region Connections

    def get_status_comments(self, params):
        """ GET API_PATH/[EVENT_ID]/comments """
        return defaultMethodResponse

    def post_status_comment(self, params):
        """ POST API_PATH/[EVENT_ID]/comments """
        return defaultMethodResponse

    def delete_status_comment(self, params):
        """ DELETE API_PATH/[COMMENT_ID] """
        return defaultMethodResponse

    def edit_status_comment(self, params):
        """ PUT API_PATH/[COMMENT_ID] """
        return defaultMethodResponse

    def like_a_status(self, params):
        """ POST API_PATH/[EVENT_ID]/likes """
        return defaultMethodResponse

    def get_status_likes(self, params):
        """ GET API_PATH/[EVENT_ID]/likes """
        return defaultMethodResponse

    def unlike_status(self, params):
        """ DELETE API_PATH/[EVENT_ID]/likes """
        return defaultMethodResponse

    def dislike_status(self, params):
        """ POST API_PATH/[EVENT_ID]/dislikes """
        return defaultMethodResponse

    def get_status_dislikes(self, params):
        """ GET API_PATH/[EVENT_ID]/dislikes """
        return defaultMethodResponse

    def delete_status_dislikes(self, params):
        """ DELETE API_PATH/[EVENT_ID]/dislikes """
        return defaultMethodResponse

    #   endregion Connections
    
    #   endregion Status Object


    #   region Secondary Objects

    #   region Comment Object

    def format_comment_response(self, params):
        response = {
                        "title": params['title'],
                        "text": params['text'],
                        "target_id": params['target_id']
                   }
        response.update(format_generic(params))
        return response

    def delete_a_comment(self, params):
        """ DELETE API_PATH/[COMMENT_ID] """
        return defaultMethodResponse

    def get_comments_for_account(self, params):
        """ GET API_PATH/[ACCOUNT_ID]/comments """
        return defaultMethodResponse

    #   Checkins
    def get_comments_for_checkin(self, params):
        """ GET API_PATH/[CHECKIN_ID]/comments """
        return defaultMethodResponse

    def post_comment_to_checkin(self, params):
        """ POST API_PATH/[CHECKIN_ID]/comments """
        return defaultMethodResponse

    def delete_a_comment_from_checkin(self, params):
        """ DELETE API_PATH/[CHECKIN_ID]/comments """
        return defaultMethodResponse

    #   Notes
    def get_comments_for_note(self, params):
        """ GET API_PATH/[NOTE_ID]/comments """
        return defaultMethodResponse

    def post_comment_to_note(self, params):
        """ POST API_PATH/[NOTE_ID]/comments """
        return defaultMethodResponse

    def delete_a_comment_from_note(self, params):
        """ DELETE API_PATH/[NOTE_ID]/comments """
        return defaultMethodResponse

    #   Statuses
    def get_comments_for_status(self, params):
        """ GET API_PATH/[STATUS_ID]/comments """
        return defaultMethodResponse

    def post_comment_to_status(self, params):
        """ POST API_PATH/[STATUS_ID]/comments """
        return defaultMethodResponse

    def delete_a_comment_from_status(self, params):
        """ DELETE API_PATH/[STATUS_ID]/comments """
        return defaultMethodResponse

    #   Workouts
    def get_comments_for_workout(self, params):
        """ GET API_PATH/[WORKOUT_ID]/comments """
        return defaultMethodResponse

    def post_comment_to_workout(self, params):
        """ POST API_PATH/[WORKOUT_ID]/comments """
        return defaultMethodResponse

    def delete_a_comment_from_workout(self, params):
        """ DELETE API_PATH/[WORKOUT_ID]/comments """
        return defaultMethodResponse

    #   endregion Comment Object

    #   region Like Object

    def format_like_response(self, params):
        response = {
                        "target_id": params['target_id']
                   }
        response.update(format_generic(params))
        return response

    def delete_a_like(self, params):
        """ DELETE API_PATH/[COMMENT_ID] """
        return defaultMethodResponse

    def get_likes_for_account(self, params):
        """ GET API_PATH/[ACCOUNT_ID]/comments """
        return defaultMethodResponse

    #   Checkins
    def get_likes_for_checkin(self, params):
        """ GET API_PATH/[CHECKIN_ID]/comments """
        return defaultMethodResponse

    def post_like_to_checkin(self, params):
        """ POST API_PATH/[CHECKIN_ID]/comments """
        return defaultMethodResponse

    def delete_a_like_from_checkin(self, params):
        """ DELETE API_PATH/[CHECKIN_ID]/comments """
        return defaultMethodResponse

    #   Notes
    def get_likes_for_note(self, params):
        """ GET API_PATH/[NOTE_ID]/comments """
        return defaultMethodResponse

    def post_like_to_note(self, params):
        """ POST API_PATH/[NOTE_ID]/comments """
        return defaultMethodResponse

    def delete_a_like_from_note(self, params):
        """ DELETE API_PATH/[NOTE_ID]/comments """
        return defaultMethodResponse

    #   Statuses
    def get_likes_for_status(self, params):
        """ GET API_PATH/[STATUS_ID]/comments """
        return defaultMethodResponse

    def post_like_to_status(self, params):
        """ POST API_PATH/[STATUS_ID]/comments """
        return defaultMethodResponse

    def delete_a_like_from_status(self, params):
        """ DELETE API_PATH/[STATUS_ID]/comments """
        return defaultMethodResponse

    #   Videos
    def get_likes_for_video(self, params):
        """ GET API_PATH/[WORKOUT_ID]/comments """
        return defaultMethodResponse

    def post_like_to_video(self, params):
        """ POST API_PATH/[WORKOUT_ID]/comments """
        return defaultMethodResponse

    def delete_a_like_from_video(self, params):
        """ DELETE API_PATH/[WORKOUT_ID]/comments """
        return defaultMethodResponse

    #   endregion Like Object

    #   region RSVP Object

    def format_rsvp_response(self, params):
        response = {
                        "rsvp": params['rsvp'],
                        "target_id": params['target_id']
                   }
        response.update(format_generic(params))
        return response

    def get_rsvp_from_event(self, params):
        """ GET API_PATH/[EVENT_ID]/rsvp """
        return defaultMethodResponse

    def get_rsvp_for_account(self, params):
        """ GET API_PATH/[ACCOUNT_ID]/events """
        return defaultMethodResponse

    def post_rsvp_to_event(self, params):
        """ POST API_PATH/[EVENT_ID]/rsvp """
        return defaultMethodResponse

    #   endregion RSVP Object

    #   region Favorite Object

    def format_favorite_response(self, params):
        response = {
                        "target_id": params['target_id']
                   }
        response.update(format_generic(params))
        return response

    def get_favorites_for_user(self, params):
        """ GET API_PATH/[USER_ID]/favorites """
        return defaultMethodResponse

    def get_favorites_from_status(self, params):
        """ GET API_PATH/[STATUS_ID]/favorites """
        return defaultMethodResponse

    def post_favorite_to_status(self, params):
        """ POST API_PATH/[STATUS_ID]/favorites """
        return defaultMethodResponse

    def delete_favorite_from_status(self, params):
        """ DELETE API_PATH/[USER_ID]/favorites """
        return defaultMethodResponse

    #   endregion Favorite Object

    #   endregion Secondary Objects

    #   endregion Activity API