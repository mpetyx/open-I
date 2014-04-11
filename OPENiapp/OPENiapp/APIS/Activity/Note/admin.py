__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniNote


class NoteAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniNote, NoteAdmin)
