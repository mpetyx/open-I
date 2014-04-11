__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniCheckin


class CheckinAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniCheckin, CheckinAdmin)
