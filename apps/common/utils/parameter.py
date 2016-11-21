#-*- coding:utf-8 -*-
"""
Created on 2016-11-21
@author: bevin
"""

import re
import copy
import ujson as json
from django.conf import settings
from django.http import HttpResponse

def checker(parameters):
    """检测request参数合法性的装饰器"""

    def _deco(func):
        def __deco(request, *args, **kwargs):
            valid = True
            rsp_data = copy.copy(settings.RETURN_MSG['PARA_ERR'])

            for item in parameters:

                if item['method'] == 'GET':
                    params = request.GET
                elif item['method'] == 'POST':
                    params = request.POST
                elif item['method'] == 'FILES':
                    params = request.FILES
                else:
                    params = request.REQUEST

                if item['must']:
                    if item['name'] not in params:
                        valid = False
                        rsp_data['msg'] = u'缺少%s参数%s' % (
                            item['method'], item['name'])
                        break

                if item['name'] in params:
                    if (not item['must']) and (params[item['name']] == ''):
                        continue
                    if not re.match(item['regex'], params[item['name']]):
                        valid = False
                        rsp_data['msg'] = u'参数%s格式错误' % item['name']

            if valid:
                return func(request, *args, **kwargs)
            else:
                return HttpResponse(json.dumps(rsp_data), content_type="application/json")

        return __deco
    return _deco
