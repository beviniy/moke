#-*- coding:utf-8 -*-
"""
Created on 2016-11-21
@author: bevin
"""

from . import parameters
from common.utils import parameter
from django.http import HttpResponse
from utils import cache
# Create your views here.


@parameter.checker(parameters.index)
def index(request):
    # print settings.ADMINS
    cache.set_test_abc_cache('123',request.GET['a'])
    return HttpResponse("Hello World! a = %s" % cache.get_test_abc_cache('123'))