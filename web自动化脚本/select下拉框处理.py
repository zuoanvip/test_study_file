# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time as t

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
t.sleep(15)
element = driver.find_element_by_link_text(u'设置')
t.sleep(10)
ActionChains(driver).move_to_element(element).perform()
t.sleep(15)
driver.find_element_by_css_selector(".setpref").click()
select = Select(driver.find_element_by_name('NR'))
select.select_by_index(1)              #根据下拉列表的索引值
select.select_by_value('50')          #模糊匹配，根据下拉框的值
select.select_by_visible_text(u'每页显示50条')    #精确匹配，根据下拉框的值
driver.quit()