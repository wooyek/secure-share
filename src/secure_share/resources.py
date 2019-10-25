# coding=utf-8
from import_export import resources

from . import models


class SharedUrlResource(resources.ModelResource):
    class Meta:
        model = models.SharedUrl


class SharedFileResource(resources.ModelResource):
    class Meta:
        model = models.SharedFile
