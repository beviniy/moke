#-*- coding:utf-8 -*-
"""
Created on 2016-11-22
@author: bevin
"""

from django.core.cache import cache
from test import settings

def make_test_abc_key(no, prefix = settings.ABC_CACHE_PREFIX):
    """生成cache key"""
    return '%s.%s' %(prefix, no)

def get_test_abc_cache(no):
    """获取cache key"""
    return cache.get(make_test_abc_key(no))

def set_test_abc_cache(no, value, timeout=settings.ABC_CACHE_TIMEOUT):
    """设置cache key"""
    cache.set(make_test_abc_key(no), value, timeout)

def del_test_abc_cache(no):
    """删除cache key"""
    cache.delete(make_test_abc_key(no))