# -*- coding: utf-8 -*-
"""这里实现Python的多线程"""
import threading
from time import ctime,sleep

def music(func):
    for i in range(2):
        print ('I am listening music!  %s,%s' %(func,ctime()))
        sleep(1)

def movie(func):
    for i in range(2):
        print ('I am watching movie! %s,%s'%(func,ctime()))
        sleep(5)
threads=[]
t1 = threading.Thread(target=music,args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=movie,args=(u'阿凡达',))
threads.append(t2)

if __name__=="__main__":
    for t in threads:
        t.setDaemon(True)
        t.start()
    # 方法的位置是在for循环外的，也就是说必须等待for循环里的两个进程都结束后，才去执行主进程。
    t.join()
    print ("\n all over %s" % ctime())