#-*- coding:utf-8 -*-
"""
Created on 2016-11-22
@author: bevin
"""

import os
from django.conf import settings as global_settings

ABC_CACHE_PREFIX = 'test.abc'
ABC_CACHE_TIMEOUT = 7*24*60*60


global_settings.TEMPLATES[0]['DIRS'].append(os.path.join(os.path.dirname(__file__), 'templates/'))
# TEMPLATE_PATH = '.'