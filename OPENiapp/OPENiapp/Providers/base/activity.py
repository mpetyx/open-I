from variables import defJsonRes, defaultMethodResponse

class bcActivity:
    #   region Activity API
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Activity%20API/
    
    #   region Badge Object
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Badge%20Mapping/

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

    #   endregion Badge Object

    #   endregion Activity API