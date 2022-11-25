import time
from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor
from multiprocessing import Pool

def func(value):
    time.sleep(1)
    print(value)


# 1. 创建线程池运行函数
thread_pool=ThreadPoolExecutor(max_workers=5)
for i in range(10):
    fut=thread_pool.submit(func,i)
    print(fut)


print("-"*20)


# 2.进程池运行函数
process_pool=ProcessPoolExecutor


