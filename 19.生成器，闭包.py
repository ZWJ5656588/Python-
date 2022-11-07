"""在Python中，使用生成器可以很方便的支持迭代器协议。生成器通过生成器函数产生，生成器函数可以通过常规的def语句来定义，
但是不用return返回，而是用yield一次返回一个结果，在每个结果之间挂起和继续它们的状态，来自动实现迭代协议。
也就是说，yield，每次返回一个值，是一个语法糖，内部实现支持了迭代器协议，同时yield内部是一个状态机，维护着挂起和继续的状态。
"""

# 1.1生成器的概念
def my_range(n):   # 本质是一个函数
    print("开始G迭代")
    i=0  # 创建一个计数器
    while i < n:
        yield  i
        i+=1

# 直接函数名加括号不可以直接调用，要赋给一个变量进行接收
print(my_range(3))    # 打印出生成器的信息及地址 <generator object my_range at 0x0000019A18553120>
my_range=my_range(3)
print(my_range)       # <generator object my_range at 0x0000019A18553120>

#生成器是一个特殊的迭代器，所以要使用next方法迭代
print(next(my_range))

print("-"*20)

for item in my_range:   #生成器中被取出了一个0，只有1,2可以通过for遍历
    print(item)

print("-"*20)

#2.1 生成器的工作流程
def my_range2(n):
    print("开始迭代2")
    i=0
    while i < n:
        print("迭代中")
        yield i
        i+=1
        print("迭代结束")
        yield "继续"


#创建一个变量接收生成生成器所返回的迭代器对象
my_iter=my_range2(5)
print(next(my_iter))    #执行到yeild被打断
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

print("-"*20)

"""1. 当调用生成器函数的时候，函数只是返回了一个生成器对象，并没有执行。
2. 当next()方法第一次被调用的时候，生成器函数才开始执行，执行到yield语句处停止: next()方法的返回值就是yield语句处的参数（yielded value）
3. 当继续调用next()方法的时候，函数将接着上一次停止的yield语句处继续执行，并到下一个yield处停止；如果后面没有yield就抛出StopIteration异常
"""


#3.1 生成器表达式，
#由于列表等容器需要占用系统内存，并且在生成内存的时候将元素创建出来，用生成式生成列表运行速率较慢

"""这种情况考虑生成器表达式"""
iter_list=(i for i in range(5000000))  #瞬间执行完毕

#执行迅速的原因
"""1.生成器表达式返回的不是一个具体的序列数据，返回的是生成器对象
2.使用next()获取这个生成器的值，在内存中只有一个"""

"""
第一次调用next获取返回值0
第二次调用next获取返回值1，覆盖了上一个值
"""
#
# for item in iter_list:
#     print(item)   运行速度很快


#4.1
gen = (i for i in range(10000) if i % 2)

print("__iter__" in dir(gen))
print("__next__" in dir(gen))
print("你" in {2:"我",6:"你"})    # 判断字典中是否有相应的键

print("-"*20)

# 使用sum求和之后会导致再次迭代所获取的值为空
print(sum(gen))   #实现列表求和
#生成器返回一个值，相当于移除一个值，保证当前内存只有一个值
print([i for i in gen])

print("-"*20)

#5.1迭代器复习
# 实现一个可迭代的对象
from collections.abc import Iterable

class My_range3:
    def __init__(self):
        self.my_list=[]

    def add(self,item):
        self.my_list.append(item)

    def __iter__(self):
        return MyIterator(self)         #这里__iter__需要返回一个迭代器，需要知道迭代的流程,传入具有__next__方法的实例对象


#写一个迭代的流程 __next__方法
class MyIterator:
    def __init__(self,obj):
        self.index=0
        self.obj=obj

    #
    # def __iter__(self):        # 返回一个迭代器
    #     return self

    def __next__(self):
        if self.index < len(self.obj.my_list):
            result=self.obj.my_list[self.index]
            self.index+=2
            return  result
        raise  StopIteration

#创建一个实例对象
my_range3=My_range3()
#添加对象
my_range3.add(1)
my_range3.add(2)
my_range3.add(5)
my_range3.add(7)
my_range3.add(6)
my_range3.add(8)
#对象关联
myinterator=MyIterator(my_range3)

for i in my_range3:
    print(i)
#for循环第一步要判断my_range3是否是可迭代对象，因为有__iter__，所以不报错

print("-"*20)

# 6.1 send() 与close() 方法
# send可以向yield传入参数
def my_range4(n):
    i=0
    while i < n:
        str_value=yield i
        if str_value=="你好":
            print("当前判断方法被执行")
        i+=1
        print(str_value)

my_iter1=my_range4(5)
#send()与next()方法类似，区别是send()可以向yield传参
#send可以向生成器传递参数，但第一次获取值时必须传递None
# print(my_iter1.send("666"))  #报错  TypeError: can't send non-None value to a just-started generator
print(my_iter1.send(None))
print(my_iter1.send("你好"))
print(my_iter1.send("nihao"))


#close 方法 关闭生成器
def my_range5(n):
    i=0
    while i < n:
        str_value1=yield i
        if str_value1=="你好":
            print("当前判断方法被执行")
        i+=1
        print(str_value1)


my_iter2=my_range5(5)
print(next(my_iter2))
my_iter2.close()  # 关闭生成器 后面再使用next(my_iter2)会报错！！

print("-"*20)

#7. 用迭代器改造学生系统
class StuSystem:
    """学生管理系统"""
    def __init__(self):
        self.stus=[]
        self.new_stu = {}
        self.current_num=0

    def add(self):
        """添加一个学生的基本信息"""
        name=input("请输入学生姓名")
        tel=input("请输入学学生手机号")
        addresss=input("请输入学生的地址")
        # self.new_stu={}
        self.new_stu["name"]=name
        self.new_stu["tel"]=tel
        self.new_stu["address"]=addresss
        self.stus.append(self.new_stu)

    def __iter__(self):
        return self
    #自己就是一个迭代器，使用了__next__方法，之前的例子返回的是迭代器类的实例对象
    #本例中直接把生成迭代器__iter__方法和迭代具体顺序__next__方法写在一个类中

    def __next__(self):
        if self.current_num < len(self.stus):
            ret=self.stus[self.current_num]
            self.current_num+=1
            return ret
        else:
            # self.current_num=0
            raise StopIteration


stu_sys=StuSystem()

stu_sys.add()
stu_sys.add()
stu_sys.add()

stu_list=[x for x in stu_sys]
print(stu_list)

print("-"*20)


#  8. 闭包函数
"""
1.外层函数的返回值是内层函数的引用
2.内层函数可以访问外层函数的变量
"""
def info_name():
    print("我是朱文峻")
    def info_gender():
        print("性别男")
        def info_address():
            print("我在成都")
            def info_tel():
                print("我的电话是19130616725")
                return None
            return info_tel
        return info_address
    return info_gender


info_name()
print("\n")
info_name()()
print("\n")
info_name()()()
print("\n")
info_name()()()()

print("-"*20)

"""
面向对象返回的是实例方法，闭包返回的是函数的引用
形成闭包的条件
1.函数嵌套，外接函数接收内层函数的返回值，该返回值是内层函数的引用
2.内层函数调用外层函数的参数
"""

a=info_name
b=info_name
print(a is b)
c=[1,2,3]
d=[1,2,3]
print(id(c))
c.append(5)
print(c)
print(id(c))
print(id(d))
e=20
f=20
print(e is f)
g=c.append(5)
print(id(g))
print(id(c) ==id (g))

print("-"*20)


#  8.1 内层函数修改外层函数参数
def counter(start=0):
    def add_one():
        nonlocal start  # nonlocal 关键字用于在嵌套函数内部使用变量，其中变量不应属于内部函数。！！！！ 应用于不可变类型，因为要改变地址
        start += 1
        return start
    return add_one

c1 = counter(5)  # 创建一个闭包
print(c1())
print(c1())

c2 = counter(50)  # 创建另外一个闭包
print(c2())
print(c2())

print(c1())
print(c1())

print(c2())
print(c2())

#调用了2次counter，也就意味着创建了2个闭包，并且每个闭包之间没有任何关系。
#调用时创建一个空间来接收引用，运行代码，
"""
1.引用是返回当前代码的储存地址
2.调用时创建一个空间来运行代码，两次调用就是开辟两个空间运行
"""
print(id(c1))
print(id(c2))

print("-"*20)


#8.3 闭包函数中中的拆包测试
#闭包中可以有多个内层函数
def person(name):
    def address_info(address):
        return f'{name}:{address}'
    def gender_info(gender):
        return f'{name}:{gender}'

    """此时return以元组的形式返回两个函数的引用"""
    return address_info,gender_info

per1=person("朱文峻")
print(per1[0]("成都"))
per2=person("刘薇薇")
print(per2[1]("女"))

print("-"*20)

def person(*args):
    def address_info(address):
        return f'{args[0]}:{address}'
    def gender_info(gender):
        return f'{args[1]}:{gender}'

    """此时return以元组的形式返回两个函数的引用"""
    return address_info,gender_info

per3,per4=person("哈登","杜兰特")
print(per3("Philadephia"))
print(per4("男"))

print("-"*20)

def person(**kwargs):
    def address_info(address):
        return f"{kwargs['anna']}:{address}"
    def gender_info(gender):
        return f'{kwargs["shuangshuang"]}:{gender}'

    """此时return以元组的形式返回两个函数的引用"""
    return address_info,gender_info


per5,per6=person(anna="安娜",shuangshuang="双双")
print(per5("长沙"))
print(per6("女"))
