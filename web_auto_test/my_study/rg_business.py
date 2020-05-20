# -*- coding: utf-8 -*-

from rg_handle import RegisterHandle

class RegisterBusiness(object):
    def __init__(self,driver):
        self.driver = driver
        self.handle = RegisterHandle(self.driver)

    def register_business(self,email,name,password,code):
        self.handle.send_user_email(email)
        self.handle.send_user_name(name)
        self.handle.send_password(password)
        self.handle.send_code_text(code)
        self.handle.click_register_button()

    def register_function(self,email,name,password,code,assertCode,assertText):
        self.register_business(email,name,password,code)
        if self.handle.get_user_text(assertCode,assertText) != None:
            return True
        else:
            return False


