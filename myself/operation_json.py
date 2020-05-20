# -*- coding: utf-8 -*-
import json

class OperationJson:
    def __init__(self,file_name = None):
        if file_name == None:
            self.file_name = 'D:\pycharm\python2\\testdjango\demo\detaconfig\\user.json'
        else:
            self.file_name = file_name
        self.data = self.open_json()

    def open_json(self):
        with open(self.file_name) as fp:
            json_data = json.load(fp)
            return json_data

    def get_json_data(self,key):
        json_data = self.data[key]
        return json_data

    def write_value(self,data):
        with open('D:\pycharm\python2\\testdjango\demo\detaconfig\cookie.json','w') as fp:
            fp.write(json.dumps(data))


if __name__ == '__main__':
    json_data = OperationJson()
    print(json_data.open_json())