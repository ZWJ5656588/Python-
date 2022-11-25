# 当创建进程池之后会创建你设置的进程个数，进程池中的进程(10)是可以重复利用的
'''
一百万个任务，
    创建一个进程池，限定创建10个进程

    把一百万个任务放在进程池中，前十个任务被执行，剩下的任务对象进行等待 直到十个进程中的某一个任务执行完毕再调用！
'''

import time
import random  # 产生随机数
from multiprocessing import Pool   #导入进程池子
import os


def worker(msg):
    # 创建一个对象用来进行任务启动的计时
    t_start=time.time()  #创建一个时间戳
    print(f'{msg}开始执行，进程号为{os.getpid()}')
    time.sleep(random.random()*3)  # 生成了0到3之间的浮点数
    t_stop=time.time()
    print('%d 任务执行完毕，耗时%.3f' % (msg,(t_stop-t_start)))


def main():
    # 创建进程池对象
    po=Pool(3)   # 只能创建三个进程,一开始可以进来三个进程，进来一个运行一个，有一个运行完了，下一个再进来
    for i in range(10):  # 创建10个任务,任务数大于进程数，则多出来的任务等待执行
        # 异步执行进城任务，非堵塞方式
        po.apply_async(worker,args=(i,))
        # 同步执行进程任务,相当于单进程，主进程此时堵塞
        # po.apply(worker,args=(i,))
        # 会出现相同的进程号，说明进程号在重复利用，证明进程池中的进程不会被关闭，会反复利用

    print('进程池启动...')
    po.close()  # 关闭进程池，当进程池一旦创建并且调用close()之后，不能动态的去创建进程数量
    po.join()   # 等待进程池中进程任务全部执行完毕后再释放，join方法必须在close之后
    # 如果没有join阻塞主进程，那么主进程一旦结束，对应的进程池也会关闭

    print('任务结束...')


if __name__ == '__main__':
    main()

'''如果第二个函数需要依赖第一个进程返回的形参'''