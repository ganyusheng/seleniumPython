# -*- coding: utf-8 -*-
import configparser

class ReadIni(object):
    def __init__(self,file_name = None,node = None):
        if file_name == None:
            self.file_name = 'D:\pycharm\python3\demo\study\web_auto_test\config\LocalElement.ini'
        else:
            self.file_name = file_name
        if node == None:
            self.node = 'RegisterElement'
        else:
            self.node = node

        self.cf = self.load_ini()

    def load_ini(self):
        cf = configparser.ConfigParser()  # 读取配置文件的函数
        cf.read(self.file_name, encoding='utf8')  # 配置文件位置
        return cf

    def get_value(self,key):    #获取value值
        data = self.cf.get(self.node, key)
        return data

if __name__ == '__main__':
    read_ini = ReadIni()
    print(read_ini.get_value('user_email'))
#print(cf.get('RegisterElement','user_email'))   #读取配置文件user_email内容
    #r'D:\pycharm\python3\demo\study\web_auto_test\config\LocalElement.ini'