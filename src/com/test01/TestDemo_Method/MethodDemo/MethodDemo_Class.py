# -*- coding:utf-8 -*-
"""
这里对python的类进行剖析
1.定制类
"""
"""
定制类：
1.怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了：重写__str__方法
2.__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

3.如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环:。

4.要表现得像list那样按照下标取出元素，需要实现__getitem__()方法

5.实现切片：__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice

此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。

与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。

总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，
这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。


class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

"""
print('定制类实例1：')
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
    __repr__ = __str__
print('测试定制类：',Chain().status.users.timeline.list)

