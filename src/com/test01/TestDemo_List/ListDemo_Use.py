# -*- coding: utf-8 -*-
"""
    这里演示python高级特性
    1.切片
    2.迭代
    3.列表生成式
    4.生成器
"""
L=[]
# 模拟一个0-100的数组
for i in range(100):
    L.append(i)
"""取一个list或tuple的部分元素是非常常见的操作"""
print('切片部分：')
print('前10:',L[:10])
print('1-10,步进为2:',L[1:10:2])
print('倒数10:',L[-10:])
print('复制对象:',L[:])
print('扩展tuple:')
print((1,2,3,4,5,6,7)[:3])
print('扩展str:')
print('hellowrld'[0:5])

print('迭代部分--')
"""str,数组,元祖类型均可以被迭代，整形和数值型不能被迭代，可以用collection 下的Iterable判断数组是否可迭代"""
print('迭代实例1')
for i,val in enumerate(['a','b','c']):
    print(i,":",val)
print('迭代实例2')
for x,y,z in [(1,1,1),(2,2,2),(3,3,3)]:
    print(x,":",y,":",z)
"""列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式"""
print('列表生成式部分--')
print('一般用法：',list(range(1,11)))
print('进阶用法：',list(x*x for x in range(1,11)))
print('加入条件语句：',list(x*x for x in range(1,11)if x%2==0))
print('扩展str',[m.lower()+n for m in 'ABC' for n in 'XYZ'])
"""这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。"""
print("生成器部分---")
K= (x * x for x in range(10))
print(K)
print('打印数组K的第一个元素:',next(K))
print('迭代打印K：')
for n in K:
    print(n)
print('生成器扩展：斐波拉契数列')
def fib(max):
    n,a,b=0,1,1
    while n<max:
        yield b
        a,b=b,a+b
        n+=1
    return 'Done'
"""解析：这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。"""
for n in fib(6):
    print(n)#这里返回的yield的值



