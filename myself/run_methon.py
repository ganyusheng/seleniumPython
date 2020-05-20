# -*- coding: utf-8 -*-

import requests
import json

class RunMethod:
    def get_method(self,url,data = None,header = None):
        if header == None:
            res = requests.get(url = url,data = data)
        else:
            res = requests.get(url = url,data = data,headers = header)
        return res

    def post_method(self,url,data,header = None):
        if header == None:
            res = requests.post(url = url,data = data).json()
        else:
            res = requests.post(url = url,data = data,headers = header).json()
        return res

    def run_method(self,method,url,data = None,header = None):
        if method == 'post':
            res = self.post_method(url,data,header)
        else:
            res = self.get_method(url,data,header)
        return json.dumps(res, ensure_ascii = False)


