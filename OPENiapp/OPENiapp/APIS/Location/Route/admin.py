__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniEvent


class EventAdmin(admin.ModelAdmin):
    pass


# admin.site.register(OpeniEvent, EventAdmin)
