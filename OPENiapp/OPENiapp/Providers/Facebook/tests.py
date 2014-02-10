from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialToken
from connector import provider as FBprovider
from django.test import TestCase

from django.utils import unittest
from django.test import Client

class MyFuncTestCase(unittest.TestCase):
    def testBasic(self):
        a = ['larry', 'curly', 'moe']
        self.assertEqual(my_func(a, 0), 'larry')
        self.assertEqual(my_func(a, 1), 'curly')

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/media/photo/?newway=on')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        #self.assertEqual(len(response.context['customers']), 5)

#class FBTest(TestCase):
#    """ Test all FB Methods for a user saved in db """
    
#    def __init__(self):
#        self.user = User.objects.get(username="romanos.tsouroplis")
#        self.access_token = SocialToken.objects.filter(account__user=self.user.id, account__provider="facebook")
#        self.provider = FBprovider("", self.access_token)
    
#    def new_provider(self):
#        self
    
