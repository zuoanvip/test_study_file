# -*- coding:utf-8 -*-
from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
# 1、move_to_element()鼠标悬停；鼠标悬停在元素上，才会显示需要的元素；2、
locator=driver.find_element_by_link_text(u'设置')
ActionChains(driver).move_to_element(locator).perform()
#2、context_click()鼠标右击
content=driver.find_element_by_xpath(".//*[@id='yao-main']/div/div[4]/div[1]/div[2]/div/div[1]/div[1]/span/span")
ActionChains(driver).context_click(content).perform()
#3、double_click()双击元素
content=driver.find_element_by_xpath(".//*[@id='yao-main']/div/div[4]/div[1]/div[2]/div/div[1]/div[1]/span/span")
ActionChains(driver).double_click(content).perform()
#4、click_and_hold 在元素上按住鼠标左键
content=driver.find_element_by_xpath(".//*[@id='yao-main']/div/div[4]/div[1]/div[2]/div/div[1]/div[1]/span/span")
ActionChains(driver).click_and_hold(content).perform()
#5、release()鼠标释放，在调用click_and_hold()方法，鼠标并没有释放
ActionChains(driver).click_and_hold(hold).release()
#send_keys 输入内容
from selenium.webdriver.common.keys import Keys      #键盘事件


