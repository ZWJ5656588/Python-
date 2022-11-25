import asyncio
from asyncio import  *

# 创建协程函数

async def func_1():  # 定义协程函数，返回协程对象，
    print(1)
    # await  相当于之前看到的 yield from
    await sleep(2)     # sleep()是内置的协程对象。。暂停线程运行等待两秒钟 并获取方法的返回值之后解堵塞
    # 这里的sleep模拟耗时操作，返回值是None，拿到之后解堵塞
    # await之后可以是文件操作，网络io等具体任务
    print(2)


async def func_2():
    print(3)
    # await:等待某些io任务，await+可等待的对象(协程对象，Future对象,Task对象)
    # await 可以把后面语句的返回值拿出来
    await asyncio.sleep(2)
    # 此时若线程里有其他的协程任务，则自动切换,如果后面是普通协程对象，则要等到当前协程运行结束再切换
    # 如果await后面是task对象，则会立即切换到其余协程
    print(4)


'''
1. 如果一个函数呗async声明，则当前的函数是一个协程函数对象
2. 协程函数对象不能被直接调用 比如func_1()会警告，不能直接被调用
3. 如果想要运行协程函数，我们需要借助事件循环、task对象运行当前协程函数！！！
4. await是协程中的一个关键字，作用是等待一些耗时任务并拿到这些任务的返回值之后才会解堵塞
5. 运行上面两个协程函数
6.事件循环只能执行可以被等待的对象：协程对象，task对象，asyncio对象，task对象
'''

# 将协程对象转为task对象，用来并发执行
tasks=[
    asyncio.ensure_future(func_1()),
    asyncio.ensure_future(func_2())
    ]
'''也可以使用变量接收创建的协程对象，再把变量送到asyncio.ensure_future()中转换为并发对象task，异步执行的关键'''
'''若直接将携程对象func_1()放到事件循环中运行，则是同步执行'''

# 创建完task对象之后用事件循环去调用task对象
loop=asyncio.get_event_loop()  # 返回一个事件循环对象，并用loop变量接收
# 将任务放到事件循环[任务列表]中检测任务状态是否执行
loop.run_until_complete(asyncio.wait(tasks)) # wait() 把task对象转换为aysncio对象

# 高版本的解释器可以使用asyncio中的run方法自动创建事件循环
# asyncio.run(func_1())

'''什么是事件循环?'''

'''简单来说是个死循环，将任务列表扔到里面
    1.循环整个任务列表
    2.将任务分为可执行和执行完毕两种
    3.将完成的任务从列表中剔除
    4.当列表为空，中断循环break'''

