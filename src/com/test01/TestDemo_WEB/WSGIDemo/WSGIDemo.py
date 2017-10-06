# -*- coding:utf-8 -*-
# WSGI使用实例-------------------------
# 定义一个处理方法
# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     return [b'<h1>Hello, web!</h1>']
# 创建一个服务端
# from wsgiref.simple_server import make_server
# 加载方法
# httpd=make_server('',8000,application)
# print('beginning...')
# httpd.serve_forever()
# 使用Web框架----------------------------
# 使用Flask框架
from flask import Flask
from flask import request
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>HOME</h1>'

@app.route('/signin',methods=['GET'])
def signin_form():
    return """<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>"""
@app.route('/signin',methods=['POST'])
def signin():# 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='aw':
        return '<h1>hello admin</h1>'
    else:
        return '<h1>ERROR</h1>'
if __name__=='__main__':
    app.run()

