# -*- coding: utf-8 -*-
# @Author  : leizi
import os, datetime, time
from testCase.case import testinterface
from Public.py_Html import createHtml
from Public.get_excel import datacel
from Public.tomail import Email

# from  Public.Dingtalk import send_ding


'''执行测试的主要文件'''


def start_interface_html_http():
    starttime = datetime.datetime.now()
    day = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    basdir = os.path.abspath(os.path.dirname(__file__))
    path = os.getcwd() + '\\test_case_data\\case.xlsx'
    list_id, list_dec, list_param, list_url, list_method, list_expect, list_name = datacel(path)
    list_relust, list_fail, list_pass, list_json, list_exption, list_weizhi = testinterface()

    # 创建测试报告html文档
    filepath = os.path.join(basdir + '\\test_Report\\%s-result.html' % day)
    if os.path.exists(filepath) is False:
        os.system(r'touch %s' % filepath)
    endtime = datetime.datetime.now()

    createHtml(titles=u'http接口自动化测试报告', filepath=filepath, starttime=starttime,
               endtime=endtime, passge=list_pass, fail=list_fail,
               id=list_id, name=list_name, key=list_dec, coneent=list_param, url=list_url, meth=list_method,
               yuqi=list_expect, json=list_json, relusts=list_relust, weizhi=list_weizhi, exceptions=list_exption)

    contec = u'http接口自动化测试完成，测试通过：%s，测试失败：%s，异常：%s，未知错误：%s' % (
        list_pass, list_fail, list_exption, list_weizhi)

    # 发送测试报告
    email = Email()
    email.sendmail(content=contec, filepath=filepath)


if __name__ == '__main__':
    start_interface_html_http()
