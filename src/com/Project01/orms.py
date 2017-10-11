# - coding:utf-8 -*-

import asyncio
import logging
import aiomysql

def log(sql,args=()):
    logging.info('SQL:%s'%sql)

async def create_pool(loop,**kw):
    logging.info('creating pool...')
    global __pool
    __pool=await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )

async def select(sql,args,size=None):
    log(sql,args)
    global __pool
    async with __pool.get() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql.replace('?','%s'),args or ())
            if size:
                rs=await cur.fetchmany(size)
            else:
                rs=await cur.fetchall()
        logging.info('rows return %s'%len(rs))
        return rs

async def execute(sql,args,autoCommit=True):
    log(sql)
    async with __pool.get() as conn:
        if not autoCommit:
            await conn.begin()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute(sql.replace('?','%s'),args or ())
                affected=cur.rowcount
            if not autoCommit:
                await conn.commit()
        except BaseException as e:
            if not autoCommit:
                await conn.rollback()
            raise
        return affected

def create_args_string(num):
    L=[]
    for n in range(num):
        L.append('?')
        return ', '.join(L)

class Field(object):

    def __init__(self,name,column_type,primary_key,default):
        self.name=name
        self.column_type=column_type
        self.primary_key=primary_key
        self.default=default

    def __str__(self):
        return '<%s,%s:%s>'%(self.__class__.__name__,self.column_type,self.name)

class StringField(Field):
    def __init__(self,name=None,primary_key=False,default=None,ddl='varchar(100)'):
        super().__init__(name,ddl,primary_key,default)

class BooleanField(Field):

    def __init__(self, name=None, default=False):
        super().__init__(name, 'boolean', False, default)

class IntegerField(Field):
    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, 'bigint', primary_key, default)

class FloatField(Field):

    def __init__(self, name=None, primary_key=False, default=0.0):
        super().__init__(name, 'real', primary_key, default)

class TextField(Field):

    def __init__(self, name=None, default=None):
        super().__init__(name, 'text', False, default)


class ModelMetaclass(type):

    def __new__(cls,name,bases,attrs):
        if name=='Model':
            return type.__new__(cls,name,bases,attrs)
        tableName=attrs.get('__table__',None) or name
        logging.info('found model: %s (table: %s)' % (name, tableName))
        mappings=dict()
        fields=[]
        primaryKey=None
        for k,v in attrs.items():
            if isinstance(v,Field):
                logging.info('  found mapping: %s ==> %s' % (k, v))
                mappings[k]=v
                if v.primary_key:
                    if primaryKey:
                        raise BaseException('Duplicate primary key for field: %s' % k)
                    primaryKey=k
                else:
                    fields.append(k)
        if not primaryKey:
            raise BaseException('Primary key not found.')
        for k in mappings.keys():
            attrs.pop(k)
        escaped_fields=list(map(lambda f:'`%s`'%f,fields))
        attrs['__mappings__']=mappings
        attrs['__table__']=tableName
        attrs['__primary_key__']=primaryKey
        attrs['__fields__']=fields
        attrs['__select__']='select `%s`, %s from `%s`' % (primaryKey, ', '.join(escaped_fields), tableName)
        attrs['__insert__']= 'insert into `%s` (%s, `%s`) values (%s)' % (tableName, ', '.join(escaped_fields), primaryKey, create_args_string(len(escaped_fields) + 1))
        attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (
        tableName, ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primaryKey)
        attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (tableName, primaryKey)
        return type.__new__(cls,name,bases,attrs)

class Model(dict,metaclass=ModelMetaclass):
    def __init__(self,**kw):
        super(Model,self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except BaseException:
            raise BaseException(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key]=value

    def getValue(self,key):
        return getattr(self,key,None)

    def getValueOrDefault(self,key):
        value=getattr(self,key,None)
        if value is None:
            field=self.__mapping__[key]
            if field.default is not None:
                value=field.default() if callable(field.default) else field.default
                logging.debug('using default value for %s: %s' % (key, str(value)))
                setattr(self,key,value)
        return value

    @classmethod
    @asyncio.coroutine
    def findAll(cls,where=None,args=None,**kw):
        sql=[cls.__select__]
        if where:
            sql.append('where')
            sql.append(where)
        if args is None:
            args=[]
        order_by=kw.get('orderBy',None)
        if order_by:
            sql.append('order by')
            sql.append(order_by)
        limited=kw.get('__limit__',None)
        if limited is not None:
            sql.append('limit')
            if isinstance(limited,int):
                sql.append('?')
                sql.append(limited)
            elif isinstance(limited,tuple) and len(limited)==2:
                sql.append('?,?')
                args.extend(limited)
            else:
                raise BaseException('Invalid limit value: %s' % str(limited))
        rs=yield from select(' '.join(sql), args)
        return [cls(**r) for r in rs]

    @classmethod
    async def findNumber(cls,selectField,where=None,args=None):
        sql=['select %s _num_ from `%s`' % (selectField, cls.__table__)]
        if where:
            sql.append('where')
            sql.append(where)
        rs=await select(' '.join(sql),args,1)
        if len(rs)==0:
            return None
        return rs[0]['_num_']

    @classmethod
    @asyncio.coroutine
    def find(cls,pk):
        rs=yield from select('%s where `%s`=?'%(cls.__select__,cls.__primary_key__),[pk],1)
        if len(rs)==0:
            return None
        return cls(**rs[0])

    async def save(self):
        args=list(map(self.getValueOrDefault,self.__fields__))
        args.append(self.getValueOrDefault(self.__primary_key__))
        rows=await execute(self.__insert__,args)
        if rows!=1:
            logging.warning('failed to insert record: affected rows: %s' % rows)

    async def update(self):
        args=list(map(self.getValue,self.__fields__))
        args.append(self.getValue(self.__primary_key__))
        rows=await execute(self.__update__,args)
        if rows!=1:
            logging.warnning('failed to update by primary key: affected rows: %s' % rows)

    async def move(self):
        args=[self.getValue(self.__primary_key__)]
        rows=await execute(self.__delete__,args)
        if rows!=1:
            logging.warnning('failed to remove by primary key: affected rows: %s' % rows)


