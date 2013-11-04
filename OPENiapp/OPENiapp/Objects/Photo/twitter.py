__author__ = 'mpetyx'

# Twython implementation

import json

from twython import Twython


APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
print json.dumps(twitter.verify_credentials(), sort_keys=True, indent=4)
print json.dumps(twitter.get_home_timeline(), sort_keys=True, indent=4)