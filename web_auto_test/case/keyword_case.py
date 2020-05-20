# -*- coding: utf-8 -*-
from excel_util import ExcelUtil
from actionMethod import ActionMethod


class KeyWordCase:
    def run_main(self):
        self.action_method = ActionMethod()
        handle_excel = ExcelUtil('D:\pycharm\python3\demo\study\web_auto_test\config\keyword.xls')
        case_lines = handle_excel.get_lines()       #获取行数
        if case_lines != None:
            for i in range(1,case_lines):       #循环行数，执行每一条case
                is_run = handle_excel.get_cell_value(i,3)
                #handle_excel.write_value(i,'test')
                #continue
                print(is_run)
                if is_run == 'yes':     #是否执行
                    method = handle_excel.get_cell_value(i, 4)
                    send_value = handle_excel.get_cell_value(i, 5)
                    handle_value = handle_excel.get_cell_value(i, 6)
                    except_result_method = handle_excel.get_cell_value(i, 7)
                    except_result = handle_excel.get_cell_value(i, 8)
                    #''而不是None
                    #if send_value:
                    self.run_method(method,send_value,handle_value)   #执行action_method方法
                    #self.action_method.quit_browser()
                    if except_result_method != '':
                        except_value = self.get_except_result_value(except_result)
                        if except_value[0] == 'text':
                            print('------',except_result_method)
                            result = self.run_method(except_result_method)
                            print(result)
                            if except_value[1] in result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                        elif except_value[0] == 'element':
                            result = self.run_method(except_result_method,except_value[1])
                            if result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                        else:
                            print('没有else')
                    else:
                        print('预期结果为空')



        # 获取行数
        #循环行数，执行每一条case
            #是否执行
            #拿到操作值
            #拿到输入数据
            #是否输入数据
                #执行方法（输入数据，操作元素）
            #没有输入数据
                #执行方法（操作元素）
    #获取预期结果值
    def get_except_result_value(self,data):
        return data.split('=')


    def run_method(self,method,send_value = '',handle_value = ''):
        method_value = getattr(self.action_method, method)
        print(send_value)
        if send_value == '' and handle_value != '':
            result = method_value(handle_value)
        elif send_value != '' and handle_value != '':
            result = method_value(send_value,handle_value)
        elif send_value != '' and handle_value == '':
            result = method_value(send_value)
        else:
            result = method_value()
        return result

if __name__ == '__main__':
    run = KeyWordCase()
    run.run_main()