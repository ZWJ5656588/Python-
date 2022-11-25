'''  1. 通过multiprocessing导入Manager类
from multiprocessing import Manager
    2.实例化Manager
manager=Manager()
    3. 调用Lock函数
lock=manager.Lock()
'''

# 理解起来与线程锁类似，锁中运行模式相当于单进程

import os
import time
import multiprocessing
import random

def work(count,lock):
    lock.acquire()      # 上锁
    print(f'{work.__name__}第{count}次执行，进程号为{os.getpid()}')  #函数名.__name__可以获得当前运行中的函数名
    time.sleep(0.4)
    lock.release()      # 解锁
    return  f'{work.__name__}函数返回值为{count},进程id为{os.getpid()}'


if __name__ == '__main__':
    pool=multiprocessing.Pool(5)
    manager=multiprocessing.Manager()
    lock=manager.Lock()      # 通过进程管理器创建锁
    results=[]
    for i in range (21):
        result=pool.apply_async(func=work,args=(i,lock))
        # 异步进程apply_async中函数传递的关键字参数是func=
        results.append(result)


    print("进程启动")
    pool.close()
    pool.join()
    print("任务结束")
