from common import *

class bcLocation:
    #   region Location API
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Location%20API/
    
    #   region Event Object
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Event%20Mapping/

    #   Event Object resides in Activity API

    #   endregion Event Object
    
    
    #   region Place Object
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Place%20Mapping/

    def format_place_response(self, params):
        response = {
                        "place": format_place(params),
                        "text": params['text']
                   }
        response.update(format_generic(params))
        return response
    
    def get_a_place(self, params):
        """ GET API_PATH/[PLACE_ID] """
        return defaultMethodResponse

    def get_all_places_for_account(self, params):
        """ GET API_PATH/[ACCOUNT_ID]/places """
        return defaultMethodResponse

    def post_place_to_account(self, params):
        """ POST API_PATH/[ACCOUNT_ID]/places """
        return defaultMethodResponse
        
    def post_place_to_aggregation(self, params):
        """ POST API_PATH/[AGGREGATION_ID]/places """
        return defaultMethodResponse

    def edit_a_place(self, params):
        """ PUT API_PATH/[PLACE_ID] """
        return defaultMethodResponse

    def delete_a_place(self, params):
        """ DELETE API_PATH/[PLACE_ID] """
        return defaultMethodResponse
    
    #   region Connections

    def get_place_comments(self, params):
        """ GET API_PATH/[PLACE_ID]/comments """
        return defaultMethodResponse

    def post_place_comment(self, params):
        """ POST API_PATH/[PLACE_ID]/comments """
        return defaultMethodResponse

    def delete_place_comment(self, params):
        """ DELETE API_PATH/[COMMENT_ID] """
        return defaultMethodResponse

    def edit_place_comment(self, params):
        """ PUT API_PATH/[COMMENT_ID] """
        return defaultMethodResponse

    def like_a_place(self, params):
        """ POST API_PATH/[PLACE_ID]/likes """
        return defaultMethodResponse

    def get_place_likes(self, params):
        """ GET API_PATH/[PLACE_ID]/likes """
        return defaultMethodResponse

    def unlike_place(self, params):
        """ DELETE API_PATH/[PLACE_ID]/likes """
        return defaultMethodResponse

    def dislike_place(self, params):
        """ POST API_PATH/[PLACE_ID]/dislikes """
        return defaultMethodResponse

    def get_place_dislikes(self, params):
        """ GET API_PATH/[PLACE_ID]/dislikes """
        return defaultMethodResponse

    def delete_place_dislikes(self, params):
        """ DELETE API_PATH/[PLACE_ID]/dislikes """
        return defaultMethodResponse


    #   endregion Connections

    #   endregion Place Object

    #   endregion Location API