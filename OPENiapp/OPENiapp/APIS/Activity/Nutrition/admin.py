__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniNutrition


class NutritionAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniNutrition, NutritionAdmin)
