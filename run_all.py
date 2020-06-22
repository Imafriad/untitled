#coding:utf-8
import time,datetime,os
import unittest
import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
#from common.Send_mail import Send_mail

def all_case():
    case_dir = 'E:\\Users\\Administrator\\PycharmProjects\\untitled\case'
    test_case = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir, pattern='test*.py', top_level_dir=None)

    for case in discover:
        test_case.addTest(case)
    print(test_case)
    '''
    for case in discover:
        for i in case:
            test_case.addTest(i)    
    '''
    return test_case

if  __name__ == '__main__' :
    now_time=time.strftime('%Y_%m_%d %H_%M_%S',time.localtime())
    report_path = ("E:\\Users\\Administrator\\PycharmProjects\\untitled\\report\\"+now_time+".html")
    today=datetime.date.today()
    with open(report_path,'wb') as f:
        runner=HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title='自动化测试',
            description='这是'+str(today)+'日的测试结果',
            verbosity=2)
        runner.run(all_case())


    def send_mail(file_new):
        # -----------1.跟发件相关的参数------
        smtpserver = 'mail.fsg.com.cn'  # 发件服务器
        port = 0  # 端口
        username = 'xiaolei.chen@fsg.com.cn'  # 发件箱用户名
        password = 'QhYHa%AG'  # 发件箱密码
        sender = 'XXly@cedex.cn'  # 发件人邮箱
        receiver = ['1300153983@com.cn']  # 收件人邮箱

    print('发送成功')