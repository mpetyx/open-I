__author__ = 'mpetyx'

from django.contrib import admin
from .models import *


class AudioAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniAudio, AudioAdmin)
