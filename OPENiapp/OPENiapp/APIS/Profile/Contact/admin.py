__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniContact


class ContactAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniContact, ContactAdmin)
