# -*- coding: utf-8 -*-
import socket
import time

# 创建一个UDP连接
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
    print (host)
    # 接收数据
    clientsocket,addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    #发送数据
    clientsocket.send(currentTime.encode('ascii'))
    #关闭客户端连接
    clientsocket.close()
