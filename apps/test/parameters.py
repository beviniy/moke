#-*- coding:utf-8 -*-
"""
Created on 2016-11-21
@author: bevin
"""


index = [
    {'name':'a', 'must':True, 'method':'GET', 'regex':'^\d$', 'desc':u'测试参数'},
    {'name':'b', 'must':False, 'method':'GET', 'regex':'^\d{2}$', 'desc':u'测试参数'},
]

login = [
    {'name':'username', 'must':False, 'method':'POST', 'regex':'^\w.{3,10}$', 'desc':u'用户名'},
    {'name':'password', 'must':False, 'method':'POST', 'regex':'^.{5,20}$', 'desc':u'密码'},
]