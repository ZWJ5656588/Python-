import asyncio

async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return '这是一个协程函数的返回值'


async def main():
    print("开始任务...")
    # 将协程对象转为task对象并放入一个任务列表中
    # 也可以通过for循环把task添加到空列表中
    task_list=[
        asyncio.create_task(func()),
        asyncio.create_task(func()),
    ]
    # 如果要运行列表中的任务，需要将列表对象转为一个可以等待的对象 wait方法
    # wait方法返回一个元组，元组里面有两个元速.  1.函数返回值，2.当前任务的状态
    done,pending= await asyncio.wait(task_list)
    print(done)
    # 如果我想获取当前协程的返回值怎么办
    for item in done:
        # 当前拆包过后的done是一个集合
        print(item.result())


# 只有添加事件循环之后才可以创建task对象
loop=asyncio.get_event_loop()
loop.run_until_complete(main())


