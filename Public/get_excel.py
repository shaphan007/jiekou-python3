# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:35
# @Author  : lileilei
# @File    : get_excel.py
import xlrd
from Public.log import LOG, logger


@logger('解析测试用例文件')
def datacel(filrpath):
    try:
        file = xlrd.open_workbook(filrpath)
        me = file.sheets()[0]
        nrows = me.nrows
        list_id = []
        list_dec = []
        list_param = []
        list_url = []
        list_method = []
        list_expect = []
        listrelut = []
        list_name = []

        for i in range(1, nrows):
            list_id.append(me.cell(i, 0).value)
            list_dec.append(me.cell(i, 2).value)
            list_param.append(me.cell(i, 3).value)
            list_url.append(me.cell(i, 4).value)
            list_name.append(me.cell(i, 1).value)
            list_method.append((me.cell(i, 5).value))
            list_expect.append((me.cell(i, 6).value))
        return list_id, list_dec, list_param, list_url, list_method, list_expect, list_name
    except Exception as e:
        LOG.info('打开测试用例失败，原因是:%s' % e)
        return
