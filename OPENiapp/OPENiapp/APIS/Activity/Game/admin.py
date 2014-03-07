__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniGame


class GameAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniGame, GameAdmin)
