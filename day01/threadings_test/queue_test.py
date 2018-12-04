'''线程优先级队列Queue'''
import queue
import threading
import time

exitFlag = 0
workQueue = queue.Queue(10)
queueLock = threading.Lock()
threadList = ['thread-1', 'thread-2', 'thread-3']
nameList = ['One', 'Two', 'Three', 'Four', 'Five']
threads = []


def process_data(threadName, q):

    while not exitFlag:
        queueLock.acquire() # 获得锁
        if not workQueue.empty():
            data = q.get() # 取出队列的数据
            print('{0} is processing {1}.'.format(threadName, data))
            queueLock.release() # 释放锁
        else:
            queueLock.release()
        time.sleep(1)


class MyThread(threading.Thread):

    def __init__(self, threadId, name, q):
        threading.Thread.__init__(self)
        self.ThreadId = threadId
        self.name = name
        self.q = q

    def run(self):
        print('starting: ', self.name)
        process_data(self.name, self.q)
        print('Exiting: ', self.name)



def main():
    # 创建新线程
    threadID = 1
    for tName in threadList:

        # global threadID
        thread = MyThread(threadID, tName, workQueue)
        thread.start()
        threads.append(thread)
        threadID += 1

    # 填充队列
    queueLock.acquire()
    for word in nameList:
        workQueue.put(word)
    queueLock.release()

    # 等待队列清空 才发出终止线程信号
    while not workQueue.empty():
        pass
    global exitFlag
    exitFlag = 1

    #等待所有线程执行完毕
    for t in threads:
        t.join()

    print('Exiting Main Thread.')

if __name__ == '__main__':
    main()