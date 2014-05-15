import sys

class basicProvider:
    """ This class is used to:
        Instantianate all basic methods and functions of the services as they are needed!
    """
    
    defJsonRes = "Doesn't Exist"
    defaultMethodResponse = "Not supported by this service"

    def __init__(self, application, access_token):
        """ Initiate the connector """
        sys.exit("Should have been implemented!")

    def add_extra_parameters(self, response, extra):
        response["extra"] = extra

    def check_if_exists(self, data, check, otherwise = defJsonRes):
        """ Loop through the  """
        checkArray = check.split('.')
        ret = data
        for allChecks in checkArray:
            if hasattr(ret, allChecks):
                ret = getattr(ret, allChecks)
            elif isinstance(ret, (list, dict)) and (allChecks in ret):
                ret = ret[allChecks]
            else:
                return otherwise
        return ret

    def get_fields(self, raw_data, fields, alternatives):
        """ 
        Make raw data into data by finding all fields that are provided by a CBS API or by using alternatives to build our response
        If field is seperated by dots check if each field exists in our raw_data
        Fields and Alternatives Arrays should have the same length
        """
        if len(fields) == len(alternatives):
            data = []
            for index in range(len(fields)):
                data.append(self.check_if_exists(raw_data, fields[index], alternatives[index]))
            return data
        else:
            sys.exit("Arrays should have same length!")

    def match_if_exists(self, fields, data):
        """
        Match data from request into data for the post and add up into a single string
        """
        data_dict = {}
        for field in fields:
            if field in data:
                data_dict[field] = data[field]
        return data_dict

    #   region Media API
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Media%20API/
    
    #   region Photo Object
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/photo/

    def format_photo_response(self, id, obj_type, service, url, from_id, from_username, from_url, prof_title, prof_icon, prof_format, location, time_created, time_edited, tags, width, height):
        response = {
                        "id": id,
                        "objectType": obj_type,
                        "service": service,
                        "url": url,
                        "from":{
                               "id": from_id,
                               "username": from_username,
                               "url": from_url
                               },
                        "profile":{
                            "title": prof_title,
                            "icon": prof_icon,
                            "format": prof_format,
                        },
                        "location": location,
                        "time":{
                                "created_time": time_created,
                                "edited_time": time_edited
                        },
                        "tags": tags,
                        "width": width,
                        "height": height
                   }
        return response
    
    def get_a_photo(self, data):
        """ GET API_PATH/[PHOTO_ID] """
        return defaultMethodResponse

    def get_all_photos_for_account(self, data):
        """ GET API_PATH/[ACCOUNT_ID]/photos """
        return defaultMethodResponse

    def post_photo_to_account(self, data):
        """ POST API_PATH/[ACCOUNT_ID]/photos """
        return defaultMethodResponse
        
    def post_photo_to_album(self, data):
        """ POST API_PATH/[ALBUM_ID]/photos """
        return defaultMethodResponse

    def share_a_photo(self, data):
        """ Share a photo (not available for OPENi - only Tumblr) """
        return defaultMethodResponse

    def edit_a_photo(self, data):
        """ PUT API_PATH/[PHOTO_ID] """
        return defaultMethodResponse

    def delete_a_photo(self, data):
        """ DELETE API_PATH/[PHOTO_ID] """
        return defaultMethodResponse
    
    #   region Connections

    def get_photo_comments(self, data):
        """ GET API_PATH/[PHOTO_ID]/comments """
        return defaultMethodResponse

    def post_photo_comment(self, data):
        """ POST API_PATH/[PHOTO_ID]/comments """
        return defaultMethodResponse

    def delete_photo_comment(self, data):
        """ DELETE API_PATH/[COMMENT_ID] """
        return defaultMethodResponse

    def edit_photo_comment(self, data):
        """ PUT API_PATH/[COMMENT_ID] """
        return defaultMethodResponse

    def like_a_photo(self, data):
        """ POST API_PATH/[PHOTO_ID]/likes """
        return defaultMethodResponse

    def get_photo_likes(self, data):
        """ GET API_PATH/[PHOTO_ID]/likes """
        return defaultMethodResponse

    def unlike_photo(self, data):
        """ DELETE API_PATH/[PHOTO_ID]/likes """
        return defaultMethodResponse

    def dislike_photo(self, data):
        """ POST API_PATH/[PHOTO_ID]/dislikes """
        return defaultMethodResponse

    def get_photo_dislikes(self, data):
        """ GET API_PATH/[PHOTO_ID]/dislikes """
        return defaultMethodResponse

    def delete_photo_dislikes(self, data):
        """ DELETE API_PATH/[PHOTO_ID]/dislikes """
        return defaultMethodResponse


    #   endregion Connections

    #   endregion Photo Object

    #   endregion Media API

    

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

    def format_comment_response(self, id, obj_type, service, url, from_id, from_username, from_url, time_created, time_edited, title, text, target_id):
        response = {
                        "id": id,
                        "objectType": obj_type,
                        "service": service,
                        "url": url,
                        "from":{
                               "id": from_id,
                               "username": from_username,
                               "url": from_url
                               },
                        "time":{
                                "created_time": time_created,
                                "edited_time": time_edited
                        },
                        "title": title,
                        "text": width,
                        "target_id": target_id
                   }
        return response

    def format_likes_response(self, id, obj_type, service, url, from_id, from_username, from_url, time_created, time_edited, target_id):
        response = {
                        "id": id,
                        "objectType": obj_type,
                        "service": service,
                        "url": url,
                        "from":{
                               "id": from_id,
                               "username": from_username,
                               "url": from_url
                               },
                        "time":{
                                "created_time": time_created,
                                "edited_time": time_edited
                        },
                        "target_id": target_id
                   }
        return response