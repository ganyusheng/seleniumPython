# -*- coding: utf-8 -*-
from rg_read_ini import RegisterReadIni

class RegisterFindElement:
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,key):
        read = RegisterReadIni()
        data = read.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'xpath':
                return self.driver.find_element_by_xpath(value)
            else:
                return self.driver.find_element_by_class(value)
        except:
            return '未找到的该定位方法！'

