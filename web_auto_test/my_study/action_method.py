# -*- coding: utf-8 -*-
from selenium import webdriver
from rg_findelement import RegisterFindElement
import time

class ActionMehtod:
    def open_browser(self,browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()

    def get_url(self,url):
        self.driver.get(url)

    def get_element(self,key):
        find_element = RegisterFindElement(self.driver)
        element = find_element.get_element(key)
        return element

    def element_send_keys(self,value,key):
        element = self.get_element(key)
        element.send_keys(value)

    def click_element(self,key):
        self.get_element(key).click()

    def quit_browser(self):
        self.driver.quit()

    def sleep_time(self):
        time.sleep(3)

    def get_title(self):
        return self.driver.title
