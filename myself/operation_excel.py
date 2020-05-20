# -*- coding: utf-8 -*-
import xlrd
from xlutils.copy import copy

class OperationExcel:
    def __init__(self,file_name = None,sheet_id = None):
        if file_name != None:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = 'D:\pycharm\python2\\testdjango\demo\detaconfig\case1.xls'
            self.sheet_id = 0
        self.data = self.open_excel()

    def open_excel(self):
        excel_data = xlrd.open_workbook(self.file_name) #打开excel文件
        data = excel_data.sheets()[self.sheet_id]   #获取sheet内容
        return data

    def get_cell_data(self,row,col):
        cell_data = self.data.cell(row,col).value   #获取sheet内的某个单元格内容
        #print(cell_data)
        return cell_data

    def write_value(self,row,col,value):
        open_excel = xlrd.open_workbook(self.file_name)     #打开excel
        copy_excel = copy(open_excel)       #复制excel内容   需要from xlutils.copy import copy
        sheet_data = copy_excel.get_sheet(0)    #获取复制的excel  的sheet内容
        sheet_data.write(row,col,value)     #往sheet内容单元格写入内容
        copy_excel.save(self.file_name)     #保存

    def get_data_lines(self):       #获取所有行数
        data = self.data
        return data.nrows

    def get_col_value(self,col_id = None):      #获取一列数据
        if col_id != None:
            col_value = self.data.col_values(col_id)
        else:
            col_value = self.data.col_values(0)
        return col_value

    def get_row_value(self,row):        #获取一列数据
        row_data = self.data.row_values(row)
        return row_data

    def get_case_row(self,case_id):     #根据依赖用例id获取该id所在的行号
        num = 0
        col_data = self.get_col_value()
        for coldatat in col_data:
            if case_id in coldatat:
                return num
            num = num + 1

    def get_case_row_data(self,case_id):        #根据用例id获取该用例的整行数据
        row_num = self.get_case_row(case_id)
        row_data = self.get_row_value(row_num)
        return row_data


if __name__ == '__main__':
    oper_excel = OperationExcel()
    print(oper_excel.get_cell_data(2,9))
    print(oper_excel.get_data_lines())