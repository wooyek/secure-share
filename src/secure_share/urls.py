# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from . import views as v

app_name = 'secure_share'

urlpatterns = [
    path('', TemplateView.as_view(template_name="secure_share/jinja2/start.html")),

    path('file/share', v.SharedFileCreate.as_view(), name='SharedFileCreate'),
    path('file/<int:pk>/detail', v.SharedFileDetail.as_view(), name='SharedFileDetail'),
    path('file/<int:pk>/', v.SharedFileAuthorize.as_view(), name='SharedFileAuthorize'),

    path('url/share', v.SharedUrlCreate.as_view(), name='SharedUrlCreate'),
    path('url/<int:pk>/detail', v.SharedUrlDetail.as_view(), name='SharedUrlDetail'),
    path('url/<int:pk>/', v.SharedUrlAuthorize.as_view(), name='SharedUrlAuthorize'),
]
