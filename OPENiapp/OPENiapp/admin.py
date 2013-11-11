__author__ = 'mpetyx'

from django.contrib import admin
from models import *

class PersonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Person, PersonAdmin)
