# -*- coding: utf-8 -*-
from selenium import  webdriver
import time
import random
from PIL import Image
from find_element import FindElement
import pytesseract

class RegidterFunction(object):
    def __init__(self,url,i):
        self.driver = self.get_driver(url,i)

    def get_driver(self,url,i):       #创建driver,使用三个不同浏览器
        if i == 0:
            driver = webdriver.Chrome()
        elif i == 1:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Edge()
        driver.maximize_window()
        driver.get(url)
        return driver

    def send_user_info(self,key,data):      #输入用户信息
        self.get_user_element(key).send_keys(data)

    def get_user_element(self,key):     #定位用户信息，获取element
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    # 获取随机数
    def get_range_user(self):
        user = ''.join(random.sample('123456789abcdef', 6))
        return user

    # 获取图片
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)  # 将页面截图保存
        code_element = self.get_user_element('getcode_num')  # 定位图片位置
        # print(code_element.location)  # 打印该元素的坐标
        left = code_element.location['x']  #
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)

    # 解析图片获取验证码
    def code_online(self,file_name):
        image = Image.open(file_name)
        text = pytesseract.image_to_string(image)
        return text

    def main(self):
        user_name_info = self.get_range_user()
        user_email = user_name_info + '@163.com'
        file_name = 'D:\pycharm\python3\demo\study\image1.png'
        code_text = self.code_online(file_name)
        self.send_user_info('user_email',user_email)
        self.send_user_info('user_name',user_name_info)
        self.send_user_info('password','111001')
        self.send_user_info('code_text',code_text)
        self.get_user_element('register_button').click()
        code_error = self.get_user_element('code_text_error')   #获取验证码错误图片的位置
        if code_error == None:
            print('注册成功！')
        else:
            print('注册失败！')
            self.driver.save_screenshot('D:\pycharm\python3\demo\study\error.png')  #保存图片
        time.sleep(5)
        self.driver.quit()

if __name__ == '__main__':
    for i in range(3):
        register = RegidterFunction('http://www.5itest.cn/register',i)
        register.main()