from allauth.socialaccount.models import SocialToken, SocialApp
from Facebook.connector import provider as FBprovider
from Twitter.connector import provider as TWprovider
from Instagram.connector import provider as INprovider
from Foursquare.connector import provider as FOprovider
from Google.connector import GOPprovider
from Citygrid.connector import provider as CGprovider
from Flickr.connector import provider as FLprovider
from Dropbox.connector import provider as DBprovider

class execution:
    def __init__(self, user, apps, method, data):
        """
            Initialize execution class.
            Assign the connected user to a variable
            Assign the apps we need to a variable (apps need to have app.cbs and app.app_name)
            Assign the method we call to a variable
            Assign
        """
        self.user = user
        self.apps = apps
        self.method = method
        self.data = data

    def make_connection(self, cbs):
        """ Call each time we want to make a new connection with one cbs """
        # Every cbs needs its access_token
        # account_provider should be called exactly as the cbs we want, ie facebook for facebook!
        access_token = SocialToken.objects.filter(account__user=self.user, account__provider=cbs)
        # Check which cbs we now have and make the connection by returning the provider from the connector
        if (cbs == "facebook"):
            provider = FBprovider(access_token)
        elif (cbs == "twitter"):
            #application = SocialApp.objects.filter(name=app_name, provider=cbs)
            provider = TWprovider(access_token[0])
        elif (cbs == "instagram"):
            provider = INprovider(access_token[0])
        elif (cbs == "foursquare"):
            provider = FOprovider(access_token[0])
        elif (cbs == "google"):
            provider = GOPprovider()
        elif (cbs == "citygrid"):
            provider = CGprovider()
        elif (cbs == "flickr"):
            provider = FLprovider()
        elif (cbs == "dropbox"):
            provider = DBprovider(access_token[0])

        return provider

    def do_method(self, provider):
        try:
            method_to_call = getattr(provider, self.method)
        except AttributeError:
            return {'attributeError': 'Such method does not exist in this service'}
        return method_to_call(self.data)


    def make_all_connections(self):
        json_result = []
        for app in self.apps:
            provider = self.make_connection(app['cbs'])
            result = self.do_method(provider)
            json_result.append(result)
        return json_result