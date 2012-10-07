'''
Created on Jun 3, 2012

@author: mpetyx
'''

from django.contrib import admin
from models import *



class PhotoAdmin(admin.ModelAdmin):
    pass

class TwitterAccountAdmin(admin.ModelAdmin):
    pass    

class FacebookAccountAdmin(admin.ModelAdmin):
    pass    

class FacebookStatusAdmin(admin.ModelAdmin):
    pass

admin.site.register(Photo, PhotoAdmin)
#admin.site.register(ProfilePicture, ProfilePictureAdmin)
#admin.site.register(TwitterAccount, TwitterAccountAdmin)
#admin.site.register(FacebookStatus, FacebookStatusAdmin)
#admin.site.register(FacebookAccount, FacebookAccountAdmin)