# -*- coding: utf-8 -*-
import unicodedata
import json
from idna import unicode
import operator

class CommonUtil:
    def is_contain(self,str_one,str_two):
        #if isinstance(str_one,unicode):
            #str_one =str_one.encode('unicode-escape').decode('string-escape')
        if str_one in str_two:
            Flag = True
        else:
            Flag = False
        return Flag

    def is_queal(self,dict_one,dict_two):
        if isinstance(dict_one,str):
            dict_one = json.loads(dict_one)
        if isinstance(dict_two,str):
            dict_two = json.loads(dict_two)
        return operator.eq(dict_one,dict_two)
        
