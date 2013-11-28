__author__ = 'mpetyx'

from django.contrib import admin
from .models import *


class PhotoAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniPhoto, PhotoAdmin)
