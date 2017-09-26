# -*- coding: utf-8 -*-
import socket
# 建立连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = socket.gethostname()

port = 9999

s.connect((host, port))
#接收数据
tm = s.recv(1024)

s.close()

print("The time got from the server is %s" % tm.decode('ascii'))
