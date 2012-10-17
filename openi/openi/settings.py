__author__ = 'mpetyx'

import os
import dj_database_url



ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

#===============================================================================
# The debug status that we currently set at True in order to have a debug mode
#===============================================================================
DEBUG = True
TEMPLATE_DEBUG = DEBUG



ADMINS = (
    ('mpetyx', 'mpetyx@epu.ntua.gr'),
    )

MANAGERS = ADMINS

#DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dfeajme6tin2ll',
        'HOST': 'ec2-54-243-250-155.compute-1.amazonaws.com',
        'PORT': 5432,
        'USER': 'negzygdyaqephj',
        'PASSWORD': '46SZloRqwLQTw_Trf6cRhGigpV'
    }
}


#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': 'openi.db',                      # Or path to database file if using sqlite3.
#        'USER': '',                      # Not used with sqlite3.
#        'PASSWORD': '',                  # Not used with sqlite3.
#        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#    }
#}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'https://s3.amazonaws.com/openiphotos/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = 'https://s3.amazonaws.com/openiphotos/'

# Additional locations of static files
STATICFILES_DIRS = (
# Put strings here, like "/home/html/static" or "C:/www/django/static".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )

# Make this unique, and don't share it with anybody.
SECRET_KEY = '5w1u7a%!#27qu60_bk-ew66!9wb5^g#&amp;%qa%=&amp;+=o#@b&amp;n(p6m'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
    )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

ROOT_URLCONF = 'openi.urls'

# Python dotted path to the WSGI application used by Django's runserver.
#WSGI_APPLICATION = 'openi.wsgi.application'

TEMPLATE_DIRS = (
    # TODO: convert this to use os.join so that it will work on Windows, not just Unix
    ROOT_PATH + '/templates',
    #===========================================================================
    # ROOT_PATH + '/templates/registration',
    #===========================================================================
    )


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'openi',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'tastypie',
    'imagekit',
    'django.contrib.humanize',
    'storages',
    'social_auth',
    "mailer",
    "notification",
    "emailconfirmation",
    "athumb",
    #    'south',
    )

#AUTH_PROFILE_MODULE = 'openi.User'


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# stops IK checking S3 all the time - main reason to use IK v2 for me
IMAGEKIT_DEFAULT_IMAGE_CACHE_BACKEND = 'imagekit.imagecache.NonValidatingImageCacheBackend'

INTERNAL_IPS = ('127.0.0.1',)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    )

#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = 'AKIAJWJD4LJWZ4PMCWTA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'openiphotos'

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    #    'social_auth.backends.google.GoogleOAuthBackend',
    #    'social_auth.backends.google.GoogleOAuth2Backend',
    #    'social_auth.backends.google.GoogleBackend',
    #    'social_auth.backends.contrib.foursquare.FoursquareBackend',
    #    'social_auth.backends.contrib.instagram.InstagramBackend',
    #    'social_auth.backends.OpenIDBackend',
    'social_auth.backends.contrib.bitbucket.BitbucketBackend',
    'django.contrib.auth.backends.ModelBackend',
    )

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
    )

TWITTER_CONSUMER_KEY         = 'Uifi6oR2hXaDaUGtTT61hw'
TWITTER_CONSUMER_SECRET      = 'UyCcdRcYO4Ls084dGZ5FaQVG1Il3FL1EnQI7doMs'
FACEBOOK_APP_ID              = '116224591864093'
FACEBOOK_API_SECRET          = '9e5c5993a5d70f7ceecf96be0be74a5b'
GOOGLE_CONSUMER_KEY          = ''
GOOGLE_CONSUMER_SECRET       = ''
GOOGLE_OAUTH2_CLIENT_ID      = ''
GOOGLE_OAUTH2_CLIENT_SECRET  = ''
FOURSQUARE_CONSUMER_KEY      = ''
FOURSQUARE_CONSUMER_SECRET   = ''
FLICKR_APP_ID                = ''
FLICKR_API_SECRET            = ''
INSTAGRAM_CLIENT_ID          = ''
INSTAGRAM_CLIENT_SECRET      = ''

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
#LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': False,
#    'filters': {
#        'require_debug_false': {
#            '()': 'django.utils.log.RequireDebugFalse'
#        }
#    },
#    'handlers': {
#        'mail_admins': {
#            'level': 'ERROR',
#            'filters': ['require_debug_false'],
#            'class': 'django.utils.log.AdminEmailHandler'
#        }
#    },
#    'loggers': {
#        'django.request': {
#            'handlers': ['mail_admins'],
#            'level': 'ERROR',
#            'propagate': True,
#        },
#    }
#}
