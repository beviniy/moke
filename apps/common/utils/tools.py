#-*- coding:utf-8 -*-
"""
Created on 2016-11-21
@author: bevin
"""

import uuid


def create_uuid():
    return str(uuid.uuid1()).replace('-', '')
