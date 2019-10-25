# coding=utf-8
from django.contrib import admin
from import_export.admin import ImportExportMixin

from . import models, resources


@admin.register(models.SharedUrl)
class SharedUrlAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = resources.SharedUrlResource
    list_display = ('email', 'secret', 'url')
    list_filter = ('email', 'url')
    date_hierarchy = 'created'


@admin.register(models.SharedFile)
class SharedUrlAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = resources.SharedFileResource
    list_display = ('email', 'secret', 'file')
    list_filter = ('email',)
    date_hierarchy = 'created'


@admin.register(models.UserAgent)
class UserAgentAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = resources.SharedFileResource
    list_display = ('user', 'agent',)
    list_filter = ('user', 'agent')
    date_hierarchy = 'ts'
