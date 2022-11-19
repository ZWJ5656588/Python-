# 1. 创建一个全局变量
import threading

g_num=100

'''创建两个任务
    一个任务负全局变量加法
    一个任务获取全局变量的值
'''

def work_1():
    global g_num        # 共享全局变量
    for i in range(3):  # 数值小，不会产生资源竞争，暂时不会出问题
        g_num+=1
    print(f'子线程1中计算得出的结果为:{g_num}')


def work_2():
    global g_num
    g_num+=2
    print(f'子线程2获取到的全局变量的值为:{g_num}')


# 函数入口，主线程
if __name__ == '__main__':
    print(f'子线程未启动之前主线程获取的值为：{g_num}')

    # 创建线程对象，刚创建的时候线程不存在，因为没有运行，运行以后线程才存在
    t1=threading.Thread(target=work_1)

    #启动线程1
    t1.start()    # 子线程创建后，主线程并不会阻塞，会继续运行完毕，等到主线程完毕后等待子线程运行完毕

    t2=threading.Thread(target=work_2)

    t2.start()

    print(f'主线程等待子线程执行完毕后获取的值为{g_num}')

    # 这三个线程并不是同时执行，是来回切换的并发执行