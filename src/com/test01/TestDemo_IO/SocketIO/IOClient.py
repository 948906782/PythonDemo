# -*- coding: utf-8 -*-

import socket

client=socket.socket()
client.connect(('127.0.0.1',8088))
while True:
    rs=client.recv(1024)
    print(str(rs).encode('ascii'))
    client.close()
