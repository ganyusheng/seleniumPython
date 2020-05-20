# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText

class SendEmail:
    global email_host
    global send_user
    global password
    send_user = 'gan19945700625@163.com'
    password = 'MEQNQOLNDAFYMTDS'
    email_host = 'smtp.163.com'

    def send_mail(self,user_list,sub,content):
        user = 'kiv'+'<'+send_user+'>'      #定义由谁发送
        message =MIMEText(content,_subtype='plain',_charset='utf-8')    #定义消息格式
        message['From'] = user      #由谁发送
        message['Subject'] = sub    #发送主题
        message['To'] = ';'.join(user_list)     #发送给谁
        server = smtplib.SMTP()     #创建邮件服务
        server.connect(email_host)      #链接服务
        server.login(send_user,password)        #登录服务
        server.sendmail(send_user,user_list,message.as_string())    #发送邮件
        server.close()      #关闭服务

    def sen_main(self,pass_count,fail_count):
        pass_num = float(len(pass_count))
        fail_num = float(len(fail_count))
        count_num = pass_num+fail_num
        pass_result = '%0.2f%%'%(pass_num/count_num*100)
        fail_result = '%0.2f%%'%(fail_num/count_num*100)
        user_list = ['1344830596@qq.com']
        sub = '接口测试结果'
        content = '此次一共运行接口个数为%s个,通过个数为%s,失败个数为%s,通过率为%s,失败率为%s'%(count_num,pass_num,fail_num,pass_result,fail_result)
        self.send_mail(user_list,sub,content)



