# 1.1单纯的重复不是迭代
# i = 0
# while True:
#     print(i)

""""迭代器本质上计数器，迭代器协议就是迭代器的实现过程"""

# 1.2. 迭代是一重复的过程，每一次重复都是基于上一次的结果而来
l = ['a','b','c']
# # # #  0   1   2
i = 0
while i< len(l):
    # print(i)
    print(l[i])
    i += 1
# # 哪些数据类型需要这样迭代取值?
# # 字符串 列表 元组 字典 集合 文件等等  文件***
l = ['a','b','c']
a = 'abc'
t = ('a','b','c')
# dic = {'name':'dahai','age':18}
i = 0
while i< len(t):
    # print(i)
    print(t[i])
    i += 1


# 所以我们需要一种不依赖索引取值的方式
# 迭代器提供了一种通用的且不依赖于索引的迭代取值方式的功能


# 2.1 可迭代对象
#一 ：可迭代的对象iterable：但凡内置有__iter__方法的对象都称之为可迭代的对象
# 因为__iter__方法这个方法可以生成迭代器
# 作者是个天才，每个需要取值的都加了__iter__方法
a = 1
# a.__iter__没有
b = 1.1
# # b.__iter__没有
c = 'hello'
c.__iter__()
d = ['a','c']
# d.__iter__()
g = {1,2,3}
# g.__iter__()
#打开文件，只读,可生成迭代器
f = open('18.txt.','rt')
# f.__iter__()

# 迭代器
# 执行可迭代对象下的__iter__方法，返回的值就是一个迭代器
#迭代器具有__next__()方法，可迭代对象没有，迭代器也是一个对象
# dic是可迭代对象

print("-"*20)

# 2.2 使用迭代器
dic = {'x':1,'y':2,'z':3}
# # # # # # 可迭代对象变成迭代器，迭代器更加节约内存！！！
iter_dic=dic.__iter__()    #执行__iter()__方法后返回值是迭代器，赋值给iter_dict
print(iter_dic)            #<dict_keyiterator object at 0x00000262B3BF80E0>
# # # # 迭代器  range 母鸡
#按key的顺序取key
print(iter_dic.__next__())
print(iter_dic.__next__())
print(iter_dic.__next__())

print("-"*20)

#再创建一个可迭代的字典dic2，利用迭代器依次取value
dic2 = {'a':4,'b':5,'c':6}
iter_dic2=dic2.__iter__()
print(dic2[iter_dic2.__next__()])
print(dic2[iter_dic2.__next__()])
print(dic2[iter_dic2.__next__()])

print("-"*20)


# # # # # #StopIteration应该被当成一种结束信号，代表迭代器取干净了
# print(iter_dic.__next__())

# 2.2.1列表不依赖索引取值
l = [1,2,3]
iter_l = l.__iter__()
# # print(iter_l)
print(iter_l.__next__())
print(iter_l.__next__())
print(iter_l.__next__())
# # # # # # #StopIteration应该被当成一种结束信号，代表迭代器取干净了
# print(iter_l.__next__())

print("-"*20)


# 2.2.2  误区
l = [1,2,3]
# 基于新的迭代器 l.__iter__()
# # 生成了一个迭代器，并且取了第一个值
print(l.__iter__().__next__())# 1
# # 又生成了一个迭代器，并且取了第一个值
print(l.__iter__().__next__())
# # 又生成了一个迭代器，并且取了第一个值
print(l.__iter__().__next__())
# # # # # 迭代是基于老的
iter_l = l.__iter__()
print(iter_l.__next__())
print(iter_l.__next__())
print(iter_l.__next__())
# # StopIteration应该被当成一种结束信号，代表迭代器取干净了
# print(iter_l.__next__())
print("-"*20)


#3.1  迭代器与可迭代对象
# 作者是个天才，每个需要取值的都加了__iter__方法，可以变成迭代器，还有些直接就是迭代器，比如文件
a = 1
# a.__iter__没有
b = 1.1
# # b.__iter__没有
c = 'hello'
# c.__iter__()
# # c.__next__()没有
d = ['a','c']
# d.__iter__()
# # d.__next__没有
g = {1,2,3}
# g.__iter__()
# g.__next__没有
f = open('18.txt','rt')
f.__iter__()
f.__next__()

# 可迭代对象与迭代器  *****
# 可迭代对象
# 只有__iter__方法，没有__next__方法
# 迭代器
#1. 既内置有__next__方法的对象，执行迭代器__next__方法可以不依赖索引取值
#2. 又内置有__iter__方法的对象，执行迭代器__iter__方法得到的仍然是迭代器本身
# 1 迭代器一定是可迭代的对象，而可迭代的对象却不一定是迭代器
#    可迭代的对象只需要有__iter__()
#    迭代器对象 __iter__()  __next__()
f = open('18.txt','rt')
# f是迭代器  文件是迭代器，可以直接调用__next__方法进行迭代
print(f)
print(f.__next__())   #print自带换行效果，文件中也有换行，所以换了两次
print(f.__next__())
# # StopIteration应该被当成一种结束信号，代表迭代器取干净了
# print(f.__next__())
# # # #  调用可迭代的对象__iter__得到的是迭代器，
# # # # 执行迭代器__iter__方法得到的仍然是迭代器本身,那么有什么用
print(f.__iter__() is f.__iter__().__iter__().__iter__().__iter__())

"""上面是为了和for循环配合使用，无论迭代器还是迭代对象，for循环底层先执行__iter__方法，确保生成一个迭代器
且每一个for循环都生成且只生成一个全新的迭代器"""

print("-"*20)


#4.1 for循环和·迭代器
# # 为了for循环
#   iter()  next()
dic = {'x':1,'y':2,'z':3}
# # # # 可迭代对象生成迭代器
# # # # 底层
iter_dic = dic.__iter__()
print(iter_dic)
iter_dic = iter(dic)   #将可迭代对象变成迭代器
print(iter_dic)        #<dict_keyiterator object at 0x0000020F9F961C20>
# # # 内置方法
print(next(iter_dic))
print(next(iter_dic))
print(next(iter_dic))
# # StopIteration应该被当成一种结束信号，代表迭代器取干净了
# print(next(iter_dic))

print("-"*20)


#4.2 while+异常处理  引出for循环遍历迭代器
dic = {'x':1,'y':2,'z':3}
iter_dic1=iter(dic)
"""在不知到迭代器长度的时候进行__next__方法迭代，要进行while循环并且异常处理"""
while True:
    try:
        print(next(iter_dic1))
    except StopIteration:       #异常捕获！！！
        break
"""以上功能相当于for循环！！！！"""
print('=================')
while True:
    try:
        print(next(iter_dic1))
    except Exception :          #所有异常的基类
        break


#4.3
# 有没有一种好的方法自己把
# 1.可迭代对象变成迭代器
# 2.能够自己获取迭代器next的值
# 3.next最后不报错
#for本质应该称之为迭代器循环
# 生成一个迭代器
l = [1,2,3]
iter_l = l.__iter__()
print(iter_l)
# # # # #  调用可迭代的对象__iter__得到的是迭代器，
# # # # # 执行迭代器__iter__方法得到的仍然是迭代器本身,那么有什么用
print(f.__iter__() is f.__iter__().__iter__().__iter__().__iter__())

print("-"*20)


# # 为了for循环
#1. 先调用in后面那个对象的__iter__方法，将其变成一个迭代器
      # 如果是个迭代器__iter__可以变成迭代器      老的迭代器，不会更新迭代器
#     # 如果是个可迭代对象__iter__可以变成迭代器   新的迭代器
#2. 调用next(迭代器)，将得到的返回值赋值给变量名  k
#3. 循环往复直到next(迭代器)抛出异常，for会自动捕捉异常StopIteration然后结束循环
l= [1,2,3]
print(iter(l).__next__())      #每次获取新的迭代器
print(iter(l).__next__())
print(iter(l).__next__())

print("-"*20)

iter1=iter(l)
print(next(iter1))             #迭代器iter1只获取了一次
print(next(iter1))
print(next(iter1))

print("-"*20)

for k in l:                     #for循环获取了新的迭代器 不会出现StopIteration报错
    print(k)
# # # # # # 为什么下一次又可以
# # # # # # 因为又做了上面三件事 又变成了一个新的迭代器

print("-"*20)

for k in l:
    print(k)

print("_"*20)

f = open('18.txt','rt')
print(f is f.__iter__())   #f是一个迭代器
print(next(f))

for line in f:              #文件f本身就是一个迭代器，此时for循环不再生成新的迭代器！！！
    print(line,end='')

print("\n"+"-"*20)







#5.1  自定义迭代器,实现原理
from collections.abc import Iterable     #Iterable是可迭代对象的基类

class Mylist:          # 1. 把普通类的对象变成可迭代对象
    def __init__(self):
        self.containor=[]

    def __iter__(self):  # 转换为可迭代对象，此方法要返回一个迭代器
        return Interator_Mylist(self)

    def add(self,item):
        self.containor.append(item)



class Interator_Mylist :       # 2.  自定义一个迭代器,并进行对象关联
    def __init__(self,my_list):
        self.my_list=my_list
        self.count=0

    def __iter__(self):        # 返回一个迭代器
        return self

    def __next__(self):        # 声明是一个迭代器,调用一次计数器+1，所以内部定于if取代while
        if(self.count<len(self.my_list.containor)):
            item=self.my_list.containor[self.count]
            self.count+=1
            return item         # 将具体的元素值返回出去
        else:
            #关键字raise,抛出一个错误,for循环遇到此异常会自动停止，for循环不断调用next()函数
            raise StopIteration

my_list=Mylist()
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.add(4)
my_list.add(5)

interator_mylist=Interator_Mylist(my_list)

for item in my_list:
    print(item)



