'''协程不是计算机提供，操作系统只是提供了线程和进程。程序员人为创造。
协程运行程序的大致状态：在一个线程中运行多个任务，任务与任务之间来回切换，并在同一时间内只能运行一个任务。
协程（coroutine）也可以被称之为微线程，是一种用户态内的上下文切换技术。简而言之，其实就是通过一个线程实现代码块相互切换执行。
'''

# 1. 协程只有一个线程，一个线程之间来回切换，单线程并发——携程
from greenlet import greenlet

def fun_1():
    print(1)
    gr2.switch()
    print(2)
    gr2.switch()



def fun_2():
    print(3)
    gr1.switch()
    print(4)

# 我想让让异步，输出 1 3 2 4

gr1=greenlet(fun_1)
gr2=greenlet(fun_2)

gr1.switch()
#  底层原理是生成器，可以保存运行状态，


