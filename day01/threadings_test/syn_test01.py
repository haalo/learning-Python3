'''
线程同步
一个列表里的元素全是0，线程set从后向前把元素改成1，print线程从前往后打印元素
Thread对象的Lock和Rlock可以实现简单的线程同步，这两个对象都有acquire方法和release方法
此时该列表为共享数据，当set线程访问列表时，必须获得锁，如果print线程获得锁，则set线程等待（同步阻塞）
等到print线程访问完毕，print线程将释放锁，此时set线程继续执行
'''

import threading
import time
from day01.threadings_test.threading_01 import print_time

threadLock = threading.Lock()
threads = []

class MyThread(threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter


    def run(self):
        print('starting ', self.name)
        # 获得锁，获得锁成功返回True
        # 可选的timeout参数， 为空将一直阻塞除非获得锁
        # 否则超时返回False
        threadLock.acquire()
        print_time(self.name, self.counter, 5)
        # 释放锁
        threadLock.release()


def main():
    # 创建线程
    thread1 = MyThread(1, 'thread-1', 1)
    thread2 = MyThread(2, 'thread-1', 2)

    thread1.start()
    thread2.start()

    # 添加线程到列表
    threads.append(thread1)
    threads.append(thread2)

    # 等待所有线程执行完毕
    for t in threads:
        t.join()

    print('Exiting Main Thread!')


if __name__ == '__main__':
    main()
