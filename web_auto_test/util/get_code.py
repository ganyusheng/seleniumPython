# -*- coding: utf-8 -*-

from PIL import Image
import time
import pytesseract

class GetCode():
    def __init__(self,driver):
        self.driver = driver

    def save_image(self,file_name):
        self.driver.save_screenshot(file_name)
        image_element = self.driver.find_element_by_id('getcode_num')
        left = image_element.location['x']
        top = image_element.location['y']
        right = image_element.size['width'] + left
        height = image_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left,top,right,height))
        img.save(file_name)
        time.sleep(2)
        #return img


    def code_online(self,file_name):
        self.save_image(file_name)
        image = open(file_name)
        #image = image.convert('RGB')
        code_text = pytesseract.image_to_string(image)
        time.sleep(2)
        if code_text == '':
            return '123'
        else:
            return code_text
