# -*- coding: utf-8 -*-
from handle.register_handle import RegidterHandle
from selenium import webdriver

class RegisterBusiness(object):
    def __init__(self,driver):
        self.register_headle = RegidterHandle(driver)

    def user_business(self,email,name,password,coed):   #输入内容
        self.register_headle.send_user_email(email)
        self.register_headle.send_user_name(name)
        self.register_headle.send_user_password(password)
        self.register_headle.send_user_code(coed)
        self.register_headle.click_register_button()
        self.register_headle.get_register_text()

    def register_success(self):
        if self.register_headle.get_register_text() == None:
            return True
        else:
            return False


    def login_email_error(self,email,name,password,file_name):        #email错误
        self.user_business(email,name,password,file_name)
        if self.register_headle.get_user_text('user_email_error','请输入有效的电子邮件地址') == None:
            print('邮箱校验不成功')
            return True
        else:
            return False

    def register_function(self, email, name, password,code,assertCode, assertText):
        self.user_business(email,name,password,code)
        if self.register_headle.get_user_text(assertCode,assertText) != None:
            return True
        else:
            return False


    def login_name_error(self,email,name,password,file_name):    #name错误
        self.user_business(email,name,password,file_name)
        if self.register_headle.get_user_text('user_name_error', '中、英文均可，最长18个英文或9个汉字') == None:
            print('用户名校验不成功')
            return True
        else:
            return False

    def login_password_error(self,email,name,password,file_name):    #密码错误
        self.user_business(email,name,password,file_name)
        if self.register_headle.get_user_text('password_error', '最少需要输入 5 个字符') == None:
            print('密码校验不成功')
            return True
        else:
            return False

    def login_code_text_error(self,email,name,password,file_name):    #密码错误
        self.user_business(email,name,password,file_name)
        if self.register_headle.get_user_text('code_text_error', '验证码错误') == None:
            print('验证码校验不成功')
            return True
        else:
            return False

