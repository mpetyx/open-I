from OPENiapp.Providers.base.location import bcLocation
from OPENiapp.Providers.base.common import *

class goLocation(bcLocation):
    """ This class is used to:
        1. Get a Google Place
    """
    # HELPER
    def get_address_by_type(self, address_array, type):
        for address in address_array:
            if (address['types'][0] == type):
                return address['long_name']
        return ''

    #   region Location API
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Location_API
    
    #   region Place Object
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Place%20Mapping/
    def get_a_place(self, params):
        """ GET API_PATH/[PLACE_ID] """
        # /reference (ie /CnRsAAAA98C4wD-VFvzGq-KHVEFhlHuy1TD1W6UYZw7KjuvfVsKMRZkbCVBVDxXFOOCM108n9PuJMJxeAxix3WB6B16c1p2bY1ZQyOrcu1d9247xQhUmPgYjN37JMo5QBsWipTsnoIZA9yAzA-0pnxFM6yAcDhIQbU0z05f3xD3m9NQnhEDjvBoUw-BdcocVpXzKFcnMXUpf-nkyF1w)
        #raw_data = self.connector.get_place(params['place_id'])
        raw_data = self.connector.get_place(params['reference'])
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['place_name', 'place_description', 'place_category', 'place_picture', 'place_address_street', 'place_address_number', 'place_address_apartment', 'place_address_city', 'place_address_locality', 'place_address_country', 'place_address_zip', 'place_location_latitude', 'place_location_longitude', 'place_location_height'])
        names.extend(['text'])

        fields = ['details.place_id', 'object_type', 'service', 'url', 'owner.id', 'owner.category', 'owner.url', 'owner.name', 'time.created_time', 'time.edited_time', 'time.deleted_time']
        fields.extend(['name', '', 'types', 'icon', '', '', '', '', '', '', '', 'geo_location.lat', 'geo_location.lng', ''])
        fields.extend(['name'])

        alternatives = ['', 'place', 'google_places', '', '', '', '', '', '', '', '']
        alternatives.extend(['', '', '', '', '', '', '', '', '', '', '', '', '', ''])
        alternatives.extend([''])

        data = self.get_fields(raw_data, names, fields, alternatives)
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'next': None
                        },
                    'data': [self.format_place_response(data)]
                    }

        address_components = check_if_exists(raw_data, 'details.address_components')
        response['data'][0]['place']['address']['street'] = self.get_address_by_type(address_components, 'route')
        response['data'][0]['place']['address']['number'] = self.get_address_by_type(address_components, 'street_number')
        response['data'][0]['place']['address']['apartment'] = self.get_address_by_type(address_components, '')
        response['data'][0]['place']['address']['city'] = self.get_address_by_type(address_components, '')
        response['data'][0]['place']['address']['locality'] = self.get_address_by_type(address_components, 'locality')
        response['data'][0]['place']['address']['country'] = self.get_address_by_type(address_components, 'country')
        response['data'][0]['place']['address']['zip'] = self.get_address_by_type(address_components, 'postal_code')

        return response

    
    def post_place_to_account(self, params):
        """ POST API_PATH/place/add """
        # /
        if ((check_if_exists(params, 'name') != defJsonRes) & (check_if_exists(params, 'lat_lng') != defJsonRes) & (check_if_exists(params, 'accuracy') != defJsonRes) & (check_if_exists(params, 'types') != defJsonRes)):
                return self.connector.add_place(
                    name = params['name'],
                    lat_lng = params['lat_lng'],
                    naaccuracyme = params['accuracy'],
                    types = params['types'],
                    language = check_if_exists(params, 'language', 'en')
                    )
        return defaultMethodResponse
    
    def delete_a_place(self, params):
        """ DELETE API_PATH/reference """
        if (check_if_exists(params, 'reference') != defJsonRes):
            return self.delete_place(
                reference = params['reference']
                )
        return defaultMethodResponse

    #   endregion Place Object

    #   endregion Location API