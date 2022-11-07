# 异常处理可以避免程序崩溃
# 1. 异常处理分支
try:
    L = [1, 2]
    print('===========')
    print('===========')
    L[2]
    print('===========')
    print('===========')
    print('===========')
except IndexError as f:
# 一但捕获到了异常
    print('兄弟检查一下你的代码')
    print(f)
except NameError as f:
# 一但捕获到了异常
    print('兄弟检查一下你的代码')
    print(f)
else:
    #     # 程序没有抛出异常的时候执行
    print('代码正确')
finally:
    #     # 不管有错没错 一定会执行的部分
    print('完成了异常捕获')
# print('aaaaaaaaa')

print("-"*20)

# 2. 异常合并
try:
    L = [1, 2]
    a            #a未定义，直接被捕获，不会执行try代码块剩下的代码
    print('===========')
    print('===========')
    print('===========')
    L[2]
except (IndexError,NameError) as f:
# 一但捕获到了异常
    print('兄弟检查一下你的代码')
    print(f)
else:
    #     # 程序没有抛出异常的时候执行
    print('代码正确')
finally:
    #     # 不管有错没错 一定会执行的部分
    print('完成了异常捕获')
# print('aaaaaaaaa')

print("-"*20)


# 3.万能捕获
# 万能捕获 Exception
try:
    d = {'x':1,'y':2}
    d['z']
    L = [1, 2]
    L[2]
    # 结束运行了
    print('===========')
    print('===========')
    print('===========')
    # 不会运行
    a
except Exception as f:
# 一但捕获到了异常
    print('兄弟检查一下你的代码')
    print(f)
else:
    #     # 程序没有抛出异常的时候执行
    print('代码正确')
finally:
    #     # 不管有错没错 一定会执行的部分
    print('完成了异常捕获')
# print('aaaaaaaaa')

print("-"*20)


# 4.1.9.筛选列表里面的字典key带有sex的字典
info =[
    {'name':'dahai','age':18,'sex':'男'},
    {'name':'dahai1','age':24,'sex':'男'},
    {'name':'xialuo','age':78},
    {'name':'dahai2','age':27,'sex':'女'},
    {'name':'xishi','age':8}
]
for i in info:
    try:
        print(i["sex"])
    except Exception as f:
        print(i)

print("-"*20)

#  4. 枚举
good_list=["哈登","维斯布鲁克","杜兰特"]
for i,item in enumerate(good_list):
    print(i,item)

print("-"*20)

print({str(index):item for index,item in enumerate([3,6,3,8,6,5,4,7])})
print({str(index):item for index,item in enumerate([3,6,3,8,6,5,4,7]) if index % 2==0})
print({str(index):item for index,item in enumerate([3,6,3,8,6,5,4,7]) if item % 2==0})

print("-"*20)


# 5.1 装饰器！！！！  函数对象+函数闭包的产物
""" 1、不修改被装饰对象的源代码(人的原来的性格，生活方式)
    2、不修改被装饰对象的调用方式(人的原来的外貌，名字)
       装饰器其实就在遵循1和2原则的前提下为被装饰对象添加新功能
"""
# 5.1函数地址可以存在于容器中
def pay():
    print('支付。。。')

def withdraw():
    print('取款。。。')

def transfer():
    print('转账。。。')

def check_balance():
    print('查看余额。。。')

def shopping():
    print('购物。。。')

func_dic={
    '1':pay,
    '2':withdraw,
    '3':transfer,
    '4':check_balance,
    '5':shopping
}

while True:
    msg="""
    1 支付
    2 取款
    3 转账
    4 查看余额
    5 购物
    6 退出
    """
    print(msg)
    choice=input('>>: ').strip()   #去除多余空格
    if choice == '6':
        break
    if choice not in func_dic:
        print('输入的指令不存在')
        continue
    func_dic[choice]()

print("-"*20)

# 5.2 装饰器装饰无参函数
def run():
    print("===========")
    print("我是大海")
    print("===========")


def decorate(func):  #传入我们被装饰函数的对象run(函数地址)
    # print(func)
    # 等下要运行闭包内层函数new_func这个函数，也就是装饰体
    def new_func():
        print("我是被装饰函数的代码")
        func()
        print("我是被装饰函数后面的代码")
    return  new_func


de=decorate(run)
de()

print("\n"+"-"*20+"\n")

# 5.3 装饰器装饰有参函数
name1= '大海'
def run_dahai(name):
    print('============')
    print('我是%s'%name)
    print('============')


name2 = '夏洛'
def run_xialuo(name):
    print('============')
    print('我是%s'%name)
    print('============')


# # # 装饰器就是一个特殊的闭包函数
#  # 1.定义了decorate，检测decorate语法, new_func没有定义
def decorate(func):# 传入我们被装饰的函数对象(函数的地址)
    # print(func)# run
    # 等下我们是要运行这个new_func这个函数
    def new_func(*args,**kwargs):
        print('我是被装饰函数前面的代码')
        func(*args,**kwargs)
        print('我是被装饰函数后面的代码')
    return new_func
# 定义new_func，和返回这个函数new_func的地址，
# 调用decorate
run_dahai=decorate(run_dahai)
run_dahai(name1)# 参数实际上是传给了new_func这个函数
run_xialuo=decorate(run_xialuo)
run_xialuo(name2)# 参数实际上是传给了new_func这个函数

print("\n"+"-"*20+"\n")


#6. 时间装饰器
from datetime import  datetime
n=9000000

# 要计算此函数运行所花费的时间
def for1(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    print(sum)


def run_time(func):
    def new_func(*args,**kwargs):
        start_time=datetime.now()
        print(f"开始时间是{start_time}")
        func(*args,**kwargs)
        end_time=datetime.now()
        print(f"结束时间是{end_time}")
        time1=end_time-start_time
        print(f"花费的时间是{time1}")
    return new_func


for1=run_time(for1)
for1(n)



# 7. 装饰器快捷用法@
"""将被修饰函数与装饰体写出，在被装饰函数前引用@装饰体函数即可，不需要进行复杂调用"""

 