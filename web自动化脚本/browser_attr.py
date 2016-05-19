# -*- coding:utf-8 -*-
from selenium import  webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.current_url           #获取当前页面的url
driver.page_source           #获取当前页面源码
driver.title                 #获取当前页面标题title
driver.name                  #获取测试浏览器名称
driver.back()                #返回
driver.forward()             #前进
driver.current_window_handle #获取当前windows窗口句柄
driver.window_handles        #获取浏览器所有句柄
driver.maximize_window()     #浏览器最大化
driver.close()               #关闭页面
driver.quit()                #退出驱动程序和关闭浏览器
driver.refresh()             #刷新页面


#WebElement类属性
element.size          #获取元素的大小
element.tag_name      #获取元素的HTML标记名称
element.text          #获取元素的文本

#WebElement类方法
element.clear()                  #清空内容
element.click()                  #点击
element.get_attribute('type')   #获取元素属性
element.is_displayed()           #元素是否可见，返回bool类型
element.is_enabled()             #元素是否可编辑，返回bool类型
element.is_selected()            #是否选择，返回bool类型
element.send_keys('selenium')  #输入
element.submit()                 #提交form表单
element.value_of_css_property()  #获取CSS属性值
