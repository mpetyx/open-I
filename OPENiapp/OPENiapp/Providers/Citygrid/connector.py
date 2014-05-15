from OPENiapp.Providers.baseConnector import basicProvider

from provider import citygridplaces
# https://github.com/CityGrid/CityGrid-Python-Samples/blob/master/class-citygrid-places-api.py

class provider(basicProvider):
    ''' This class is used to:
        1. Make the connection to the Citygrid API
        2. Get user's Photos
        3. Get OPENi album Photos
        4. Post Photos to OPENi album
    '''
    def __init__(self):
        ''' Initiate the connector '''
        self.connector = citygridplaces()

    def get_a_place(self, data):
        """ GET API_PATH/[PLACE_ID] """
        # Returns a detailed instance of Citygrid
        #https://api.citygridmedia.com/content/places/v2/detail?id=10100230&id_type=cs&placement=search_page&client_ip=123.4.56.78&publisher=test&format=json
        raw_data = self.connector.placesdetail(id = self.check_if_exists(data ,'id', ''),
                                            id_type = self.check_if_exists(data ,'id_type', ''),
                                            phone = self.check_if_exists(data ,'phone', ''),
                                            publishercode = self.check_if_exists(data ,'publisher', ''),
                                            customer_only = self.check_if_exists(data ,'customer_only', ''),
                                            all_results = self.check_if_exists(data, 'all_results', ''),
                                            review_count = self.check_if_exists(data ,'review_count', ''),
                                            placement = self.check_if_exists(data ,'placement', ''),
                                            #client_ip = data['client_ip'],
                                            format = self.check_if_exists(data ,'format', ''),
                                            callback = self.check_if_exists(data ,'callback', ''),
                                            i = self.check_if_exists(data ,'i', ''))
        fields = ['locations.location.id', 'type', 'service', 'locations.location.urls.profile_url', 'user.id', 'user.username', 'locations.location.contact_info.display_url', 'locations.location.name', 'locations.location.address.street', 'locations.location.address.number', 'locations.location.address.latitude', 'locations.location.address.longitude', 'locations.location.years_in_business', 'types']
        alternatives = ['', 'place', 'openi', '', '', '', '', '', '', '', '', '', '', '']
        data = self.get_fields(raw_data, fields, alternatives)
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'next': None
                        },
                    'data': [self.format_place_response(data)]
                    }
        return { 'response': response }