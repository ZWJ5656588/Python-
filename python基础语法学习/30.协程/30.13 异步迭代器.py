import asyncio

# 迭代器的主要作用是制定循环方式

# 自定义异步迭代器
class Reader:
    def __init__(self):
        self.count = 0

    async def readline(self):
        # await asyncio.sleep(1)
        self.count += 1
        if self.count == 100:
            return None
        return self.count

    def __aiter__(self):
        return self   # 返回一个aiterable对象 创建的实例就是

    async def __anext__(self):
        val = await self.readline()
        if val is None:
            raise StopAsyncIteration
        return val


async def func():
    # 在函数里获取类的实例对象
    obj = Reader()
    # 异步for循环必须在协程函数内执行，协程函数名称随意取名
    async for item in obj:
        print(item)


asyncio.run(func())