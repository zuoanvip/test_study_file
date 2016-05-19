# -*- coding:utf-8 -*-
'''
生成一个生成器两种方法一个是：(x for x in range(10));另一种是yield x
生成斐波那契数列，并获的指定位置的数
'''
def func(max):
    n,a,b=0,0,1
    while(n<max):
        yield a
        a,b=b,a+b
        n=n+1
'''
yield为一个生成器，若要输出其中的元素则使用for循环
for x in func：
    print x
'''
def getfuncvalue(gen,index):
    n=1
    for x in gen:
        if n==index:
            print x
        n=n+1
getfuncvalue(func(10),5)
