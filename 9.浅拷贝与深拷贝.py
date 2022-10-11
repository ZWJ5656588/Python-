#1.1不可变类型：数字，字符串，元组
str1="python"
str2="python"
print(id(str2)==id(str1)) #不可变类型，赋值相同数据，内存中地址不改变
print("-"*20)

tuple1=(1,2,3,4,5)
tuple2=(1,2,3,4,5)
print(f"元组1的地址为{id(tuple1)}")
print(f'元组2的地址为{id(tuple2)}')
print("-"*20)

#1.2可变类型 列表，字典，集合
list1=[1,2,3]
list2=[1,2,3]
print(f"lsit1的地址为:{id(list1)}")
print(f"lsit2的地址为:{id(list2)}") #对于可变类型，数据相同时不同变量名开辟的内存地址是不同的
list3=list1
print(f"lsit3的地址为:{id(list3)}")
list1.append(4)
print(list1)
print(list3)
print("-"*20)

#2.1一个变量多次赋值
#一个变量多次赋值时，内存地址会相应改变
tuple1=(1,5,2)
print(id(tuple1))
tuple1=(2,5)
print(id(tuple1))
print("-"*20)

#2.2变量赋值
#将一个变量赋给另一个变量，实质上是一个对象，数据相同，内存地址相同
a=1
b=a
print(id(a))
print(id(b))
a=2  #a的地址改变，b地址不变
print(b)
print(id(a))
print(id(b))
