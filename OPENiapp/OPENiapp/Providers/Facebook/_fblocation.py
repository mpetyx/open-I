from OPENiapp.Providers.base.location import bcLocation
from OPENiapp.Providers.base.common import *

class fbLocation(bcLocation):
    """ This class is used to:
        1. Get a Facebook Event
        2. Get all Events for a Facebook Account

        3. Get a Status
        4. Get all Statuses for an Account
        5. Post Status to Account
        6. Post Status to Aggregation
        7. Delete a Status

        8. Get all Comments for a Status
        9. Post a Comment to a Status
        10. Get all Likes for a Status
        11. Post a Like to a Status
        12. Post an Unlike to a Status

        13. Delete a Comment

        14. Get all Comments for a Checkin

        15. Get all RSVP for an Event
        16. Post an RSVP to an Event
    """
    #   region Location API
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Location_API
    
    #   region Place Object
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Place%20Mapping/
    def get_a_place(self, params):
        """ GET API_PATH/[PLACE_ID] """
        return defaultMethodResponse