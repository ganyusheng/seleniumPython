# -*- coding: utf-8 -*-
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.5itest.cn/register')
driver.find_element_by_id('register_email').send_keys('152165@qq.com')
driver.find_element_by_xpath('//*[@id="register-btn"]').click()
time.sleep(5)
text = driver.find_element_by_id('register_email').text
try:
    assert text == ''
    print('pass')
    print(text)
except:
    print('fail')
    print(text)
driver.quit()