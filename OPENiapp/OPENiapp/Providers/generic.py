from Facebook.connector import provider as FBprovider

class execution:
    def __init__(self, apps, method, data):
        self.user = user
        self.apps = apps
        self.method = method
        self.data = data

    def make_connection(self, cbs, app_name):
        if (cbs == "facebook"):
            provider = FBprovider(
                        access_token=SocialToken.objects.filter(account__user=self.user.id, account__provider=cbs),
                        data = self.data)
            try:
               method_to_call = getattr(provider, self.method)
            except AttributeError:
               print AttributeError
            return method_to_call()
        elif (cbs == "twitter"):
            provider = TWprovider(app_name, self.user)


    def make_all_connections():
        json_result = []
        for app in apps:
            json_result.append({
                                'cbs': cbs,
                                'app_name': app_name,
                                'result': make_connection(app.cbs, app.app_name)
                               })