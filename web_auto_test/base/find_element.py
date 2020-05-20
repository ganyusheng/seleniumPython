# -*- coding: utf-8 -*-
import sys
sys.path.append('D:\pycharm\python3\demo\study\web_auto_test\\util')
from read_ini import ReadIni

class FindElement(object):
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)  #获取键的值
        by = data.split('>')[0] #以>号分割，取第一个
        value = data.split('>')[1]  #以>号分割，取第二个
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'calssname':
                return self.driver.find_element_by_class_name(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except: #抛异常

            #self.driver.save_screenshot('D:\pycharm\python3\demo\study\web_auto_test\page\%s.png' %value)  #没定位到元素即截图
            return None

if __name__ == '__main__':
    pass