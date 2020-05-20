# -*- coding: utf-8 -*-
import configparser

class RegisterReadIni:
    def __init__(self, file_path=None, node=None):
        if file_path != None:
            self.file_path = file_path
        else:
            self.file_path = 'D:\pycharm\python3\demo\study\web_auto_test\my_study\config_element.ini'
        if node != None:
            self.node = node
        else:
            self.node = 'Register_Element'

    def load_ini(self):
        cf = configparser.ConfigParser()
        cf.read(self.file_path)
        return cf

    def get_value(self,key):
        data = self.load_ini().get(self.node,key)
        return data