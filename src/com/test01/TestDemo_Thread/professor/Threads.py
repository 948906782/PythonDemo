# -*- coding: utf-8 -*-
"""这是一个多线程的进阶实例-锁机制
当多线程争夺锁时，允许第一个获得锁的线程进入临街区，并执行代码。
所有之后到达的线程将被阻塞，直到第一个线程执行结束，退出临街区，并释放锁。
需要注意，那些阻塞的线程是没有顺序的。
"""

import threading
from random import randint
from time import ctime,sleep

L=threading.Lock()

def hi(n):
    L.acquire()
    for i in [1,2]:
        print ('第',i,'次打印')
        sleep(n)
        print ('ZZZZZ睡了',n,'秒')
    L.release()

def main():
    print ('START!')
    threads=[]
    for i in range(10):
        rands = randint(1, 2)
        t = threading.Thread(target=hi, args=(rands,))
        threads.append(t)

    for i in range(10):
        threads[i].start()

    for i in range(10):
        threads[i].join()

    print ('DONE!')

if __name__=="__main__":
    main()