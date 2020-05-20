# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
import time
import os
import ddt
from rg_business import RegisterBusiness
import HTMLTestRunner
from excel_util import ExcelUtil

ex = ExcelUtil()
data = ex.get_data()
#lens = len(data)


@ddt.ddt
class RegisterRun(unittest.TestCase):
    def setUp(self):
        # print('测试开始前执行')
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        # print('测试完成后执行')
        # if sys.exc_info()[0]:
        for method_name, error in self._outcome.errors:  # _outcome.errors能获取当前运行case名称和错误信息
            if error:  # 如果有错误信息
                case_name = self._testMethodName  # 获取当前运行错误case的名称
                path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 获取当前文件目录的上一级目录
                file_path = path + '\\report\\' + case_name + '.png'  # 存储路径
                self.driver.save_screenshot(file_path)  # 截图
        time.sleep(3)
        self.driver.quit()

    '''
    @ddt.data(      #ddt数据
        ['12','kiv111','cde33333','321','user_email_error','请输入有效的电子邮件地址'],
        ['qq.com','kiv111','cde33333','321','user_email_error','请输入有效的电子邮件地址'],
        ['12qq.com','kiv111','cde33333','321','user_email_error','请输入有效的电子邮件地址'],
    )

    @ddt.unpack     #解包
    '''

    @ddt.data(*data)
    def test_register_case(self,data):
        email, name, password, code, assertCode, assertText = data # 为data里的每一个字段赋值，赋值到相应字段名
        email_error = self.login.register_function(email, name, password, code, assertCode,assertText)  # 也就是cls.file_name
        return self.assertFalse(email_error, 'case执行失败')  # 判断结果是否为false,不为false时候 打印'case执行'
        # if email_error == True:
        #    print('注册成功，此case执行失败')
        # 通过Assert判断是否为error
    '''
    def setUp(self):    #用例执行前执行
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://www.5itest.cn/register')
        self.register_business = RegisterBusiness(self.driver)

    def tearDown(self):     #用例执行后执行
        time.sleep(3)
        self.driver.quit()

    #@ddt.unpack
    @ddt.data(*data)
    def test_run_register(self,data):
        email,name,password,code,assertCode,assertText = data
        #register_business.register_business(email,name,password,code)
        res = self.register_business.register_function(email,name,password,code,assertCode,assertText)
        return self.assertFalse(res,'case执行失败')
    '''

if __name__ == '__main__':
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #获取当前文件目录的上一级目录
    file_path = path +'\\report\\'+'first_case.html'  #结果写入的文件路径
    fp = open(file_path,'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(RegisterRun)
    runner = HTMLTestRunner.HTMLTestRunner(stream = fp,verbosity = 2,title = 'title',description = 'yes')
    runner.run(suite)
