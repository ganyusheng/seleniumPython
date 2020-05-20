# -*- coding: utf-8 -*-
import pymysql
import json

class OperationMysql:
    def __init__(self):
        self.connect = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='cde3CDE#',
            db='le_study',
            charset='utf8',
            cursorclass = pymysql.cursors.DictCursor        #输出的结果为字典类型
        )   #链接数据库

    def find_mydql_data(self,sql):
        cur = self.connect.cursor()  # 创建游标
        cur.execute(sql)
        res = cur.fetchone()
        res = json.dumps(res)
        cur.close()
        return res

if __name__ == '__main__':
    mysql = OperationMysql()
    data = mysql.find_mydql_data('select * from web_user where name = "test"')
    print(data)