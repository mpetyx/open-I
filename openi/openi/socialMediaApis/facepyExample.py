__author__ = 'mpetyx'

class FacebookOpeni():

    def __init__(self):

        from facepy import GraphAPI

        # Initialize the Graph API with a valid access token (optional,
        # but will allow you to do all sorts of fun stuff).
        self.graph = GraphAPI(oauth_access_token)

    def latest_posts(self):

        # Get my latest posts
        return self.graph.get('me/posts')

    def post_photo(self, photo):

        return self.graph.post(
                    path = 'me/photos',
                    source = open( photo )
                            )

    def fql(self, query):

        return self.graph.fql(query)