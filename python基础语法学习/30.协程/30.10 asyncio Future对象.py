'''Task 继承 Future, Task对象内部中的await结果的处理基于Future对象来的

在Future对象中会保存当前执行的这个协程任务的状态，如果当前任务状态为finished, 则await不再等待。

'''

import asyncio

# 1. 演示

# async def main():
#     # 获取当前正在运行的事件循环
#     loop=asyncio.get_running_loop()   # 获取系统层面上的事件循环 看官方文档
#     # 创建任务，future对象 当前对象没有绑定任务
#     fut=loop.create_future()
#     # 等待任务结果，因为当前future没有绑定任何任务，所以没有返回值，await一直堵塞
#     await fut
#

# 2.案例

async def set_after(fut):
    await asyncio.sleep(2)
    # Future对象调用set_result拿到返回值
    fut.set_result("这是自己设置的结果")


async def main():
    # 获取系统层面的事件循环
    loop=asyncio.get_running_loop()

    # 创建一个Future对象
    fut=loop.create_future()

    # 手动设置future任务的最终结果
    # 把Future对象当做参数对象传给协程对象
    # task->set->future
    await loop.create_task(set_after(fut))  # 对Future绑定任务

    #获取future对象的返回值
    data=await fut
    print(data)


asyncio.run(main())