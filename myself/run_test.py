# -*- coding: utf-8 -*-
import json
from get_data import GetData
from run_methon import RunMethod
from operation_excel import OperationExcel
from common_util import CommonUtil
from dependent import Dependent
from operation_header import OperationHeader
from operation_json import OperationJson
from operation_mysql import OperationMysql
from send_emaile import SendEmail

class RunTest:
    def __init__(self):
        self.getdata = GetData()
        self.run_method = RunMethod()
        self.oper_excel = OperationExcel()
        self.common_util = CommonUtil()
        self.oper_mysql = OperationMysql()
        self.sen_mail = SendEmail()

    def run_test(self):
        id = 0
        pass_count = []
        fail_count = []
        row = self.oper_excel.get_data_lines()
        for id in range(1,row):
            is_run = self.getdata.get_is_run_value(id)
            if is_run:
                url = self.getdata.get_url_value(id)
                method = self.getdata.get_request_way_value(id)
                is_header = self.getdata.get_is_header_value(id)
                case_dependent = self.getdata.get_case_dependent_value(id)
                response_dependent = self.getdata.get_response_dependent_value(id)
                data_dependent = self.getdata.get_data_dependent_value(id)
                data = self.getdata.get_data_for_json(id)
                #expect = self.getdata.get_expect_from_mysql(id)
                expect = self.getdata.get_expect_value(id)
                result = self.getdata.get_result_value(id)
                if case_dependent != None:
                    self.dependent = Dependent(case_dependent)
                    dependent_data = self.dependent.dependent_key_values(id)
                    data[data_dependent] = dependent_data
                #print(type(expect))
                if is_header == 'write':
                    res = self.run_method.run_method(method, url, data)
                    #print(res['data']['url'])
                    res = json.loads(res)
                    #print(type(res))
                    oper_header = OperationHeader(res)
                    oper_header.write_cookie()
                elif is_header == 'yes':
                    oper_json = OperationJson('D:\pycharm\python2\\testdjango\demo\detaconfig\cookie.json')
                    is_header = oper_json.get_json_data('apsid')
                    cookie = {
                        'apsid':is_header
                    }
                    res = self.run_method.run_method(method,url,data,cookie)
                else:
                    res = self.run_method.run_method(method,url,data)
                #print(id,res,type(res),type(expect))
                #print(expect,res)
        #self.sen_mail.sen_main(pass_count,fail_count)

                if self.common_util.is_contain(expect,res):
                    self.getdata.write_data(id,'pass')
                    pass_count.append(id)
                    print('pass')
                else:
                    self.getdata.write_data(id, 'fail')
                    fail_count.append(id)
                    print('fail')
        print(len(pass_count))
        self.sen_mail.sen_main(pass_count, fail_count)

"""if self.common_util.is_queal(expect, res):
                    self.getdata.write_data(id, 'pass')
                    pass_count = pass_count.append(id)
                    print('pass')
                else:
                    self.getdata.write_data(id, 'fail')
                    fail_count = fail_count.append(id)
                    print('fail') """

if __name__ == "__main__":
    res = RunTest()
    print(res.run_test())
