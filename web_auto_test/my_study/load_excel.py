# -*- coding: utf-8 -*-
import xlrd
from xlutils.copy import copy

class LoadExcel:
    def __init__(self,file_path = None,index = None):
        if file_path == None:
            self.file_path = 'D:\pycharm\python3\demo\study\web_auto_test\config\casedata.xls'
        else:
            self.file_path = file_path
        if index == None:
            self.index = 0
        else:
            self.index = index
        self.open = xlrd.open_workbook(self.file_path)       #打开excel文件
        self.table = self.open.sheets()[self.index]      #获取第一个sheet

    def get_row_value(self,row):
        row_data = self.table.row_values(row)
        return row_data

    def get_lines(self):
        row = self.table.nrows
        if row >= 1:
            return row
        return None

    def get_data(self):
        result = []
        rows = self.get_lines()      #获取行数
        #print(rows)
        if rows != None:
            for i in range(rows):
                data = self.table.row_values(i)
                result.append(data)
            return result
        return None

    def get_cell_value(self,row,col):
        if self.get_lines() > row:
            data = self.table.cell(row,col).value
            return data
        return None

    def write_value(self,row,value):
        open = xlrd.open_workbook(self.file_path)
        write_data = copy(open)
        write_data.get_sheet(0).write(row,9,value)
        write_data.save(self.file_path)

if __name__ == '__main__':
    ex = LoadExcel()    #excel最好用后缀为xls的文件
    print(ex.get_data())
    #print(ex.get_lines())
