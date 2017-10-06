# -*- coding: utf-8 -*-
"""Generator专题：
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，
不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，
从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
要创建一个generator，有很两种方法：
第一种方法：只要把一个列表生成式的[]改成()，就创建了一个generator：
第二种方法：如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
"""
print('例子：斐波拉契数列')
def fib(nax):
    a=[1,1]
    n=1
    while n<nax:
        yield a
        a.append(0)
        a[n+1]=a[n-1]+a[n]
        n+=1

print(fib(10))
# for i in fib(10):
#     print(i)

import os
print(os.name)
# print(os.uname())#注意uname()函数在Windows上不提供
print(os.path)
from PIL import Image
rm=Image.open('j:/a.jpg')
w,h=rm.size
print (w,h)





