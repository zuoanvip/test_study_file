# -*- coding:utf-8 -*-
from selenium import webdriver
import time
'''
元素定位方法的二次封装+封装百度登陆功能
'''
def wait():
    time.sleep(3)

def findId(driver,id):
    wait()
    d = driver.find_element_by_id(id)
    return d

def findName(driver,name):
    wait()
    d  = driver.find_element_by_name(name)
    return d

def findClassName(driver,name):
    wait()
    d = driver.find_element_by_class_name(name)
    return d

def findTagName(driver,name):
    wait()
    d = driver.find_element_by_tag_name(name)
    return d

def findLinkText(driver,text):
    wait()
    d = driver.find_element_by_link_text(text)
    return d

def findPLinkText(driver,text):
    wait()
    d = driver.find_element_by_partial_link_text(text)
    return d

def findXpath(driver,xpath):
    wait()
    d = driver.find_element_by_xpath(xpath)
    return d

def findCss(driver,css):
    wait()
    d = driver.find_element_by_css_selector(css)
    return d

def login(driver,username='username',password='password'):
    findxpath(driver,".//*[@id='u1']/a[7]").click()
    findId(driver,'TANGRAM__PSP_8__userName').send_keys(username)
    findId(driver,'TANGRAM__PSP_8__password').send_keys(password)
    findId(driver,'TANGRAM__PSP_8__submit').click()
