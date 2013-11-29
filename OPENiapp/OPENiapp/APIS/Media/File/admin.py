__author__ = 'mpetyx'

from django.contrib import admin
from .models import *


class FileAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniFile, FileAdmin)
