#-*- coding:utf-8 -*-
"""
Created on 2016-11-21
@author: bevin
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.log_in, name='login'),
]