__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniService


class ServiceAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniService, ServiceAdmin)
