# -*- coding:utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('http://localhost:8080/devilfish/login/auth')
time.sleep(10)
driver.find_element_by_id('username').send_keys('admin')
driver.find_element_by_id('password').send_keys('111111')
time.sleep(10)
driver.find_element_by_xpath('//*[@id="loginForm"]/div[3]/div[2]/button').click()
#等待页面元素可见的时候操作，会设置一定范围的时间，如果在时间范围内，元素可见，就执行操作，元素不可见，就会引发TimeoutException的异常
so = WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="loginForm"]/div[3]/div[2]/button')))
#是指定页面元素的文本位置，一般用于验证一个文本信息或者错误的信息
WebDriverWait(driver,10).until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR,"#TANGRAM__PSP_8__error"),u'请您填写手机/邮箱/用户名'))
#visibility_of_element_located(locator)是元素可见后再执行其他的操作
element=WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((By.XPATH,".//*[@id='lh']/a[3]")))
print element.text



