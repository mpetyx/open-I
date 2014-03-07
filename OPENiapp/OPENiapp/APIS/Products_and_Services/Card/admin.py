__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniCard


class CardAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniCard, CardAdmin)
