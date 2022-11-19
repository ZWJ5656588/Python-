"""
    time模块
        与时间相关的功能
    在python中 时间分为3种
        1.时间戳  timestamp  从1970 年 1 月 1日 到现在的秒数  主要用于计算两个时间的差
        2.localtime  本地时间  表示的是计算机当前所在的位置
        3.UTC 世界协调时间 又称世界统一时间、世界标准时间、国际协调时间。
          时间戳 结构化 格式化字符
"""
# 1. time 模块

import  time
# 获取时间戳 返回的是浮点型
# 作用 用来计算时间差,相对起始时间过了多少秒
print(time.time())
# 获取当地时间   返回的是结构化时间
print(time.localtime())
# 获取UTC时间 返回的还是结构化时间  比中国时间少8小时
print(time.gmtime())
# 结构化时间转换成字符串时间，必须写成如下格式，年月日时分秒
print(time.strftime('%Y-%m-%d %H:%M:%S'))
# 将格式化字符串的时间转为结构化时间  注意 格式必须匹配
print(time.strptime('2022-05-10 20:51:07','%Y-%m-%d %H:%M:%S'))
# 时间戳 转结构化
# 10秒时间戳
print(time.localtime(10))
print(time.gmtime(10))
# 当前时间戳
print(time.localtime(time.time()))

# 结构化转 时间戳
print(time.mktime(time.localtime()))

# sleep
# 让当前进程睡眠一段时间 单位是秒
time.sleep(0.5)
print('over')

print('1.'+'-'*20)


# 2. datetime 模块
'''2.1. 1什么是包??? 包和模块的不同
    包就是一个包含有__init__.py文件的文件夹
    包本质就是一种模块,即包是用包导入使用的,包内部包含的文件也都是用来被导入使用
     2.1.2 为何要用包
    那文件夹就是用来组织文件的，包就是组织模块的'''

'''2.2 导入包实现的功能
1. 以包下的__init__.py文件为基准来产生一个名称空间
2. 执行包下的__init__.py文件的代码,将执行过程中产生的名字都丢到名称空间中
3. 在当前执行文件中拿到一个名字p1,该p1就是指向__init__.py名称空间的'''

''' 2. 3 导入包的注意事项
1. 导入包就是在导包下的__init__.py文件
2. 使用绝对导入,绝对导入的起始位置都是以包的目录为起始点，本例的起始点是time模块文件夹
3. 但是包内部模块的导入通常应该使用相对导入,用.代表当前所在的文件(而非执行文件),..代表上一级'''


# 2.4包基于相对导入进行调用，找到包自动执行__init__文件
import pypackage1

pypackage1.f2()

pypackage1.f1()

# 注意 多次调用一个包时，里面的__init__文件只运行一次

print('2'+'-'*20)


# 3.datetime包
import  datetime
print(datetime.datetime.now())   #第一个datetime是模块，第二个是datetime是模块中的类对象，now()是类方法

d=datetime.datetime.now()
print(type(d))
# # 单独获取某个时间 年 月
d = datetime.datetime.now()
print(d.year)
print(d.month)
print(d.day)
print(d.hour)
print(d.minute)
print(d.second)
print(d.microsecond)

# # 手动指定时间
print(datetime.datetime(2018,8,9,9,50,00))  # 输出格式化时间
d2 = datetime.datetime(2018,8,9,9,50,00)
print(d-d2)
print(type(d-d2))

# # 替换某个时间单位的值
print(d.replace(year=2019))

# 转换成字符串时间
d_str=d.strftime('%Y-%m-%d %H:%M:%S')
print(d_str)
print(type(d_str))

# timedelta代表两个datetime之间的时间差
print(datetime.timedelta(days=1))
print(datetime.datetime.now()+datetime.timedelta(days=1))
print(type(datetime.timedelta(days=1)))
print(type(datetime.datetime.now()))

# 转换成字符串时间
print((datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S'))
# 增加一天
print((datetime.datetime.now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'))
# 减少一天
print((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d %H:%M:%S'))
print((datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S'))
# 增加一小时
print((datetime.datetime.now()+datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S'))
# 减少一小时
