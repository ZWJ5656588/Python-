import asyncio

async def others():
    print("start")
    await asyncio.sleep(2)
    print("end...")
    return '这是一个协程函数的返回值'


async def func():
    print("执行协程函数的代码")
    response_1=await others()
    print(response_1)
    response_2=await others()
    print(response_2)


asyncio.run(func())
# 实质上是同步 await 如果后面跟的是一个普通协程对象，默认同步执行