# -*- coding: utf-8 -*-
from PIL import Image
import pytesseract


image = Image.open('D:\pycharm\python3\demo\study\image1.png')
text = pytesseract.image_to_string(image)
print(text)