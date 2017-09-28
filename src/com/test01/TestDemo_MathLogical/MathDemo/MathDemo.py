# -*- coding: utf-8 -*-
"""
    函数编程
    1.高阶函数：函数本身也可以赋值给变量，即：变量可以指向函数
    2.map/reduce
    3.filter
    4.排序
    1.1.2 返回函数
    1.1.3 匿名函数
    1.1.4 装饰器
"""
def couts(x):
    return x*x
def calc(x,y,f):
    return f(x)+f(y)
print('高阶函数使用示例：')
"""把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式"""
f=couts
print(f)
rs=calc(2,3,f)
print(rs)

print('map/reduce 使用实例：')
def counts2(x):
    return x*x
r=map(counts2,[1,2,3,4])
G=list(r)
print('map():',G)
print('map() str扩展:',list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
"""reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)"""
from functools import reduce
def ads(x,y):
    return x+y
print('reduce（）：',reduce(ads,[1,2,3,4,5]))

print('Filter 使用实例：')
"""
Python内建的filter()函数用于过滤序列。
和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素
filter()这个高阶函数，关键在于正确实现一个“筛选”函数。
注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，
需要用list()函数获得所有结果并返回list
"""
def is_odd(n):
    return n%2==1
print('1.过滤偶数，打印奇数：',list(filter(is_odd,[n for n in range(10)])))
def not_empty(n):
    return n and n.strip()
print('2.过滤空字符，打印字符串：',list(filter(not_empty,['A','','C','','E'])))
"""
用filter求素数

计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：

首先，列出从2开始的所有自然数，构造一个序列：

2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：

3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：

5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取新序列的第一个数5，然后用5把序列的5的倍数筛掉：

7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

不断筛下去，就可以得到所有的素数。
"""
print("filter求素数")
def jisu():
    n=1
    while True:
        n+=2
        yield n

def _selector_(n):
    return lambda x: x%n>0
def gersusu():
    yield 2
    it=jisu()
    while True:
        n=next(it)
        yield n
        it=filter(_selector_,it)
O=[]
for n in gersusu():
    if n<1000:
        O.append(n)
    else:
        break
print(O)
"""
排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。

"""
print("排序使用实例1(按绝对值排序）：",sorted([36, 5, -12, 9, -21], key=abs))
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0].lower()
L2 = sorted(L, key=by_name)
print(L,'按名称排序：',L2)
def by_score(t):
    return -t[1]
L2=sorted(L,key=by_score)
print(L,'按成绩排序：',L2)

"""
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
"""
def calc_sum(*args):#这里立即求和
    ax=0
    for n in args:
        ax+=n
    return ax

def lazy_sum(*args):
    def adm():
        ax = 0
        for n in args:
            ax += n
        return ax
    return adm
print('立即求和：',calc_sum(1,3,5))
f=lazy_sum(1,3,5)
print('不求和，返回对象：',f)
print('现在才开始求和:',f())
"""
闭包
返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
"""
def countsadd():
    def f1(i):
        def f2():
            return i+i
        return  f2
    fs=[]
    for n in range(1,4):
        fs.append(f1(n))
    return fs
z1,z2,z3=countsadd()
print('闭包实例：',z1(),'\t',z2(),'\t',z3())

"""当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便
在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，
而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。

decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。
"""

print('匿名函数实例：求10内所有的奇数\n',list(filter((lambda x:x%2>0),(x for x in range(10)))))
print('装饰器实例1：')
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2013-01-02')
now()
import functools
def log2(text):
    def decorate(func):
        @functools.wraps(func)
        def wrap(*args,**kw):
            print('%s %s()'%(text,func.__name__))
            return func(*args,**kw)
        return wrap
    return decorate
@log2('execute')
def now2():
    print('2014-01-02')
print('装饰者实例2：')
now2()