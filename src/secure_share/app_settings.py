# coding=utf-8

from django.conf import settings

# This is an example
SECURE_SHARE_SECRET = settings.SECRET_KEY[::4]
