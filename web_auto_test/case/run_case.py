# -*- coding: utf-8 -*-
import unittest
import os

class RunCase(unittest.TestCase):
    def test_case01(self):
        case_path = os.path.join(os.getcwd())    #获取当前case路径
        print(case_path)
        suite = unittest.defaultTestLoader.discover(case_path,'unittest_*.py')  #unittest_*.py文件的case存入suite中
        unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    unittest.main()