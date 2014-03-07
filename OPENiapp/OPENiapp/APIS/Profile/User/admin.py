__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniUser


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniUser, UserAdmin)
