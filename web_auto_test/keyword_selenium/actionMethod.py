# -*- coding: utf-8 -*-
from selenium import webdriver
from find_element import FindElement
import time

class ActionMethod:
    def __init__(self):
        pass

    def open_browser(self,browser):     #打开浏览器
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()
        self.driver.maximize_window()

    def get_url(self,url):      #输入url
        self.driver.get(url)

    def get_element(self,key):      #定位元素
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    def element_send_keys(self,value,key):        #输入元素
        element = self.get_element(key)
        element.send_keys(value)

    def click_element(self,key):        #点击元素
        self.get_element(key).click()

    def sleep_time(self):       #等待
        time.sleep(3)

    def quit_browser(self):
        self.driver.quit()

    def get_title(self):    #获取title
        return self.driver.title