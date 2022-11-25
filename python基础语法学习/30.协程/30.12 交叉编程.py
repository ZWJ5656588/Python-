'''一般情况下，代码编写需要统一编程风格，简而言之，就是如果使用的是线程/进程，则整个程序都统一使用线程/进程。

只有一种情况可能会进行交叉编程。一个项目中的所有IO请求为协程异步请求，假设MySQL数据库版本过低导致无法使用协程进行并发存储，这种情况会使用线程/进程完成并发存储任务。
'''

import time
import asyncio
import concurrent.futures


def func_1():
    time.sleep(2)
    return '测试'


async def main():
    loop = asyncio.get_running_loop()

    # 在协程函数中运行普通函数 在执行函数时，协程内部会自动创建一个线程池来运行任务
    # run_in_executor()方法第一个参数为None时则默认创建一个线程池
    fut = loop.run_in_executor(None, func_1)
    # await 可以运行由时间循环创立的线程池
    result = await fut
    print('当前方式会自动创建一个线程池去执行普通函数: ', result)


if __name__ == '__main__':
    asyncio.run(main())



'''1.在协程函数中可以运行一个线程池，但是这个线程池必须由事件循环处理
    run_in_excutor:如果不是一个协程对象则通过该方法调用
    run_in_excutor默认会创建一个线程池
    如果自己动手创建也必须用run_in_excutor
    '''