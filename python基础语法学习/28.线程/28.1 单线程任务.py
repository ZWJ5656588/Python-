'''- 并发：指的是任务数多余cpu核数，通过操作系统的各种任务调度算法，实现用多个任务“一起”执行（实际上总有一些任务不在执行，因为切换任务的速度相当快，看上去一起执行而已）
- 并行：指的是任务数小于等于cpu核数，即任务真的是一起执行的。

线程负负责将代码转换为二进制码给机器执行，进程是哟个软件执行需要资源的一个分配单位

'''

import time

def print_hello():
    print('hello')
    #让程序休眠一秒
    time.sleep(1)   # 程序执行到此处代码阻塞一秒


for i in range(5):
    print_hello()

'''当前程序为一个单线程程序
            如果程序休眠阻塞，则必须解阻塞才可以继续运行'''

