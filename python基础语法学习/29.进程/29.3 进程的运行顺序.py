'''对于线程，线程的运行是有操作系统自动调度的，
Pythonc程序员无法决定运行顺序，只能上锁干扰'''

# 进程之间的执行顺序也是无序的！！！！
# 多个进程中的线程是相互独立的，多个线程一定是在同一个进程里面的
# 在同一个进程中的统一线程只能有一个在运行！！

# 计算机可以创建进程并且进程之间相互独立，子进程将父进程的代码copy并且创建了一个单独的空间进行代码运行
# 进程理论上可以进行并行，但这是理论上的，实际上操作系统还有其他的任务，四核处理器做不到并行

import time
import multiprocessing


def test_1():
    for i in range(10):
        print('子进程1：%d' % i)
        time.sleep(0.5)


def test_2():
    for i in range(10):
        print('子进程2：%d' % i)
        time.sleep(1)


def main():
    p1=multiprocessing.Process(target=test_1)
    p2=multiprocessing.Process(target=test_2)


    p1.start()
    p2.start()

    p1.join()  # 阻塞主进程
    p2.join()

    for i in range(10):
        print('主进程：%d' % i)
        time.sleep(0.5)


if __name__ == '__main__':
    main()


