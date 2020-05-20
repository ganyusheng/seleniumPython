# -*- coding: utf-8 -*-
import unittest

class FirstCase01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('所有case执行之前执行')

    @classmethod
    def tearDownClass(cls):
        print('所有case执行之后执行')

    def setUp(self):    #case的前置条件
        print('case的前置条件')

    def tearDown(self): #case的后置条件
        print('case的后置条件')

    @unittest.skip('不执行此条case')
    def testfirst01(self):          #如果要以main函数运行需要以test开头
        print('这是第一条测试')

    def testfirst02(self):
        print('第二条测试')

    def testfirst03(self):
        print('第3条测试')



if __name__ == '__main__':
    #unittest.main()    #运行类里面的所有用例,默认按升序排列执行
    suite = unittest.TestSuite()        #创建一个存放用例的容器
    suite.addTest(FirstCase01('testfirst02'))        #往容器增加用例
    suite.addTest(FirstCase01('testfirst01'))        #往容器增加用例
    suite.addTest(FirstCase01('testfirst03'))        #往容器增加用例
    unittest.TextTestRunner().run(suite)        #运行用例   #suite = unittest.TestSuite()  suite.addTest(类名(方法名'))  unittest.TextTestRunner().run(suite)


