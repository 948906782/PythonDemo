# -*- coding: utf-8 -*-
"""这里解决廖雪峰老师留下来的问题"""
print('调用函数章节--')
n1 = 255
n2 = 1000
print(hex(n1),hex(n2))

print('定义函数章节--')
import math
def quadratic(a,b,c):
    tem=b*b-4*a*c
    if tem>=0:
        print(math.sqrt(tem))
        return ((-b+math.sqrt(tem))/(2*a),(-b-math.sqrt(tem))/(2*a))
    else:
        print('error')
print('ax2 + bx + c = 0——>quadratic(2, 3, 1)',quadratic(2, 3, 1))

print('函数的参数--汉诺塔的移动')
def move(n,a,b,c):
    if n==0:
        return
    elif n==1:
        print('MOVE %s TO %s' % (a, c))
    else:
        move(n-1,a,c,b)
        print('MOVE %s TO %s BY %s' % (a, c, b))
        move(n-1,b,a,c)
move(3,'A','B','C')

print("python 实现杨辉三角")
def triangles(n):
    L = [1]  # 定义一个list[1]
    while True:
        yield L  # 打印出该list
        L = [L[x] + L[x + 1] for x in range(len(L) - 1)]  # 计算下一行中间的值（除去两边的1）
        L.insert(0, 1)  # 在开头插入1
        L.append(1)  # 在结尾添加1
        if len(L) > n:  # 仅输出10行
            break
a=triangles(3)
for i in a:
    print(i)

print("map(使用实例）")
"""利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']："""
def normalize(name):
    return str(name[0]).upper()+str(name[1:len(name)]).lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
"""Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积："""
print("map(使用实例2）")
from functools import reduce

def prod(L):
    def acou(x,y):
        return x*y
    return reduce(acou,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
import functools
print('装饰者问题1：')
def log(func):
    def wrap(*args,**kw):
        print('begin call..')
        res=func(*args,**kw)
        print('end call...')
        return res
    return wrap
@log
def exam():
    print('do something...')
exam()
"""
再思考一下能否写出一个@log的decorator，使它既支持：

@log
def f():
    pass
又支持：

@log('execute')
def f():
    pass
"""
print('装饰者问题2：')
def log2(args=0):
    def wrap(func):
        print('call method:%s'%(func.__name__))
        return func
    if isinstance(args,str):
        print(args)
        return wrap
    else:
        return wrap
@log2()
def today():
    print('today')

@log2('next')
def tomorrow():
    print('tomorrow')
today()
tomorrow()