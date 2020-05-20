# -*- coding: utf-8 -*-


class DataConfig:
    id = 0
    name = 1
    url = 2
    is_run = 3
    request_way = 4
    is_header = 5
    case_dependent = 6
    response_dependent = 7
    data_dependent = 8
    data = 9
    expect = 10
    result = 11

def get_id():       #获取用例id
    return DataConfig.id

def get_name():
    return DataConfig.name

def get_url():
    return DataConfig.url

def get_is_run():
    return DataConfig.is_run

def get_request_way():
    return DataConfig.request_way

def get_is_header():
    return DataConfig.is_header

def get_case_dependent():
    return DataConfig.case_dependent

def get_response_dependent():
    return DataConfig.response_dependent

def get_data_dependent():
    return DataConfig.data_dependent

def get_data():
    return DataConfig.data

def get_expect():
    return DataConfig.expect

def get_result():
    return DataConfig.result
