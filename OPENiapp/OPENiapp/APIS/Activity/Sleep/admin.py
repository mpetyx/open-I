__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniSleep


class SleepAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniSleep, SleepAdmin)
