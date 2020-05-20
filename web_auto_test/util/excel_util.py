# -*- coding: utf-8 -*-
import xlrd
from xlutils.copy import copy

class ExcelUtil:
    def __init__(self,excel_path = None,index = None):
        if excel_path == None:
            self.excel_path = 'D:\pycharm\python3\demo\study\web_auto_test\config\casedata.xls'
        else:
            self.excel_path = excel_path
        if index == None:
            self.index = 0
        else:
            self.index = index
        self.data = xlrd.open_workbook(self.excel_path)     #打开excel
        self.table = self.data.sheets()[self.index]     #获取sheet数据
        #self.rows = self.table.nrows   #获取行数
        #[[],[]]

    def get_data(self):     # 获取excel数据，按照每行一个list，添加到一个大的list里面
        result = []
        row = self.get_lines()
        if row != None:
            for i in range(row):
                col = self.table.row_values(i)
                result.append(col)
            return result
        return None

    def get_lines(self):
        row = self.table.nrows  #获取行数
        if row >= 1:
            return row
        return None

    def get_cell_value(self,row,col):   #获取单元格数据
        if self.get_lines() > row:
            cell_value = self.table.cell(row,col).value
            return cell_value
        return None

    def write_value(self,row,value):  #写入数据,xlrd的写入会覆盖之前的内容，需要用xlutils
        read_data = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_data)    #复制一份表格数据
        write_data.get_sheet(0).write(row,9,value)  #往复制数据的第一个sheet的某个单元格写入值
        write_data.save(self.excel_path)   #保存

if __name__ == '__main__':
    ex = ExcelUtil()    #excel最好用后缀为xls的文件
    #print(ex.get_cell_value(10,4))
    print(ex.get_data())
    #print(ex.write_value(7,'test'))