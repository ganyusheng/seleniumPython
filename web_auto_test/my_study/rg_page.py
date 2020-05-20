# -*- coding: utf-8 -*-

from rg_findelement import RegisterFindElement

class RegisterPage(object):
    def __init__(self,driver):
        self.driver = driver
        self.find_element = RegisterFindElement(self.driver)

    def get_user_email_element(self):   #获取邮箱地址文本框元素定位
        return self.find_element.get_element('user_email')

    def get_user_name_element(self):    #获取用户名文本框元素定位
        return self.find_element.get_element('user_name')

    def get_password_element(self):     #获取密码文本框元素定位
        return self.find_element.get_element('password')

    def get_code_text_element(self):        #获取验证码文本框元素定位
        return self.find_element.get_element('code_text')

    def get_getcode_num_element(self):      #获取验证码图片元素定位
        return self.find_element.get_element('getcode_num')

    def get_user_email_error_element(self):     #获取错误邮箱地址提示信息元素定位
        return self.find_element.get_element('user_email_error')

    def get_user_name_error_element(self):      #获取错误用户名提示信息元素定位
        return self.find_element.get_element('user_name_error')

    def get_password_error_element(self):       #获取错误密码提示信息元素定位
        return self.find_element.get_element('password_error')

    def get_code_text_error_element(self):      #获取错误验证码提示信息元素定位
        return self.find_element.get_element('code_text_error')

    def get_register_button_element(self):      #获取注册按钮元素定位
        return self.find_element.get_element('register_button')




