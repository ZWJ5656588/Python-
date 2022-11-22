'''进程：一个程序运行起来后，代码+用到的资源 称之为进程，它是操作系统分配资源的基本单元。
不仅可以通过线程完成多任务，进程也是可以的
'''

'''进程也可以完成多任务
1.线程的多任务一般用于文件读写，网络IO，但是线程不太适合做计算
2.进程可以使计算效率变得更快'''

'''工作中，任务数往往大于cpu的核数，即一定有一些任务正在执行，而另外一些任务在等待cpu进行执行，因此导致了有了不同的状态。

- 就绪态：运行的条件都已经具备，正在等在cpu执行
- 执行态：cpu正在执行其功能
- 等待态：等待某些条件满足，例如一个程序sleep了，此时就处于等待态


'''

import time
import threading           # 创建多线程任务
import multiprocessing     # 创建多进程任务


# 1. 回顾多线程
# def test_1():
#     for i in range(10):
#         print('这是任务1: %s' % i)
#         time.sleep(1)
#
#
# def test_2():
#     for i in range(10):
#         print('这是任务2: %s' % i)
#         time.sleep(1)
#
#
# def main():
#     t1=threading.Thread(target=test_1)
#     t2=threading.Thread(target=test_2)
#
#     t1.start()
#     t2.start()
#
#
# if __name__ == '__main__':
#     main()


# 2. 多线程方法
def test_1():
    for i in range(10):
        print('这是任务1: %s' % i)
        time.sleep(1)


def test_2():
    for i in range(10):
        print('这是任务2: %s' % i)
        time.sleep(1)


def main():  #windows系统只支持spawn方式启动子线程，且必须要有主函数入口
    # 创建两个进程
    p1=multiprocessing.Process(target=test_1)
    p2=multiprocessing.Process(target=test_2)

    p1.start()
    p2.start()


if __name__ == '__main__':
    main()


