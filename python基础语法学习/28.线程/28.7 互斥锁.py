'''# 2.1 系统调用t1，然后获取到g_num的值为0，此时上一把锁，即不允许其他线程操作g_num
# 2.2 t1对g_num的值进行+1
# 2.3 t1解锁，此时g_num的值为1，其他的线程就可以使用g_num了，而且是g_num的值不是0而是1
# 2.4 同理其他线程在对g_num进行修改时，都要先上锁，处理完后再解锁，在上锁的整个过程中不允许其他线程访问，就保证了数据的正确性'''
import time
import threading

# 创建线程互斥锁 设置为全局变量
mutex = threading.Lock()

# 创建一个全局变量
g_num = 0


def add_number_1(num):
    global g_num
    # 上锁
    mutex.acquire()
    for i in range(num):
        g_num += 1
    print(f'线程1计算得出的结果为{g_num}')
    # 解锁释放
    mutex.release()


def add_number_2(num):
    global g_num
    # 上锁
    mutex.acquire()
    for i in range(num):
        g_num += 1
    print(f'线程2计算得出的结果为{g_num}')
    # 解锁释放
    mutex.release()


if __name__ == '__main__':
    time1 = time.time()
    t1 = threading.Thread(target=add_number_1, args=(1000000,))
    t1.start()

    t2 = threading.Thread(target=add_number_2, args=(1000000,))
    t2.start()

    # 主线程等待，当主线程运行到没有代码时进行等待，直到子线程任务完成则程序结束，但实际上主线程已经运行完毕
    # g_num*=2
    # print(f'主线程最终的到的结果是：{g_num}')
    # 结果不对，锁了还是不对，因为主线程没有等待子线程返回最终结果就已经结束，但整个程序还在运行

    '''如果大家需要等待子线程执行完毕后获取最终结果
    那么需要完成在子线程启动时候让主线程等待
    如果主线程执行到子线程启动后下面还有代码的情况下
    下面的代码不会执行
    '''
    t1.join()  # 子线程一阻塞主线程
    t2.join()  # 子线程二阻塞主线程

    g_num*=2

    print(f'主线程最终的到的结果是：{g_num}')
    time2 = time.time()
    print(f'程序运行的时间为{time2 - time1}')

    '''锁的坏处：
- 阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了
- 由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁
'''

print('1'+'--------------------------------------')


# 2. 代码改进
'''上段代码可以将缩放在for循环里面，这样以来系统就可以并发执行两端for循环
    不需要第二个线程等待第一个线程运行100 0000次以后再执行，保留了并发工作的模式
    提高了工作效率
'''

# 创建线程互斥锁 设置为全局变量
mutex = threading.Lock()

# 创建一个全局变量
g_num = 0


def add_number_1(num):
    global g_num
    for i in range(num):
        # 上锁
        mutex.acquire()
        g_num +=1
        # 解锁释放
        mutex.release()
    # print(f'线程1计算得出的结果为{g_num}')


def add_number_2(num):
    global g_num
    for i in range(num):
        # 上锁
        mutex.acquire()
        g_num += 1
        # 解锁释放
        mutex.release()
    # print(f'线程2计算得出的结果为{g_num}')


if __name__ == '__main__':
    time1=time.time()
    t1 = threading.Thread(target=add_number_1, args=(1000000,))
    t1.start()

    t2 = threading.Thread(target=add_number_2, args=(1000000,))
    t2.start()

    # 主线程等待，当主线程运行到没有代码时进行等待，直到子线程任务完成则程序结束，但实际上主线程已经运行完毕
    # g_num*=2
    # print(f'主线程最终的到的结果是：{g_num}')
    # 结果不对，锁了还是不对，因为主线程没有等待子线程返回最终结果就已经结束，但整个程序还在运行

    '''如果大家需要等待子线程执行完毕后获取最终结果
    那么需要完成在子线程启动时候让主线程等待
    如果主线程执行到子线程启动后下面还有代码的情况下
    下面的代码不会执行
    '''
    t1.join()  # 子线程一阻塞主线程
    t2.join()  # 子线程二阻塞主线程

    g_num*=2

    print(f'主线程最终的到的结果是：{g_num}')
    time2=time.time()
    print(f'程序运行的时间为{time2-time1}')