# -*- coding: utf-8 -*-
from find_element import FindElement

class RegisterPage(object):
    def __init__(self,driver):
        self.find_element = FindElement(driver)

    def get_email_element(self):    #获取邮箱元素位置
        return self.find_element.get_element('user_email')

    def get_username_element(self): #获取用户名元素位置
        return self.find_element.get_element('user_name')

    def get_password_element(self): #获取密码元素位置
        return self.find_element.get_element('password')

    def get_code_element(self): #获取验证码元素位置
        return self.find_element.get_element('code_text')

    def get_button_element(self):   #点击按钮元素位置
        return self.find_element.get_element('register_button')

    def get_email_error_element(self):      #获取输入错误email提示信息
        return self.find_element.get_element('user_email_error')

    def get_username_error_element(self):      #获取输入错误username提示信息
        return self.find_element.get_element('user_name_error')

    def get_password_error_element(self):      #获取输入错误password提示信息
        return self.find_element.get_element('password_error')

    def get_code_error_element(self):      #获取输入错误验证码提示信息
        return self.find_element.get_element('code_text_error')