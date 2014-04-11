__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniMeasurement


class MeasurementAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniMeasurement, MeasurementAdmin)
