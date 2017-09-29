# -*- coding: utf-8 -*-
"""对象与方法
面向对象及高级编程
1.__slots__
2.@property
"""
class Student():
    pass
s=Student()
s.name='LiLei'# 动态给实例绑定一个属性
print(s.name)

def set_age(self,age):# 定义一个函数作为实例方法
    self.age=age

from types import MethodType
s.set_age=MethodType(set_age,s)# 给实例绑定一个方法
s.set_age(15)
print(s.age)
"""
s2 = Student() # 创建新的实例
 s2.set_age(25) # 尝试调用方法
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'set_age'
"""
def set_score(self,score):
    self.score=score

Student.set_score = set_score# 给class绑定一个方法
s.set_score(99)
print(s.score)
s2=Student()
s2.set_score(100)
print(s2.score)
"""
s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
s.score = 99 # 绑定属性'score'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'score'
"""
print('__slots__实例：')
class Teacher():
    __slots__=('name','age')# 用tuple定义允许绑定的属性名称

te=Teacher()
te.name='hello'
te.age=12
print(te)
# te.size=12 没有在slots的属性会报错AttributeError，子类不继承父类的约束,子类新的约束继承父类的约束

"""
@porperty 实例
Python内置的@property装饰器就是负责把一个方法变成属性调用的
"""
print('@porperty实例')
class Leader():
    @property
    def name(self):#等价于get_name方法
        return self._name
    @name.setter
    def name(self,value):#等价于set_name 方法
        self._name=value
leader=Leader()
leader.name='litaibai'#这里调用了set_name方法
print(leader.name)#这里调用了get_name 方法