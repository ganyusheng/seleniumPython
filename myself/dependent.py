# -*- coding: utf-8 -*-
from operation_excel import OperationExcel
from get_data import GetData
from run_methon import RunMethod
from jsonpath_rw import jsonpath,parse
import json

class Dependent:
    def __init__(self,case_id):
        self.case_id = case_id
        self.oper_excel = OperationExcel()
        self.data = GetData()
        self.run = RunMethod()

    def dependent_run(self):        #运行依赖的用例
        case_row = self.oper_excel.get_case_row(self.case_id)
        method = self.data.get_request_way_value(case_row)
        url = self.data.get_url_value(case_row)
        data = self.data.get_data_for_json(case_row)
        header = self.data.get_is_header_value(case_row)
        res = self.run.run_method(method,url,data,header)
        return res

    def dependent_key_values(self,row):     #获取需要依赖键的值
        response_data = self.dependent_run()    #运行依赖用例，获取其返回值
        requests_data = self.data.get_response_dependent_value(row)  #获取返回值里的某个键的值
        response_data = json.loads(response_data)   #将json数据转换成python可识别的对象
        json_exe = parse(requests_data)     #定义一个规则，以json格式去格式化接口返回的数据
        mable = json_exe.find(response_data)    #按照规则来查找整个结果集
        return [math.value for math in mable]   #官方写法，从结果集查找某部分数据

if __name__ == '__main__':
    dep = Dependent('Imooc-11')
    print(dep.dependent_key_values(11))
    """order = {
        "data": {
            "_input_charset": "utf-8",
            "body": "慕课网订单-1710141907182334",
            "it_b_pay": "1d",
            "notify_url": "http://order.imooc.com/pay/notifyalipay",
            "out_trade_no": "1710141907182334",
            "partner": "2088002966755334",
            "payment_type": "1",
            "seller_id": "yangyan01@tcl.com",
            "service": "mobile.securitypay.pay",
            "sign": "kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D",
            "sign_type": "RSA",
            "string": "_input_charset=utf-8&body=慕课网订单-1710141907182334&it_b_pay=1d&notify_url=http://order.imooc.com/pay/notifyalipay&out_trade_no=1710141907182334&partner=2088002966755334&payment_type=1&seller_id=yangyan01@tcl.com&service=mobile.securitypay.pay&subject=慕课网订单-1710141907182334&total_fee=299&sign=kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D&sign_type=RSA",
            "subject": "慕课网订单-1710141907182334",
            "total_fee": 299
        },
        "errorCode": 1000,
        "errorDesc": "成功",
        "status": 1,
        "timestamp": 1507979239100
    }
    res = "data.out_trade_no"
    json_exe = parse(res)
    madle = json_exe.find(order)
    print([math.value for math in madle][0], '\n', order, '\n', res, '\n', json_exe, '\n', madle)
"""