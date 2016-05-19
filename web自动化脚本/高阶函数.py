# -*- coding:utf-8 -*-
from math import sqrt
'''
一、基础
获得函数调用结果,可以把结果赋值给变量
x=abs(-10)
同样可以将函数本身赋值给变量,即变量可以指向函数
f=abs
f(abs)
二、传入函数
def add(x,y,f):
    return f1(x)+f2(y)
把函数作为参数传入,这样的函数称为高阶函数,函数式编程就是指这种高度抽象的编程范式
'''
'''
map/reduce函数
map()函数接收两个参数,一个是函数,一个是序列,map将传入的函数依次作用到序列的每个元素,
并把结果作为新的list返回
def f(x):
    return x*x
L=[1,2,3,4,5,6,7,8,9,10]
print map(f,L)
map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]) 将序列中的数字转化为字符串
***********************************************************************
reduce()函数必须接收两个参数,reduce把结果继续和序列的下一个元素做累积计算
def add(x,y):
    return x-y
L=[1,2,3]
print reduce(add,L)
'''
'''
map和reduce函数混合使用
char2num字符转化为整数
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
'''
'''
练习题：将输入的单词首字母大写，其余小写
def str_upper(x):
    return x[0].upper()+x[1:].lower()
L=['adam', 'LISA', 'barT']
print map(str_upper,L)
'''
'''
-------------------------------------------------------------------------
filter:接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素,
然后根据返回值是True还是False决定保留还是丢弃该元素。
如：删除一个序列中的偶数
def is_odd(n):
    return n%2==1
print filter(is_odd,range(10))
练习：查找100以内的素数(for 也可以有else语句)
def is_sushu(num):
    for i in range(2,101):
        if(i != num and num % i == 0) or num == 1:
            return 0
    return 1
print filter(is_sushu,range(1,101))
'''
'''
sorted()函数也是一个高阶函数,它还可以接收一个比较函数来实现自定义的排序
def cmpfunc(x,y):
    if x>y:
        return -1
    else:
        if x<y:
            return 1
        else:
            return 0
L=[12,3,15,34,23,76,123,45,23,67,11]
print sorted(L,cmpfunc)
'''


        
    






