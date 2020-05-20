# -*- coding: utf-8 -*-
import logging
import os
import datetime



class UserLog(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)      #log级别
        #consle = logging.StreamHandler()    #日志流
        #logger.addHandler(consle)       #输出日志到控制台
        #consle.close()          #关闭流
        #logger.debug('111')
        #logger.removeHandler(consle)        #关闭控制台

        #文件名称
        base_dir = os.path.dirname(os.path.abspath(__file__))   #获取当前文件所在目录路径
        log_dir = os.path.join(base_dir,'logs') #拼接路径
        log_file = datetime.datetime.now().strftime('%Y-%m-%d')+'.log'  #以年月日命名文件
        log_name = log_dir+'\\'+log_file    #文件名
        #print(log_name)
        self.file_handle = logging.FileHandler(log_name,'a',encoding='utf-8')     #日志需要写入的文件
        self.file_handle.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(filename)s---> %(funcName)s %(levelno)s: %(levelname)s---> %(message)s')        #日志格式
        self.file_handle.setFormatter(formatter)     #写入的格式
        self.logger.addHandler(self.file_handle)
        #self.logger.debug('test5415415as5a416s516')      #日志内容
        #self.logger.removeHandler(self.file_handle)   #关闭
        #self.file_handle.close()  # 关闭文件流

    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)   #关闭
        self.file_handle.close()  # 关闭文件流

if __name__ == '__main__':
    log = UserLog()
    use = log.get_log()
    use.debug('test')
    log.close_handle()