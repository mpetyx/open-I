__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniApplication


class ApplicationAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniApplication, ApplicationAdmin)
