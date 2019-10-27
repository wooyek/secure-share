# coding=utf-8

from rest_framework import routers

import secure_share.api.urls

router = routers.DefaultRouter()
router.registry.extend(secure_share.api.urls.router.registry)
