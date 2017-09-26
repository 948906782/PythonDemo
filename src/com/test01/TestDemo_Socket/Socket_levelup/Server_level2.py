# -*- coding: utf-8 -*-
#这里是一个socket的更深层次的实现实例-服务端

import socket
import time
class ServerDemo():
    def __int__(self):
        print 'Server initing...'
    server=None

    def getconn(self,HOST,PORT):
        self.server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.bind((HOST,PORT))
        self.__Logical()

    def __Logical(self):
        self.server.listen(5)
        while True:
            client,addr=self.server.accept()
            print ('Get a connection from %s' %str(addr))
            currentTime = time.ctime(time.time()) + "\r\n"
            client.send(currentTime.encode('ascii'))
            msg=client.recv(1024)
            print('Getmessage:%s' %str(msg).encode('ascii'))
            client.close()

if __name__=="__main__":
    Server=ServerDemo()
    Server.getconn('localhost',8888)
