from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized

__author__ = 'amertis'
#todo: remove this and add proper Authorization/Authentication to resources
class NoAuthorization(Authorization):
    """
    Default Authentication class for ``Resource`` objects.

    Only allows ``GET`` requests.
    """
    def read_list(self, object_list, bundle):
        return object_list

    def read_detail(self, object_list, bundle):
        return True

    def create_list(self, object_list, bundle):
        return []

    def create_detail(self, object_list, bundle):
        raise Unauthorized("You are not allowed to access that resource.")

    def update_list(self, object_list, bundle):
        return []

    def update_detail(self, object_list, bundle):
        return True

    def delete_list(self, object_list, bundle):
        return []

    def delete_detail(self, object_list, bundle):
        return True