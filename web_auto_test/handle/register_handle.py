# -*- coding: utf-8 -*-
from page.register_page import RegisterPage
from selenium import webdriver

class RegidterHandle(object):
    def __init__(self,driver):
        self.driver = driver
        self.register_page = RegisterPage(self.driver)

    def send_user_email(self,email):  #输入邮箱
        self.register_page.get_email_element().send_keys(email)

    def send_user_name(self,username):  #输入用户名
        self.register_page.get_username_element().send_keys(username)

    def send_user_password(self,password):  #输入密码
        self.register_page.get_password_element().send_keys(password)

    def send_user_code(self,code):  #输入验证码
        #get_code_text = GetCode(self.driver)
        #code  = get_code_text.code_online(file_name)
        self.register_page.get_code_element().send_keys(code)

    def get_user_text(self,info,user_info):
        try:
            if info == 'user_email_error':
                text = self.register_page.get_email_error_element().text    #获取元素文本信息
            elif info == 'user_name_error':
                text = self.register_page.get_username_error_element().text
            elif info == 'password_error':
                text = self.register_page.get_password_error_element().text
            else:
                text = self.register_page.get_code_error_element().text
            #print(text)
        except:
            text = None
        return text


    def click_register_button(self):    #点击注册按钮
        self.register_page.get_button_element().click()

    def get_register_text(self):
        text = self.register_page.get_button_element().text
        return text

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://www.5itest.cn/register')
    re_handle = RegidterHandle(driver)
    res = re_handle.get_register_text()
    driver.quit()
    print(res)