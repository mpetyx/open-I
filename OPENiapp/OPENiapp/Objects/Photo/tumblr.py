__author__ = 'romdim'

# PyTumblr implementation

import pytumblr
import json

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Authenticate via API Key
client = pytumblr.TumblrRestClient(consumer_key, consumer_secret, access_token, access_token_secret)

# Make the request
romdim_posts = client.posts('romdim.tumblr.com')
print json.dumps(romdim_posts['posts'][0]['photos'], sort_keys=True, indent=4)