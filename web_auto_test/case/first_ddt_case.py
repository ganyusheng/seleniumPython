# -*- coding: utf-8 -*-
import ddt
import unittest
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import HTMLTestRunner
import os
import time
from util.excel_util import ExcelUtil

ex = ExcelUtil()
data = ex.get_data()
#print(data)

#邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
@ddt.ddt    #引用ddt
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        #print('测试开始前执行')
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        #print('测试完成后执行')
        #if sys.exc_info()[0]:
        for method_name,error in self._outcome.errors:  #_outcome.errors能获取当前运行case名称和错误信息
            if error:       #如果有错误信息
                case_name = self._testMethodName    #获取当前运行错误case的名称
                path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #获取当前文件目录的上一级目录
                file_path = path +'\\report\\'+case_name+'.png'     #存储路径
                self.driver.save_screenshot(file_path)  #截图
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
        email,name,password,code,assertCode,assertText = data   #为data里的每一个字段赋值，赋值到相应字段名
        email_error = self.login.register_function(email,name,password,code,assertCode,assertText)    #也就是cls.file_name
        return self.assertFalse(email_error,'case执行失败')   #判断结果是否为false,不为false时候 打印'case执行'
        #if email_error == True:
        #    print('注册成功，此case执行失败')
        #通过Assert判断是否为error


if __name__ == '__main__':
#    unittest.main()
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #获取当前文件目录的上一级目录
    file_path = path +'\\report\\'+'first_case.html'  #结果写入的文件路径
    fp = open(file_path,'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)   #加载类里面的case
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title='This is title',description='description')    #将报告写入file_path文件
    runner.run(suite)
