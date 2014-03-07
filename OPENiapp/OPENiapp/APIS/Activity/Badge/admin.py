__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniBadge


class BadgeAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniBadge, BadgeAdmin)
