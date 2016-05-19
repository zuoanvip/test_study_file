# -*- coding:utf-8 -*-
from email.mime.text import  MIMEText
from email.header import Header
import smtplib

def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body,'html')
    msg['Subject'] = Header("自动化测试报告",'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect("smtp.126.com")
    smtp.login("zuoqi2018@126.com",'shawn6495')
    smtp.sendmail("zuoqi2018@126.com","1076305700@qq.com",msg.as_string())
    smtp.quit()
    print "email has send out !"

send_mail("D:\\123456.txt")