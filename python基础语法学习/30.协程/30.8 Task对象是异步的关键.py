'''Tasks用于并发调度协程，通过asyncio.create_task(协程对象)的方式创建Task对象，这样可以让协程加入事件循环中等待被调度执行。

除了使用asyncio.create_task()函数外，还可以使用低层级的loop.create_task()或ensure_future()函数。但是不建议手动实例化Task对象

注意：asyncio.create_task()函数在 Python 3.7 中被加入。在 Python 3.7 之前可以改用低层级的asyncio.ensure_future()函数

'''

import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return '这是一个返回值'


async def main():
    print('开始任务...')
    # 创建task对象，将当前的func任务添加到事件循环中
    task_1 = func()   # asycnio.run()可以在底层将普通协程对象转换为task对象
    task_2 = asyncio.ensure_future(func())
    print('任务结束...')

    # 当执行某些协程遇到IO操作时，会自动切换执行其他任务
    # 此处的await是等待相对应的协程全部执行完毕并获取结果
    # 但是在等待的过程中，由于task缘故，会执行其他的协程
    result_1 = await task_1
    result_2 = await task_2
    print(result_1, result_2)


 # asycnio.run()可以在底层将普通协程对象转换为task对象
 # 这样一来程序还是并发执行
asyncio.run(main())