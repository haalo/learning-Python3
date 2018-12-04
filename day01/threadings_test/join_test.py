'''
默认情况(setDaemon(False))，主线程执行完毕后退出，此时子线程会继续执行自己的任务知道任务结束
setDaemon(Ture) 设置子线程为守护线程, 一旦主线程执行完毕，则全部线程被终止执行
join([timeout])
当设置子线程为守护线程时，主线程对于子线程等待timeout的时间后会终止子线程，最后退出程序，
就是给子线程一个timeout时间，让他去执行，时间一到就终止。
没有设置守护线程时，主线程将会等待timeout的累加和这样一段时间，时间一到主线程结束，子线程则可以
一直执行到任务完成
'''

import threading
import time


def run():
    time.sleep(1)
    print('当前线程的名称是: ', threading.current_thread().name)
    time.sleep(2)


if __name__ == '__main__':
    start_time = time.time()
    print('这是主线程!', threading.current_thread().name)
    threadlist = []
    for i in range(5):
        t = threading.Thread(target=run())
        threadlist.append(t)

    for t in threadlist:
        t.setDaemon(True)
        t.start()

    for t in threadlist:
        t.join()

    print("Exiting Main Thread ",threading.current_thread().name)
    print('一共执行了:{0} '.format(time.time() - start_time))
