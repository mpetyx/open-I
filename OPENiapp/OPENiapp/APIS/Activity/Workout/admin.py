__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniWorkout


class WorkoutAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniWorkout, WorkoutAdmin)
