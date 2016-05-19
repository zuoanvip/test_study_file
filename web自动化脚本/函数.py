# -*- coding:utf-8 -*-
'''
----------------------------------------------------------------
返回函数,函数的返回值不再是一个具体的值,而是一个函数
def lazy_sum(*args):
    def sum():
        ax=0
        for x in args:
            ax=ax+x
        return ax
    return sum

f=lazy_sum(1,2,3,4,5,6,7,8,9)
print f
print f()
'''
'''
---------------------------------------------------------------
闭包:返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
例1：
def plus(number):
    def plus_in(number_in):
        print str(number_in) + "\r\n"
        return number+number_in
    return plus_in
v1=plus(20)
print v1(100)
例2：
def count():
    fs = []
    for i in range(1,4):
        def f(j):
            def g():
                return j*j
            return g
        fs.append(f(i))
    return fs
f1,f2,f3=count()
print f1()
print f2()
print f3()
'''
'''
----------------------------------------------------------------
关键字lambda表示匿名函数,冒号前面的x表示函数参数.
匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
eg:map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
'''
'''
print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
def build(x, y):
    return lambda: x * x + y * y
b = build(2,3)
print b()
'''
'''
----------------------------------------------------------------
装饰器
import time
 
def timeit(func):
    def wrapper():
        start = time.clock()
        func()
        end =time.clock()
        print 'used:', end - start
    return wrapper
@timeit
def foo():
    print 'in foo()'
@timeit与foo=timeit(foo)完全等价
'''


