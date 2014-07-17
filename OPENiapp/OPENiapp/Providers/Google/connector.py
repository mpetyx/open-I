from googleplaces import GooglePlaces, types, lang
# https://github.com/slimkrazy/python-google-places

from OPENiapp.Providers.baseConnector import basicProvider
import json
from _golocation import goLocation

class GOPprovider(basicProvider, goLocation):
    ''' This class is used to:
        1. Make the connection to the Google Places API
        2. Get user's Photos
        3. Get OPENi album Photos
        4. Post Photos to OPENi album
    '''
    def __init__(self):
        ''' Initiate the connector '''
        YOUR_API_KEY = 'AIzaSyDoZ455JKv5GS2DgmK1jQc7R8Oj5JVjEnI'
        self.connector = GooglePlaces(YOUR_API_KEY)

    def get_nearby_places(self, data):
        """ EXTRA!!! Find nearby places """
        raw_datas = self.connector.nearby_search(location='London, England', keyword='Fish and Chips', radius=20000, types=[types.TYPE_FOOD])
        fields = ['id', 'type', 'service', 'url', 'user.id', 'user.username', 'website', 'name', 'details.formatted_address', 'details.formatted_address.number', 'geo_location.lat', 'geo_location.lng', 'created_time', 'types']
        alternatives = ['', 'place', 'openi', '', '', '', '', '', '', '', '', '', '', '']
        response = {
                    'meta':
                        {
                            'total_count': 'blah',
                            'next': 'bla'
                        },
                    'data': []
                    }
        for raw_data in raw_datas.places:
            data = self.get_fields(raw_data, fields, alternatives)
            response['data'].append(self.format_place_response(data))
        return response

    def add_a_place(self, data):
        """ EXTRA!!! Add a new place """
        # Returns a detailed instance of googleplaces.Place
        raw_data = self.connector.add_place(name=data['name'],
            lat_lng={'lat': data['lat'], 'lng': data['lng']},
            accuracy=data['accuracy'],
            types=data['type'],
            language=data['lang'])
        response = {
                        'added_place_reference': raw_data.reference,
                        'added_place_id': raw_data.id
                    }
        return response
    
    def delete_a_place(self, data):
        """ DELETE API_PATH/[PLACE_ID] """
        # Returns a detailed instance of googleplaces.Place
        raw_data = self.connector.delete_place(data['reference'])
        return { 'status': 'OK' }