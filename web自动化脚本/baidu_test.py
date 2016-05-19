# -*- coding:utf-8 -*-
from selenium import webdriver
import  unittest
from HTMLTestRunner import HTMLTestRunner
import time
class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = 'http://www.baidu.com'

    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id('kw').send_keys("HTMLTestRunner")
        driver.find_element_by_id('su').click()

    def tearDown(self):
        self.driver.quit()
#生成测试报告
'''
if __name__ =='__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(baidu("test_baidu_search"))
#定义报告存放路径
fp = open("./result.html",'wb')
#定义测试报告
runner = HTMLTestRunner(stream = fp,title = u'百度搜索测试报告',description =u'用例执行情况：')
runner.run(testunit)
fp.close()
'''
#自动生成测试报告文件名
if __name__ =='__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu('test_baidu_search'))
    #按照一定格式获取当前时间
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    #定义报告存放路径
    filename = './' + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream = fp,title = '百度搜索测试报告',description ='用例执行情况')
    runner.run(testunit)
    fp.close()

#项目集成测试报告
#制定测试用例的目录
test_dir = './test_case'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = test_dir + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream = fp,title = '测试报告',description ='用例执行情况')
    runner.run(testunit)
    fp.close()
#自动发邮件功能
import  smtplib
from email.mime.text import MIMEText
from email.header import Header
#发送邮箱服务器
smtpserver = 'smtp.sina.com'
#发送邮箱用户名/密码
user = 'username@sina.com'
password = '123456'
#发送邮箱
sender = 'username@sina.com'
#接收邮箱
receiver = 'receiver@126.com'
#发送邮件主题
subject = 'Python send email test'
#发送的附件
sendfile = open('d:\\test\\python\\log.txt','rb').read()
att = MIMEText(sendfile,'base64','utf-8')
att['Content-Type'] = 'application/octet-stream'
att['Content-Disposition'] = 'attachment; filename="log.txt"'
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot.attach(att)
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msgRoot.as_string())
smtp.quit()
