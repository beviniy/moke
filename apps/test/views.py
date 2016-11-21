#-*- coding:utf-8 -*-
"""
Created on 2016-11-21
@author: bevin
"""

from django.shortcuts import render
from django.http import HttpResponse
# from django.conf import settings
# Create your views here.

def index(request):
    # print settings.ADMINS
    return HttpResponse("Hello World!")