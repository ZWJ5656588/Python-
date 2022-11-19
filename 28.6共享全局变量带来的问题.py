import threading
import  time

g_num=0

'''创建两个任务
    一个任务负全局变量加法
    一个任务获取全局变量的值
'''

#1.
def work_1(num):
    global g_num        # 共享全局变量
    for i in range(num):  # 数值小，不会产生资源竞争，暂时不会出问题
        g_num+=1
    print(f'子线程1中计算得出的结果为:{g_num}')


def work_2(num):
    global g_num
    for i in range (num):
        g_num+=1
    print(f'子线程2获取到的全局变量的值为:{g_num}')


if __name__ == '__main__':
    print(f'子线程未启动之前主线程获取的值为：{g_num}')
    t1=threading.Thread(target=work_1,args=(100000,))   # 线程里的参数通过args元组进行传递
    t1.start()
    t2=threading.Thread(target=work_1,args=(200000,))   # 线程里的参数通过args元组进行传递
    t2.start()
    print(f'子线程启动之后主线程获取的值为：{g_num}')

    # 会产生资源竞争 在没有把得出来的结果赋值给全局变量的时候，就已经进行了任务切换，导致线程一的结果与线程二结果覆盖，导致程序出错


# 2. 避免资源竞争

# 线程同步 A线程执行完，B线程才给执行 协同配合

# 互斥锁，线程切换由操作系统决定，随机

# 2.1 系统调用t1，然后获取到g_num的值为0，此时上一把锁，即不允许其他线程操作g_num
# 2.2 t1对g_num的值进行+1
# 2.3 t1解锁，此时g_num的值为1，其他的线程就可以使用g_num了，而且是g_num的值不是0而是1
# 2.4 同理其他线程在对g_num进行修改时，都要先上锁，处理完后再解锁，在上锁的整个过程中不允许其他线程访问，就保证了数据的正确性