'使用threading 模块创建线程，直接从threading.Thread继承'

import threading
import time


exitFlag = 0


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threading.Thread.exit()
        time.sleep(delay)
        print('{0}: {1}'.format(threadName, time.ctime(time.time())))
        counter -= 1


class MyThread(threading.Thread):
    '''
    继承threaing.Thread类,重写__init__()和run()方法
    '''

    def __init__(self, threadID, name, counter):
        '''
        重写__init__()
        :param threadID:
        :param name: 线程名字
        :param counter:
        '''
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        '''
        将要执行的代码写入run()函数里，线程在创建后会直接运行run()函数
        :return:
        '''
        print('starting ', self.name)
        print_time(self.name, self.counter, 5)
        print('Exiting ', self.name)



def main():
    # 创建线程
    thread1 = MyThread(1, 'Thread-1', 1)
    thread2 = MyThread(2, 'Thread-2', 2)

    # 启动线程
    thread1.start()
    thread2.start()

    print('Exiting Main Thread')

if __name__ == '__main__':
    main()