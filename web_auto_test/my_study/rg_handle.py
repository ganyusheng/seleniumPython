# -*- coding: utf-8 -*-
from selenium import webdriver
from rg_page import RegisterPage

class RegisterHandle(object):
    def __init__(self,driver):
        self.driver = driver
        self.page = RegisterPage(self.driver)

    def send_user_email(self,email):
        self.page.get_user_email_element().send_keys(email)

    def send_user_name(self,name):
        self.page.get_user_email_element().send_keys(name)

    def send_password(self,password):
        self.page.get_user_email_element().send_keys(password)

    def send_code_text(self,code):
        self.page.get_user_email_element().send_keys(code)

    def get_user_text(self,assertCode,assertText):
        try:
            if assertCode == 'user_email_error':
                text = self.page.get_user_email_error_element().text
            elif assertCode == 'user_name_error':
                text = self.page.get_user_name_error_element().text
            elif assertCode == 'password_error':
                text = self.page.get_password_error_element().text
            else:
                text = self.page.get_code_text_error_element().text
            #return text
        except:
            text = None
        return text

    def click_register_button(self):
        self.page.get_register_button_element().click()

