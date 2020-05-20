# -*- coding: utf-8 -*-
import sys
sys.path.append('D:\pycharm')
sys.path.append('D:\pycharm\python3')
sys.path.append('D:\pycharm\python3\demo')
sys.path.append('D:\pycharm\python3\demo\study')
sys.path.append('D:\pycharm\python3\demo\study\web_auto_test')
sys.path.append('D:\pycharm\python3\demo\study\web_auto_test\\base')
sys.path.append('D:\pycharm\python3\demo\study\web_auto_test\\business')
sys.path.append('D:\pycharm\python3\demo\study\web_auto_test\case')
sys.path.append('D:\pycharm\python3\demo\study\web_auto_test\config')
sys.path.append('D:\pycharm\python3\demo\study\web_auto_test\handle')
sys.path.append('D:\pycharm\python3\demo\study\web_auto_test\keyword_selenium')
sys.path.append('D:\pycharm\python3\demo\study\web_auto_test\log')
sys.path.append('D:\pycharm\python3\demo\study\web_auto_test\my_study')
sys.path.append('D:\pycharm\python3\demo\study\web_auto_test\page')
sys.path.append('D:\pycharm\python3\demo\study\web_auto_test\\report')
sys.path.append('D:\pycharm\python3\demo\study\web_auto_test\\util')
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import HTMLTestRunner
import os
import time
from log.user_log import UserLog



class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #cls.login = UserLog()
        #cls.logger = cls.login.get_log()
        cls.file_name = 'D:\pycharm\python3\demo\study\image1.png'  #静态全局变量
        cls.log = UserLog()
        cls.logger = cls.log.get_log()

    def setUp(self):
        print('测试开始前执行')
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.logger.info('This is chrome')
        self.driver.maximize_window()
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        print('测试完成后执行')
        #if sys.exc_info()[0]:
        for method_name,error in self._outcome.errors:  #_outcome.errors能获取当前运行case名称和错误信息
            if error:       #如果有错误信息
                case_name = self._testMethodName    #获取当前运行错误case的名称
                path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #获取当前文件目录的上一级目录
                file_path = path +'\\report\\'+case_name+'.png'     #存储路径
                self.driver.save_screenshot(file_path)  #截图
        time.sleep(3)
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    def test_login_email_error(self):
        email_error = self.login.login_email_error('34','111','1111',self.file_name)    #也就是cls.file_name
        return self.assertFalse(email_error,'case执行')   #判断结果是否为false,不为false时候 打印'case执行'
        #if email_error == True:
        #    print('注册成功，此case执行失败')
        #通过Assert判断是否为error

    def test_login_username_error(self):
        name_error = self.login.login_name_error('344', '111', '1111', self.file_name)
        self.assertFalse(name_error,'case执行')   #判断结果是否为false

    def test_login_password_error(self):
        password_error = self.login.login_password_error('344', '111', '1111', self.file_name)
        self.assertFalse(password_error,'case执行')   #判断结果是否为false

    def test_login_code_error(self):
        code_error = self.login.login_code_text_error('344', '111', '1111', self.file_name)
        self.assertFalse(code_error,'case执行')   #判断结果是否为false

    def test_login_success(self):
        success = self.login.user_business('344', '111', '1111', self.file_name)
        #print(self.file_name)
        self.assertFalse(success,'case执行')   #判断结果是否为false
        #self.driver.quit()

'''
def main():
    first = FirstCase()
    first.test_login_email_error()
    first.test_login_username_error()
    first.test_login_password_error()
    first.test_login_code_error()
    first.test_login_success()
'''

if __name__ == '__main__':
    #unittest.main()
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #获取当前文件目录的上一级目录
    file_path = path +'\\report\\'+'first_case.html'  #结果写入的文件路径
    #print(file_path)
    fp = open(file_path,'wb+')    #读写形式打开
    suite = unittest.TestSuite()
    #suite.addTest(FirstCase('test_login_email_error'))
    suite.addTest(FirstCase('test_login_username_error'))
    suite.addTest(FirstCase('test_login_success'))
    #unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream = fp,verbosity=2,title='测试结果title', description='测试结果description')    #htmltestrunner运行
    runner.run(suite)
    fp.close()