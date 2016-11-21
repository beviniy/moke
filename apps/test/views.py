#-*- coding:utf-8 -*-
"""
Created on 2016-11-21
@author: bevin
"""

from . import parameters
from common.utils import parameter
from django.shortcuts import render
from django.http import HttpResponse
# from django.conf import settings
# Create your views here.


@parameter.checker(parameters.index)
def index(request):
    # print settings.ADMINS
    return HttpResponse("Hello World!")