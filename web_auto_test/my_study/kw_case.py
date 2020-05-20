# -*- coding: utf-8 -*-
from action_method import ActionMehtod
from load_excel import LoadExcel

class KwCase:
    def run_main(self):
        self.action_method = ActionMehtod()
        excel = LoadExcel('D:\pycharm\python3\demo\study\web_auto_test\config\keyword.xls')
        rows = excel.get_lines()
        if rows != None:
            for i in range(1,rows):
                is_run = excel.get_cell_value(i,3)
                if is_run == 'yes':
                    method = excel.get_cell_value(i,4)
                    send_value = excel.get_cell_value(i,5)
                    handle_value = excel.get_cell_value(i,6)
                    except_result = excel.get_cell_value(i,7)
                    except_result_value = excel.get_cell_value(i,8)
                    self.run_method(method,send_value,handle_value)
                    if except_result != '':
                        except_value = self.get_except_result_value(except_result_value)
                        if except_value[0] == 'text':
                            res = self.run_method(except_result)
                            if except_value[1] in res:
                                excel.write_value(i,'pass')
                            else:
                                excel.write_value(i,'fail')
                        elif except_value[0] == 'element':
                            res = self.run_method(except_result,except_value[1])
                            if res:
                                excel.write_value(i,'pass')
                            else:
                                excel.write_value(i,'fail')
                        else:
                            return '无else'
                    else:
                        print('无预期结果！')


    def get_except_result_value(self,data):
        return data.split('=')

    def run_method(self,method,send_value = '',handle_value = ''):
        method_value = getattr(self.action_method,method)       #运行self.action_method类里面的method方法
        if send_value == '' and handle_value != '':
            res = method_value(handle_value)
        elif send_value != '' and handle_value != '':
            res = method_value(send_value,handle_value)
        elif send_value != '' and handle_value == '':
            res = method_value(send_value)
        else:
            res = method_value()
        return res

if __name__ == '__main__':
    run = KwCase()
    run.run_main()