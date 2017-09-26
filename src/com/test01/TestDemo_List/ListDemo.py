# -*- coding: utf-8 -*-
"""这里是Python数组应用示例"""
import types
from array import *
class TestDemo():
    #list 链表数组
    arr=[]
    arr1=['a']
    arr2=[i for i in range(0,10,2)]#多维数组,注意， i for in xx 这个必须放在第一个位置，否则要先定义i，
    j=0
    k=0
    arr3=[j for j in range(1,9,3),k for k in range(2,7,1)]

    arr0=['a','b','c','d','e','f','g','h']#用于测试的数组
    arr00=[[1,2,3]]#用于测试的二元数组
    del arr0[2]
    print '删除数组的一个元素'
    print arr0
    print '遍历数组'
    for k,v in enumerate(arr0):
        print k,v
    print '增加元素'
    arr0.append('i')
    print arr0
    print '二维数组增加元素'
    arr00[0].append(4)
    print arr00[0]
    print '添加元素用+='
    arr0+='m'
    print arr0
    '''
Tuple 没有的方法：
    [1] 不能向 tuple 增加元素，没有 append 、 extend 、insert 等方法。
    [2] 不能从 tuple 删除元素，没有 remove 或 pop 方法。
    [3] 不能在 tuple 中查找元素，没有 index 方法（index是查找而不是索引，索引直接用下标即可，如：t[0]）。
    
使用 tuple 的好处：
    1 Tuple 比 list 操作速度快。如果您定义了一个值的常量集, 并且唯一要用它做的是不断地遍历它, 请使用 tuple 代替 list。
    2 如果对不需要修改的数据进行 “写保护”, 可以使代码更安全。使用 tuple 而不是 list 如同拥有一个隐含的 assert 语句, 
    说明这一数据是常量。如果必须要改变这些值, 则需要执行 tuple 到 list 的转换 (需要使用一个特殊的函数)。
    3 还记得我说过 dictionary keys 可以是字符串, 整数和 “其它几种类型”吗? Tuples 就是这些类型之一。
      Tuples 可以在 dictionary 中被用做 key, 但是 list 不行。实际上, 事情要比这更复杂。Dictionary key 
      必须是不可变的。Tuple 本身是不可改变的, 但是如果您有一个 list 的 tuple, 那就认为是可变的了， 
      用做 dictionary key 就是不安全的。只有字符串, 整数或其它对 dictionary 安全的 tuple 才可以用作 dictionary key。
    '''
    print 'Tuple 固定数组'
    t=('a','b','c')
    print t
    # Tuple 可以转换成list
    tlist = list( t )
    # list可以转换成Tuple
    arrtuple=tuple(arr0)

    #-----------------------------Dictionary(哈希数组) 词典数组----------------------------------------
    dict_arr={}
    dict_arr['name']='test'
    dict_arr['value']=[1,2,3]
    print '打印Dictionary的key'
    print dict_arr.keys()
    print '打印Dictionary的value'
    print dict_arr.values()
    print '遍历数组'
    for k in dict_arr:
        v = dict_arr.get(k)
        if type(v) is types.ListType:  # 如果数据是list类型，继续遍历
            print k, '---'
            for kk, vv in enumerate(v):
                print kk, vv
            print '---'
        else:
            print dict_arr.get(k)

    #-----------------------Array数组---------------------------------------------------------------------


    print '删除最后一个Array数组的元素'
    myarr = array("l")
    myarr.append(3)
    myarr.append(1)
    myarr.append(8)
    print myarr
    print '数组反序'
    myarr.reverse()
    print myarr

    myarr.pop()
    print '删除最后的一个值'
    print myarr
    myarr.remove(1)
    print '删除指定值'
    print myarr
    num1 = myarr[0]
    print '取数组的值。。。。。通过下标'
    print num1
    print '指定位置，。。。。插入值'
    myarr.insert(1,10)
    print myarr

