__author__ = 'mpetyx'

from django.contrib import admin
from .models import *


class VideoAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniVideo, VideoAdmin)
