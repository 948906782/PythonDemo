#-*- coding:utf-8 -*-
"""
这里实现模拟ORM框架
ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，
这样，写代码更简单，不用直接操作SQL语句。

要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。
"""




# 定义Field类，它负责保存数据库表的字段名和字段类型
class Field(object):
    def __init__(self,name,column_type):
        self.name=name
        self.column_type=column_type
    def __str__(self):
        return '<%s:%s>'%(self.__class__.__name__,self.name)
# 扩展的String类型
class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar(100)')
# 扩展的Integer类型
class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField,self).__init__(name,'bigint')

# ModelMetaclass 元类
class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if name=='Model':
            return type.__new__(cls,name,bases,attrs)
        print('Found model: %s' %(name))
        mappings=dict()
        for k,v in attrs.items():
            if isinstance(v,Field):
                print('Found mappings %s==%s>'%(k,v))
                mappings[k]=v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__']=mappings
        attrs['__table__']=name
        return type.__new__(cls,name,bases,attrs)
# Model类,原型方法
class Model(dict,metaclass=ModelMetaclass):
    def __init__(self,**kwargs):
        super(Model,self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"Model" "object has no attr %s"%key)

    def __setattr__(self, key, value):
        self[key]=value
    # 保存方法
    def save(self):
        fields=[]
        params=[]
        args=[]
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
        sql='insert into %s (%s) values (%s)'%(self.__table__,','.join(fields),','.join(params))
        print('SQL:%s'%sql)
        print('args:%s'%str(args))

class User(Model):
    id=IntegerField('id')
    name=StringField('name')


u=User(id=123,name='yes')
u.save()
