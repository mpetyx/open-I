import sys
from base.common import defJsonRes, defaultMethodResponse

class basicProvider:
    """ This class is used to:
        Instantianate all basic methods and functions of the services as they are needed!
    """

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

    def get_fields(self, raw_data, names, fields, alternatives):
        """ 
        Make raw data into data by finding all fields that are provided by a CBS API or by using alternatives to build our response
        If field is seperated by dots check if each field exists in our raw_data
        Fields and Alternatives Arrays should have the same length
        """
        if len(names) == len(fields) == len(alternatives):
            data = {}
            for index in range(len(fields)):
                data[names[index]] = (self.check_if_exists(raw_data, fields[index], alternatives[index]))
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