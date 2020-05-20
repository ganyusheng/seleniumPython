# -*- coding: utf-8 -*-
from myself.operation_excel import OperationExcel
from myself.operation_json import OperationJson
from myself.dataconfig import DataConfig
import dataconfig
import json
from operation_mysql import OperationMysql

class GetData:
    def __init__(self):
        self.oper_excel = OperationExcel()
        self.oper_json = OperationJson()
        self.data = dataconfig
        self.oper_mysql = OperationMysql()

    def get_id_value(self,row):
        col = self.data.get_id()
        id = self.oper_excel.get_cell_data(row,col)
        return id

    def get_name_value(self,row):
        col = self.data.get_name()
        name = self.oper_excel.get_cell_data(row,col)
        return name

    def get_url_value(self,row):
        col = self.data.get_url()
        url = self.oper_excel.get_cell_data(row,col)
        return url

    def get_is_run_value(self,row):
        col = self.data.get_is_run()
        is_run = self.oper_excel.get_cell_data(row,col)
        if is_run == 'yes':
            Falg = True
        else:
            Falg = False
        return Falg

    def get_request_way_value(self,row):
        col = self.data.get_request_way()
        request_way = self.oper_excel.get_cell_data(row,col)
        return request_way

    def get_is_header_value(self,row):
        col = self.data.get_is_header()
        is_header = self.oper_excel.get_cell_data(row,col)
        if is_header == 'no':
            return None
        else:
            return is_header

    def get_case_dependent_value(self,row):
        col = self.data.get_case_dependent()
        case_dependent = self.oper_excel.get_cell_data(row,col)
        if case_dependent =='':
            return None
        else:
            return case_dependent

    def get_response_dependent_value(self,row):
        col = self.data.get_response_dependent()
        response_dependent = self.oper_excel.get_cell_data(row,col)
        if response_dependent == '':
            return None
        else:
            return response_dependent

    def get_data_dependent_value(self,row):
        col = self.data.get_data_dependent()
        data_dependent = self.oper_excel.get_cell_data(row,col)
        if data_dependent == '':
            return None
        else:
            return data_dependent

    def get_data_value(self,row):
        col = self.data.get_data()
        data = self.oper_excel.get_cell_data(row,col)
        if data == '':
            return None
        else:
            return data

    def get_data_for_json(self,row):
        data = self.oper_json.get_json_data(self.get_data_value(row))
        return data

    def get_expect_value(self,row):
        col = self.data.get_expect()
        expect = self.oper_excel.get_cell_data(row,col)
        return expect

    def get_result_value(self,row):
        col = self.data.get_result()
        result = self.oper_excel.get_cell_data(row,col)
        return result

    def write_data(self,row,value):
        col = self.data.get_result()
        self.oper_excel.write_value(row,col,value)

    def get_expect_from_mysql(self,row):
        sql = self.get_expect_value(row)
        data = self.oper_mysql.find_mydql_data(sql)
        return data