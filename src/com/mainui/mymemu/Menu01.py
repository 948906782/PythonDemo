# -*- coding:utf-8 -*-
"""
这个模块讨论WEB的继承
现有的aiohttp
一般的格式为：
1.@asyncio.coroutine装饰的函数
2.传入的参数需要自己从request中获取
3.自己构造一个Response对象
"""

import functools
# 用装饰器实现@GET(path)标签
def get(path):
    def decorator(func):
        @functools.wraps(func)
        def warpper(*args,**kw):
            return func(*args,**kw)
        warpper.__method__='GET'
        warpper.__route__=path
        return warpper
    return decorator
# 同理
def post(path):
    def decorator(func):
        @functools.wraps(func)
        def warpper(*args,**kw):
            return func(*args,**kw)
        warpper.__method__='POST'
        warpper.__route__=path
        return warpper
    return decorator

import inspect

"""
处理没有默认值的参数
 
"""

def get_require_kw_args(fn):
    args=[]
    params=inspect.signature(fn).parameters
    for name,param in params.items():
        if param.kind==inspect.Parameter.KEYWORD_ONLY and param.default==inspect.Parameter.empty:
            args.append(name)
        return tuple(args)
"""
处理有默认值的参数，要用param=来赋值
"""
def get_name_kw_args(fn):
    args=[]
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            args.append(name)
    return tuple(args)
"""
判断参数是否必须，用param=来赋值
"""
def has_named_kw_args(fn):
    params=inspect.signature(fn).parameters
    for name,param in params.items():
        if param.kind==inspect.Parameter.VAR_KEYWORD:
            return True
"""
"""
def has_var_kw_arg(fn):
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.VAR_KEYWORD:
            return True
"""
"""
def has_request_arg(fn):
    sig=inspect.signature(fn)
    params=sig.parameters
    found=False
    for name,param in params.items():
        if name=='request':
            found=True
            continue
        if found and(param.kind !=inspect.Parameter.VAR_POSITIONAL and param.kind!=inspect.Parameter.KEYWORD_ONLY and param.kind!=inspect.Parameter.VAR_KEYWORD):
            raise ValueError('request parameter must be the last named parameter in function: %s%s' % (fn.__name__, str(sig)))
        return found

from aiohttp import web
import os
from urllib import parse

class RequestHandler(object):
    def __init__(self,app,fn):
        self._app=app
        self._func=fn
        self._has_request_arg=has_request_arg(fn)
        self._has_var_kw_arg=has_var_kw_arg(fn)
        self._has_named_kw_args = has_named_kw_args(fn)
        self._named_kw_args = get_name_kw_args(fn)
        self._required_kw_args = get_require_kw_args(fn)

    async def __call__(self, request):
        kw=None
        if self._has_var_kw_arg or self._has_named_kw_args or self._required_kw_args:
            if request.method=='POST':
                if not request.content_type:
                    return web.HTTPBadRequest('Miss content_type!')
                ct=request.content_type.lower()
                if ct.startswith('application/json'):
                    params=await request.json()
                    if not isinstance(params,dict):
                        return web.HTTPBadRequest('JSON Error!')
                    kw=params
                elif ct.startswith('application/x-www-form-urlencoded') or ct.startswith('multipart/form-data'):
                    params=await request.post()
                    kw=dict(**params)
                else:
                    return web.HTTPBadRequest('Unsupported Content-Type: %s' % request.content_type)
            if request.method=='GET':
                qs=request.query_string
                if qs:
                    kw=dict()
                    for k,v in parse.parse_qs(qs,True).items():
                        kw[k]=v[0]
        if kw is None:
            kw=dict(**request.match_info)
        else:
            if not self._has_var_kw_arg and self._has_named_kw_args:
                copy=dict()
                for name in self._has_named_kw_args:
                    if name in kw:
                        copy[name]=kw[name]
                kw=copy

            for k,v in request.match_info.items():
                if k in kw:
                    print('Duplicate arg name in named arg and kw args: %s' % k)
                kw[k]=v
        if self._has_request_arg:
            kw['request']=request
        if self._required_kw_args:
            for name in self._required_kw_args:
                if not name in kw:
                    return web.HTTPBadRequest('Missing argument: %s' % name)
        try:
            r=await self._func(**kw)
            return r
        except ValueError as e:
            return dict(error=e.error,data=e.data,message=e.message)
import asyncio,logging
def add_static(app):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    app.router.add_static('/static/', path)
    logging.info('add static %s => %s' % ('/static/', path))

def add_route(app, fn):
    method = getattr(fn, '__method__', None)
    path = getattr(fn, '__route__', None)
    if path is None or method is None:
        raise ValueError('@get or @post not defined in %s.' % str(fn))
    if not asyncio.iscoroutinefunction(fn) and not inspect.isgeneratorfunction(fn):
        fn = asyncio.coroutine(fn)
    logging.info('add route %s %s => %s(%s)' % (method, path, fn.__name__, ', '.join(inspect.signature(fn).parameters.keys())))
    app.router.add_route(method, path, RequestHandler(app, fn))

def add_routes(app, module_name):
    n = module_name.rfind('.')
    if n == (-1):
        mod = __import__(module_name, globals(), locals())
    else:
        name = module_name[n+1:]
        mod = getattr(__import__(module_name[:n], globals(), locals(), [name]), name)
    for attr in dir(mod):
        if attr.startswith('_'):
            continue
        fn = getattr(mod, attr)
        if callable(fn):
            method = getattr(fn, '__method__', None)
            path = getattr(fn, '__route__', None)
            if method and path:
                add_route(app, fn)




