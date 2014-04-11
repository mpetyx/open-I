__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniProduct


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniProduct, ProductAdmin)
