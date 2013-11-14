__author__ = 'mpetyx'

# Twython implementation

import json

from twython import Twython


APP_KEY = 'Uifi6oR2hXaDaUGtTT61hw'
APP_SECRET = 'UyCcdRcYO4Ls084dGZ5FaQVG1Il3FL1EnQI7doMs'
OAUTH_TOKEN = '95257276-erB33trzmvpc27G0hQhMT9j8QNfWAJx8mML3uVQKU'
OAUTH_TOKEN_SECRET = 'z0HTviJNm7iRXnTDbKNI9iJ5PSrRW7FnXgjh4tCVGuAJ1'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
print json.dumps(twitter.verify_credentials(), sort_keys=True, indent=4)
print json.dumps(twitter.get_home_timeline(), sort_keys=True, indent=4)