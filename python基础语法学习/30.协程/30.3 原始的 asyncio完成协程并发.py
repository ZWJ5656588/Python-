import asyncio

# 协程的效率远大于多线程

@asyncio.coroutine        # 即将遗弃的携程用法
def func_1():
    print(1)
    # 手动任务切换，并没有指定函数名称
    # 革命性的，遇到阻塞代码会自动切换到可以执行任务的代码块
    yield from asyncio.sleep(2)   # 堵塞两秒
    print(2)


@asyncio.coroutine
def func_2():
    print(3)
    yield from asyncio.sleep(2)
    print(4)


tasks=[
    asyncio.ensure_future(func_1()),  # 将协程函数对象交给future 将当前函数对象转换为task对象
    asyncio.ensure_future(func_2())   # 如果asyncio遇到了task对象，则将task对象作为并发执行，如果不转，则是同步执行
]                                     # 协程中，函数加()不是调用，是返回一个协程对象
# 创建了一个容器，事件循环
# 是协程的重要组成部分，将需要执行的任务由事件循环调度
# 事件循环只能执行三个对象-> task、asyncio、可等待对象
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))