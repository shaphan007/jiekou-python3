# -*- coding: utf-8 -*-
# @Date    : 2017-08-02 21:54:08
# @Author  : lileilei
from Public.fengzhuang_dict import res
from .log import LOG, logger


@logger('断言测试结果')
def assert_in(asserqiwang, fanhuijson):
    if len(asserqiwang.split('=')) > 1:
        data = asserqiwang.split('&')
        result = dict([(item.split('=')) for item in data])
        # value1=([(str(res(fanhuijson,key))) for key in result.keys()])
        # value2=([(str(value)) for value in result.values()])
        for key in result.keys():
            if key in fanhuijson['result'].keys():
                if result[key] != str(fanhuijson['result'][key]):
                    return {'code': 1, 'result': 'fail'}

        return {'code': 0, "result": 'pass'}

    else:
        LOG.info('填写测试预期值')
        return {"code": 2, 'result': '填写测试预期值'}


@logger('断言测试结果')
def assertre(asserqingwang):
    if len(asserqingwang.split('=')) > 1:
        data = asserqingwang.split('&')
        result = dict([(item.split('=')) for item in data])
        return result
    else:
        LOG.info('填写测试预期值')
        raise {"code": 1, 'result': '填写测试预期值'}
