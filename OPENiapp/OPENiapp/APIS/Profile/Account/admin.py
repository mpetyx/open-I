__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniAccount


class AccountAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniAccount, AccountAdmin)
