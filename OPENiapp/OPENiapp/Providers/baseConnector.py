import sys

class basicProvider:
    """ This class is used to:
        Instantianate all basic methods and functions of the services as they are needed!
    """
    
    defaultJsonResponse = "Doesn't Exist"
    defaultMethodResponse = "Not supported by this service"


    def __init__(self, application, access_token):
        """ Initiate the connector """
        sys.exit("Should have been implemented!")

    #   region Media API
    #   As described here: http://redmine.openi-ict.eu/projects/openi/wiki/Media_API
    
    #   region Photo Object
    #   As described here: http://redmine.openi-ict.eu/projects/openi/wiki/Photo_Mapping

    def add_extra_parameters(self, response, extra):
        response["extra"] = extra

    def check_if_exists(self, data, check, otherwise):
        if hasattr(data, check):
            data.check
            return data.check
        else:
            return otherwise

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
    
    def get_a_photo(self):
        """ GET API_PATH/[PHOTO_ID] """
        return defaultMethodResponse

    def get_all_photos_for_account(self):
        """ GET API_PATH/[ACCOUNT_ID]/photos """
        return defaultMethodResponse

    def post_photo_to_account(self):
        """ POST API_PATH/[ACCOUNT_ID]/photos """
        return defaultMethodResponse
        
    def post_photo_to_album(self):
        """ POST API_PATH/[ALBUM_ID]/photos """
        return defaultMethodResponse

    def share_a_photo(self):
        """ Share a photo (not available for OPENi - only Tumblr) """
        return defaultMethodResponse

    def edit_a_photo(self):
        """ PUT API_PATH/[PHOTO_ID] """
        return defaultMethodResponse

    def delete_a_photo(self):
        """ DELETE API_PATH/[PHOTO_ID] """
        return defaultMethodResponse
    
    #   region Connections

    def get_photo_comments(self):
        """ GET API_PATH/[PHOTO_ID]/comments """
        return defaultMethodResponse

    def post_comment(self):
        """ POST API_PATH/[PHOTO_ID]/comments """
        return defaultMethodResponse

    def delete_comment(self):
        """ DELETE API_PATH/[COMMENT_ID] """
        return defaultMethodResponse

    def edit_comment(self):
        """ PUT API_PATH/[COMMENT_ID] """
        return defaultMethodResponse

    def like_a_photo(self):
        """ POST API_PATH/[PHOTO_ID]/likes """
        return defaultMethodResponse

    def get_photo_likes(self):
        """ GET API_PATH/[PHOTO_ID]/likes """
        return defaultMethodResponse

    def unlike_photo(self):
        """ DELETE API_PATH/[PHOTO_ID]/likes """
        return defaultMethodResponse

    def dislike_photo(self):
        """ POST API_PATH/[PHOTO_ID]/dislikes """
        return defaultMethodResponse

    def get_photo_dislikes(self):
        """ GET API_PATH/[PHOTO_ID]/dislikes """
        return defaultMethodResponse

    def delete_photo_dislikes(self):
        """ DELETE API_PATH/[PHOTO_ID]/dislikes """
        return defaultMethodResponse


    #   endregion Connections

    #   endregion Photo Object

    #   endregion Media API

    

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