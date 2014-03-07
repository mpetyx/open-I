__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniDevice


class DeviceAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniDevice, DeviceAdmin)
