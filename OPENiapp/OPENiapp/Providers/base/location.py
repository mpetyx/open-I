from variables import defJsonRes, defaultMethodResponse

class bcLocation:
    #   region Location API
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Location%20API/
    
    #   region Event Object
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Event%20Mapping/

    def format_event_response(self, data):
        response = {
                        "id": data[0],
                        "objectType": data[1],
                        "service": data[2],
                        "url": data[3],
                        "from":{
                               "id": data[4],
                               "username": data[5],
                               "url": data[6]
                               },
                        "place":{
                            "text": data[7],
                            "address":{
                                "street": data[8],
                                "number": data[9]
                                },
                            "location":{
                                "latitude": data[10],
                                "longtitude": data[11]
                                }
                        },
                        "duration":{
                                "starts_time": data[12],
                                "ends_time": data[13]
                        },
                        "title": data[14],
                        "description": data[15],
                        "picture": data[16]
                   }
        return response
    
    def get_an_event(self, data):
        """ GET API_PATH/[EVENT_ID] """
        return defaultMethodResponse

    def get_all_events_for_account(self, data):
        """ GET API_PATH/[ACCOUNT_ID]/events """
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
    
    
    #   region Place Object
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Place%20Mapping/

    def format_place_response(self, data):
        response = {
                        "id": data[0],
                        "objectType": data[1],
                        "service": data[2],
                        "url": data[3],
                        "from":{
                               "id": data[4],
                               "username": data[5],
                               "url": data[6]
                               },
                        "place":{
                            "text": data[7],
                            "address":{
                                "street": data[8],
                                "number": data[9]
                                },
                            "location":{
                                "latitude": data[10],
                                "longtitude": data[11]
                                }
                        },
                        "time":{
                                "created_time": data[12]
                        },
                        "text": data[13]
                   }
        return response
    
    def get_a_place(self, data):
        """ GET API_PATH/[PLACE_ID] """
        return defaultMethodResponse

    def get_all_places_for_account(self, data):
        """ GET API_PATH/[ACCOUNT_ID]/places """
        return defaultMethodResponse

    def post_place_to_account(self, data):
        """ POST API_PATH/[ACCOUNT_ID]/places """
        return defaultMethodResponse
        
    def post_place_to_aggregation(self, data):
        """ POST API_PATH/[AGGREGATION_ID]/places """
        return defaultMethodResponse

    def edit_a_place(self, data):
        """ PUT API_PATH/[PLACE_ID] """
        return defaultMethodResponse

    def delete_a_place(self, data):
        """ DELETE API_PATH/[PLACE_ID] """
        return defaultMethodResponse
    
    #   region Connections

    def get_place_comments(self, data):
        """ GET API_PATH/[PLACE_ID]/comments """
        return defaultMethodResponse

    def post_place_comment(self, data):
        """ POST API_PATH/[PLACE_ID]/comments """
        return defaultMethodResponse

    def delete_place_comment(self, data):
        """ DELETE API_PATH/[COMMENT_ID] """
        return defaultMethodResponse

    def edit_place_comment(self, data):
        """ PUT API_PATH/[COMMENT_ID] """
        return defaultMethodResponse

    def like_a_place(self, data):
        """ POST API_PATH/[PLACE_ID]/likes """
        return defaultMethodResponse

    def get_place_likes(self, data):
        """ GET API_PATH/[PLACE_ID]/likes """
        return defaultMethodResponse

    def unlike_place(self, data):
        """ DELETE API_PATH/[PLACE_ID]/likes """
        return defaultMethodResponse

    def dislike_place(self, data):
        """ POST API_PATH/[PLACE_ID]/dislikes """
        return defaultMethodResponse

    def get_place_dislikes(self, data):
        """ GET API_PATH/[PLACE_ID]/dislikes """
        return defaultMethodResponse

    def delete_place_dislikes(self, data):
        """ DELETE API_PATH/[PLACE_ID]/dislikes """
        return defaultMethodResponse


    #   endregion Connections

    #   endregion Place Object

    #   endregion Location API