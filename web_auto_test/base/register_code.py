# -*- coding: utf-8 -*-
import time
from selenium import webdriver
import random
from PIL import Image
import pytesseract

driver = webdriver.Chrome()
def driver_init():
    driver.get('http://www.5itest.cn/register')
    driver.maximize_window()
    time.sleep(5)

#获取element信息
def get_element(id):
    element = driver.find_element_by_xpath(id)
    return element

#获取随机数
def get_range_user():
    user = ''.join(random.sample('123456789abcdef',6))
    return user

#获取图片
def get_code_image(file_name):
    driver.save_screenshot(file_name)  # 将页面截图保存
    code_element = driver.find_element_by_id('code_image')  # 定位图片位置
    #print(code_element.location)  # 打印该元素的坐标
    left = code_element.location['x']  #
    top = code_element.location['y']
    right = code_element.size['width'] + left
    height = code_element.size['height'] + top
    im = Image.open(file_name)
    img = im.crop((left, top, right, height))
    img.save(file_name)

#解析图片获取验证码
def code_online():
    image = Image.open('D:\pycharm\python3\demo\study\image1.png')
    text = pytesseract.image_to_string(image)
    return text

def run_main():
    user_name_info = get_range_user()
    user_email = user_name_info+'@163.com'
    file_name = 'D:\pycharm\python3\demo\study\image1.png'
    driver_init()
    get_element('//*[@id="register_email"]').send_keys(user_email)
    get_element('//*[@id="register_nickname"]').send_keys(user_name_info)
    get_element('//*[@id="register_password"]').send_keys('cde3CDE#')
    get_code_image(file_name)
    text = code_online()
    get_element('//*[@id="captcha_code"]').send_keys(text)
    get_element('//*[@id="register-btn"]').click()
    driver.quit()

run_main()

