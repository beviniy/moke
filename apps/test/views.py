#-*- coding:utf-8 -*-
"""
Created on 2016-11-21
@author: bevin
"""

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from common.utils import parameter

from . import parameters
from .utils import cache
# Create your views here.

@login_required
@parameter.checker(parameters.index)
def index(request):
    # print settings.ADMINS
    cache.set_test_abc_cache('123',request.GET['a'])
    return HttpResponse("Hello World! a = %s" % cache.get_test_abc_cache('123'))


@parameter.checker(parameters.login)
def log_in(request):

    if request.method == 'GET':
        if request.user.id == None:
            return render(request, 'login.html')
        else:
            return HttpResponse("Welcome, %s" % request.user)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'welcome.html', {'username': username})
        else:
            return HttpResponseRedirect('/test/login')