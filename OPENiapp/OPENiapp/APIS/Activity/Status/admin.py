__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniStatus


class StatusAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniStatus, StatusAdmin)
