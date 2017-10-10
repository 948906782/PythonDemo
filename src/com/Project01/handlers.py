# -*- coding:utf-8 -*-

import re,time,json,logging,hashlib,base64,asyncio
from src.com.Project01.coroweb import get,post
from src.com.Project01.Models import User

@get('/')
def index(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    users=yield from User.findAll()
    return {
        '__template__': 'blogs.html',
        'users': users
    }

@get('/api/users')
def api_get_users():
    users=yield from User.findAll(orderBy='create_at desc')
    for u in users:
        u.name='******'
        return dict(users=users)

