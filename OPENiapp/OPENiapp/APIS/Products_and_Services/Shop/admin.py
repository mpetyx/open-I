__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniShop


class ShopAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniShop, ShopAdmin)
