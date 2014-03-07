__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniQuestion


class QuestionAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniQuestion, QuestionAdmin)
