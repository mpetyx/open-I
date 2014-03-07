__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniArticle


class ArticleAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniArticle, ArticleAdmin)
