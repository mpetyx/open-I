#from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.contrib import admin
#from publi_query_api import *
from tastypie.api import Api
from api import  *


admin.autodiscover()

# private closed api for user
openi_api = Api(api_name='openi')
openi_api.register(PhotoResource())

# public open api for requests
#public_open_api = Api(api_name='query_openi')
#public_openi_api.register(publi_query_api.UserResource())


urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
    
    # urls.py

    # The normal jazz here...
#    (r'^publicapi/', include(public_open_api.urls)),
    (r'^api/', include(openi_api.urls)),
    url(r'^social/', include('social_auth.urls')),

#    (r'^public_api/',include(public_api.urls())),
    #===========================================================================
    # (r'^accounts/', include('registration.backends.default.urls')),
    #===========================================================================
)
