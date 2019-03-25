# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:36
# @Author  : lileilei
# @Site    : 
# @File    : testFengzhuang.py
from Public.test_requests import requ
import json
reques = requ()


class TestApi(object):
    def __init__(self, url, key, connent, fangshi):
        self.url = url
        self.key = key
        self.connent = connent
        self.fangshi = fangshi

    def testapi(self):
        if self.fangshi == 'POST':
            self.response = reques.post(self.url, json.loads(self.connent))
        elif self.fangshi == "GET":
            self.response = reques.get(url=self.url, params=self.connent)
        return self.response

    def getJson(self):
        json_data = self.testapi()
        return json_data
