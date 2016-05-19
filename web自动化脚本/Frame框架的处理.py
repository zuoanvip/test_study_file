# -*- coding:utf-8 -*-
#在html中，<frameset>是框架结构的标签，<frame>是框架标签，<iframe>是定义内联的子窗口
#处理未嵌套的frame--frame有ID
driver.switch_to_frame('frame_ID')
#处理未嵌套的frame--frame无ID，根据frame的index来定位，起始为0
driver.switch_to_frame('0')
#处理嵌套的frame，对于嵌套的frame，处理的方式是先进入到iframe的父节点，再进入到子节点
#进入到父iframe
driver.switch_to_frame('test')
#进入到子iframe
driver.switch_to_frame('test2')

