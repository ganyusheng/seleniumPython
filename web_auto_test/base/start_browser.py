# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import random
from PIL import Image
from selenium.webdriver.support import expected_conditions as EC    #使用此包对比title
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from PIL import Image
import pytesseract


driver = webdriver.Chrome()     #启动chrome浏览器
#driver = webdriver.Firefox()        #启动Firefox浏览器
driver.get('http://www.5itest.cn/register?goto=http%3A//www.5itest.cn/')    #打开网站
#time.sleep(10)
WebDriverWait(driver,30)
print(EC.title_contains('注册'))  #对比页面title是否正确
driver.maximize_window()
#element = driver.find_element_by_class_name('controls')
#EC.visibility_of_element_located(element)   #判断元素是否显示出来
locator = (By.CLASS_NAME,'controls')
WebDriverWait(driver,10).until(EC.visibility_of_element_located(locator))  #在driver页智能（找到了就退出，最多等10秒）查找10秒，看是否存在controls元素

driver.find_element_by_id('register_email').send_keys('1344830596@qq.com')  #通过id定位，输入email
'''
for i in range(5):
    user_email = ''.join(random.sample('123456789abcdefg',5))+'@163.com'    #random随机函数，从123456789abcdefg中随机生成5位字符,for循环是让它生成五个
    print(user_email)
'''
user_name_element_node = driver.find_elements_by_class_name('controls')[1]     #查找第二个controls父类
#user_name_element_node.driver.find_element_by_class_name('form-control input-lg').send_keys('kiv')   #通过父类找子类，并输入内容
driver.find_element_by_xpath('//*[@id="register_nickname"]').send_keys('kiv')
driver.find_element_by_name('password').send_keys('cde3CDE#')
driver.find_element_by_xpath('//*[@id="captcha_code"]').send_keys('aa')
email_element = driver.find_element_by_id('register_email') #查找register_email的元素
print(email_element.get_attribute('placeholder'))   #通过register_email元素获取placeholder属性值
email_element.send_keys('test@163.com')     #再次输入email
print(email_element.get_attribute('value'))     #获取email_element的属性值

driver.save_screenshot('D:\pycharm\python3\demo\study\image.png')   #将页面截图保存
code_element = driver.find_element_by_id('getcode_num')     #定位图片位置
print(code_element.location)   #打印该元素的坐标
left = code_element.location['x']   #
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top
im = Image.open('D:\pycharm\python3\demo\study\image.png')
img = im.crop((left,top,right,height))
img.save('D:\pycharm\python3\demo\study\image1.png')

image = Image.open('D:\pycharm\python3\demo\study\image1.png')      #打开图片
text = pytesseract.image_to_string(image)   #将图片内容转换成文本
print(text)
driver.find_element_by_xpath('//*[@id="captcha_code"]').send_keys(text)

driver.quit()