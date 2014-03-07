__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniActivityEvent


class ActivityEventAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniActivityEvent, ActivityEventAdmin)
