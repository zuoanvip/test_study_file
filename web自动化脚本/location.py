# -*- coding:utf-8 -*-
from selenium import webdriver
import time

class baidu(object):
    def __init__(self,driver):
        self.driver = driver

    def wait(self):
        time.sleep(3)
'''
二次定位找到登录按钮
'''
    def clickLogin(self):
        self.wait()
        self.driver.find_element_by_id('u1').find_element_by_class_name('lb').click()

    def typeUsername(self,username):
        self.wait()
        self.driver.find_element_by_id('TANGRAM__PSP_8__userName').send_keys('username')

    def typePassword(self,password):
        self.wait()
        self.driver.find_element_by_id('TANGRAM__PSP_8__password').send_keys('password')

    def clickButton(self):
        self.wait()
        self.driver.find_element_by_id('TANGRAM__PSP_8__submit').click()

    def getErrorText(self):
        self.wait()
        return self.driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_8__error']").text

    def login(self,username,password):
        self.wait()
        self.clickLogin()
        self.typeUsername(username)
        self.typePassword(password)
        self.clickButton()

