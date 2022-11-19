'''
1.python中需要使用一个模块来完成多线程任务
    threading 标准库
'''

import time
import threading


def print_hello():
    print('hello')
    time.sleep(1)


# 使用多线程进行任务加速
for i in range(5):
    # 1. 创建一个线程对象，这个线程对象类似于实例对象，在模块中的类中创建
    # 创建了五个线程对象，本质上是线程之间的切换
    # 当运行到print('hello')结束时，很快进入到挂起状态，切换到第二个线程，暂时不执行time.sleep(1)
    t=threading.Thread(target=print_hello)   # 传入函数的引用，target是实例对象的参数，用来绑定任务，在这里是绑定函数地址
    # 2. 使用线程对象启动一个线程
    t.start()        #调用一个方法
