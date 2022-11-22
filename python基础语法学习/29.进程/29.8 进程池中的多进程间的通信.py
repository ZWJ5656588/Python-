'''进程池中的 Queue

如果要使用Pool创建进程，就需要使用multiprocessing.Manager()中的Queue()，而不是multiprocessing.Queue()，否则会得到一条如下的错误信息：

RuntimeError: Queue objects should only be shared between processes through inheritance.

下面的实例演示了进程池中的进程如何通信：
'''
# 进程池多进程通信 调用import中的Queue为Manager
from multiprocessing import Manager, Pool
import os, time


def reader(q):
    print('reader启动(%s),父进程为(%s)' % (os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print('reader从Quene获取到消息: %s' % q.get())


def writer(q):
    print('writer启动(%s)，父进程为(%s)' % (os.getpid(), os.getppid()))
    for i in 'tuling':
        q.put(i)


if __name__ == '__main__':
    print(f"{os.getpid()}start")
    q=Manager().Queue()
    po=Pool()
    po.apply_async(writer,(q,))
    # 等待队列写入
    time.sleep(0.1)
    po.apply_async(reader,(q,))
    po.close()
    po.join()
    print(f"{os.getpid()}end")