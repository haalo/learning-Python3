'''
Python 中使用线程有两种方式:
1, 函数式
2, 用类包装线程对象
'''

# 函数式: 调用_thread模块中的start_new_thread()函数来产生新线程
# import _thread
# _thread.start_nsew_thread(function, args, [, kwargs])  语法
# function 线程函数
# args 传递给线程的参数，是个元组(tuple)类型
# kwargs 可选参数
# 实例
import time
import _thread
def print_time(threadName, delay):
    '''
    打印当前时间
    :param threadName: 线程命名
    :param delay:  延时时间 秒
    :return:
    '''
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("{0}: {1}".format(threadName, time.ctime(time.time())))


def main():
    # 创建两个线程
    try:
        _thread.start_new_thread(print_time, ('thread-1', 2))
        _thread.start_new_thread(print_time, ('thread-2', 4))
    except:
        print('Error')

    while 1:
        pass

if __name__ == '__main__':
    main()