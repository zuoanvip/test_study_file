# -*- coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
#alert主要有text、dismiss、accept、send_keys四种方法
#获取alert弹出警告框的text
driver.switch_to_alert().text
#接受警告框
driver.switch_to_alert().accept()
#confirm确认框的处理
driver.switch_to_alert().accept()
#confirm拒绝确认框
driver.switch_to_alert().dismiss()
#promp是javascript中的一个方法
driver.switch_to_alert().send_keys('selenium')
driver.switch_to_alert().accept()

