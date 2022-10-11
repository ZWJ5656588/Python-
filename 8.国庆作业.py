#1.
print('ac' in 'abcd')
L = ['a','b','c','d']
print(tuple(L))
print("-"*20)

#2.
info = {'name':'大海','age':38}
print(info["name"])  #字典查询值时用中括号把键括起来
print("-"*20)

# 3：快速生成一个1~10内key为某个数此时value为平方的字典
dict1={x: x ** 2 for x in range(1, 11)}
print(dict1)
print("-"*20)

#4
dict2={1:1}
dict2[2]=2
print(dict2)
print(len(dict2))
print("-"*20)

##5
# name  ='dahai'
# name[3]='w'  程序报错，字符串不可变，不支持直接给字符串指派元素

#6
L1= ['夏洛',1,1.2,(1.22,{'name':[4,5,'大海']})]
print(L1[3][1]["name"][2])
print("-"*20)

#7、
# .用户有这样的一条信息，姓名为翠花，年龄18岁，性别女，请定义一个字典包含了这些信息，然后进行一下操作
#
# 1.增加一个元素，地址为北京
#
# 2.将性别改为男
#
# 3.删除年龄
#
# 4.输出此字典
dict3={"name":"翠花","age":18,"gender":"女"}
dict3["address"]="北京"
dict3["gender"]="男"
del dict3["age"]
print(dict3)
print("-"*20)

#8、
# 第二十题
#
# 定义一个列表，列表中的元素有'安琪拉','妲己','韩信','典韦','吕布'五个元素，然后进行以下操作：
#
#     1.末尾追加两个元素，'小乔','貂蝉'
#
#     2.查找'妲己'的索引
#
#     3.删除'韩信'
#
#     4.将最后一个元素修改为'白起'

"""特别注意，apppend.(),extend.()均无返回值，直接打印新的引用会得到返回值None"""
list2=["安琪拉","妲己","韩信","典韦","吕布"]
list2.extend(["小乔","貂蝉"])
print(list2)
print(list2.index("妲己"))
list2.remove("韩信")
list2[5]="白起"
print(list2)
print("-"*20)

#9.
for i in [0, 1]:
    print(i+1)
print("-" * 20)

#10.
k=0
while k<10 :
    k += 1
    if k!=3:
        print(k)
print("-"*20)

#11.
sum,s=0,1
while s<=10:
    sum=sum+s
    s+=1
print(sum)

#12.1while循环
number1=1
while number1<=10:
    if number1%2==0:
        print(f"{number1}为偶数")
    else:
        print(f"{number1}为奇数")
    number1+=1
print("-"*20)

#12.2for循环
for number2 in range(1,11):
    if number2 % 2==0:
        print(f"{number2}为偶数")
    else:
        print(f"{number2}为奇数")
print("-"*20)

#13./n /r
print("\n你是大傻逼")
print("我测\n你们码")
print("我测'\\n'你们码")#\n前再加一个\转化为普通字符串
print("我测\r你们码") #\r会覆盖前一行内容，光标移到开
print("-"*20)

#14.sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
#list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作
#sorted 语法 sorted(iterable[, cmp[, key[, reverse]]])，sorted可操作性对象为一切可遍历的对象！！，返回值均为list
str1="dsefmnij"
str2="-".join(str1)
print(str2)
list3=str2.split("-")
print(list3)
list3.sort()
print(list3)
list4=sorted(list3,reverse=True) #通过sorted函数返回新列表
print(list4)
str3=sorted(str1)
print(str3)