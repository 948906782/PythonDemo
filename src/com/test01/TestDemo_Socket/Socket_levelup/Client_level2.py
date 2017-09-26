# -*- coding: utf-8 -*-
#这里是一个socket的更深层次的实现实例-客户端

import socket
class ClientDemo():
    def __int__(self):
        print 'Client Startint...'
    client=None
    def getconn(self,HOST,PORT):
        self.client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect((HOST,PORT))
        self.__getresponse()

    def __getresponse(self):
        sendmsg='A message'
        # 接收信息
        meg=self.client.recv(1024)
        # 发送信息
        self.client.send(sendmsg.encode('ascii'))
        self.client.close()
        print('now : %s' %str(meg).encode('ascii'))

if __name__=="__main__":
    Client=ClientDemo()
    Client.getconn('localhost',8888)