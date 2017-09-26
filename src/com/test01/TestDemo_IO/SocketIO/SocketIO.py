# -*- coding: utf-8 -*-

#IO多路复用 利用select监听终端操作实例
import socket
import select

sk1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk1.bind(('localhost',8088))
sk1.listen(1)
inpu = [sk1,]

while True:
    r_list,w_list,e_list = select.select(inpu,[],[],1)
    for sk in r_list:
        if sk == sk1:
            conn,address = sk.accept()
            inpu.append(conn)
        else:
            try:
                ret = str(sk.recv(1024),encoding="ascii")
                sk.sendall(bytes(ret+"hao",encoding="ascii"))
            except Exception as ex:
                inpu.remove(sk)