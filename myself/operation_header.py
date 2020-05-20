# -*- coding: utf-8 -*-
from operation_json import OperationJson
import requests
import json

class OperationHeader:
    def __init__(self,response):
        self.response = response
        self.oper_json = OperationJson()

    def get_cookie_url(self):
        #response = json.loads(self.response)
        #print(type(self.response),self.response)
        data = self.response["data"]["url"][0]      #获取返回数据中的url
        return data

    def get_cookie(self):
        url = self.get_cookie_url()+'&callback=jQuery21009892417771030149_1588681864316&_=1588681864318'    #拼接获取cookie请求的url
        cookie = requests.get(url).cookies     #发送请求，并将请求的cookie的返回
        return cookie

    def write_cookie(self):
        cookie = self.get_cookie()
        cookies = requests.utils.dict_from_cookiejar(cookie)    #将cookie转换成字典
        self.oper_json.write_value(cookies)     #写入json


if __name__ == '__main__':
    dic = {'status': 10001, 'msg': '成功', 'data': {'userInfo': {'uid': '8981072'}, 'url': ['http://www.imooc.com/user/ssologin?token=4KhJKsZsXE2zI7tstFb_HjWflb8ZPJg9BbeRjf5gwChrqhJTQU1sVOTgGtbJ7cu9HraHDkqq6ZANqUmshuYaHYWTWAiZ-3whyyJaL3I9nriPvXJIJr5w4R-VKUwoqw3sA3A2hXtM7THtLqRdUgFIk8ISjUhmsz7GmVHzJanWa9XApJQklze5MTOPurbZYLDYJkvBdi3KjD6Fu-pIIuyxyfFgTcUKKGFhnYoGUngrUFmjKOg0zoaarcenx8VMRbbGq-tBBIQO4Eg,-r07U', 'http://coding.imooc.com/user/ssologin?token=9b46ml8ovzVeSyJWOw4A0OBLOSf9G8xh1gaQz__2hzLlggdbyAbNoIvRqTaoqgqtbdsiGUoCwYFfjaEIxY1NmVBNm-zFfv6uD9QsFoOzbO9sN3-NoifanScvud6xxjsQS6HeHDnM0ZGNZL2vT5C0U_tBAohTgHYnHYdy10aEjZwv0VkSBbHbhfMl628R-TDPIxp0fp__Q0KvwXNGZoA9VgmYtMX3RdtMfmKBdgesWWNYtH81OkYrLZlcI8iuTF4jvt4fiO9uVL0,-eHzQd']}}
    data = dic['data']['url']
    print(data)