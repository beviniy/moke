#-*- coding:utf-8 -*-
"""
Created on 2016-11-21
@author: bevin
"""

from __future__ import unicode_literals

from django.db import models

class TimeModel(models.Model):
    """class: 包含创建和修改时间的基础类"""
    create_time = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=u'创建时间')
    modify_time = models.DateTimeField(auto_now=True, db_index=True, verbose_name=u'更新时间')

    class Meta:
        abstract = True

class NoModel(models.Model):
    """class: 包含唯一编号的基础类"""

    no = models.CharField(max_length=32, unique=True, verbose_name=u'编号')

    class Meta:
        abstract = True


class VisitModel(models.Model):
    '''
    class: 包含唯一浏览数的基础类
    '''
    visit_count = models.IntegerField(default=0, verbose_name=u'浏览数')

    class Meta:
        abstract = True


class EnjoyModel(models.Model):
    '''
    class: 包含唯一喜欢数的基础类
    '''
    enjoy_count = models.IntegerField(default=0, verbose_name=u'喜欢数')

    class Meta:
        abstract = True
