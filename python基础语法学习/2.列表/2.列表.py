# 1.列表的可变属性
list1 = [1, 2, 3, 4, 5]
list1.append(7)
print(list1)
print("_" * 20)

# 1.1 列表的切片，得到一个新列表
stu_names0 = ['张三', '李四', '王五']
print(stu_names0[1:3])  # 此时得到一个新列表 [李四', '王五']
print("-" * 20)

# 2.1遍历列表 for循环
stu_names1 = ['张三', '李四', '王五']
for name in stu_names1:
    print(name, end=" ")
print("\n", "_" * 20)

# 2.2 遍历列表 while循环
stu_names2 = ['张三', '李四', '王五']
length = len(stu_names2)
i = 0
while i < length:
    print(stu_names2[i])
    i += 1
print("_" * 20)

# 3.1 append 方法,在列表最后添加元素，列表独有，并且一次仅仅添加一个元素
stu_names3 = ['张三', '李四', '王五']
print(stu_names3)
for name in stu_names3:
    print(name)
print("_" * 20)
# 提示、并添加元素
temp = input("请输入添加学生的姓名：")
stu_names3.append(temp)
print("-----添加之后，列表的数据-----")
for name in stu_names3:
    print(name)
print("_" * 20)

# 3.2 extend 方法,通过extend可以将另一个列表中的元素逐一添加到列表中,不同于列表相加，列表相加得到新列表，地址改变
# extend可以添加序列类型（元组，字符串，字典keys）
a1 = [1, 2]
b1 = [3, 4]
c1 = "sdsd"
d1 = (7, 5, "sdwer")
a1.append(b1)
print(a1)
a1.extend(b1)
print(a1)
a1.extend(c1)
print(a1)
a1.extend(d1)
print(a1)  # a列表的值已经被改变 而地址不变
print("_" * 20)
"""特别注意，apppend.(),extend.()均无返回值，直接打印新的引用会得到返回值None"""
print(a1.extend(d1))

# 3.3 insert 方法insert(index, object)在指定位置index（索引，理解为下标即可）前插入元素object
a2 = [0, 1, 2]
a2.insert(1, 3)
print(a2)
print("_" * 20)

a = 10
print(id(a))
a *= 10
print(id(a))  # number地址改变
print("_" * 20)

print(9 / 2)
print(9 // 2)
print(3 * 1 ** 3)
print("_" * 20)

# 4.1 in not in 查询值是否在序列中
# 待查找的列表
stu_names4 = ['张三', '李四', '王五']
# 获取用户要查找的名字
find_name = input('请输入要查找的姓名:')
# 查找是否存在
if find_name in stu_names4:  # in为关键字，判断值是否在序列中
    print('找到了名字')
else:
    print('没有找到')
print("_" * 20)

# 4.2 count方法统计元素出现在列表的次数
list_obj = ("东南大学", "武汉大学", "北京航空航天大学", "山东大学", "武汉大学")
print(list_obj.count("武汉大学"))

# 5.1 del关键字，根据下标进行删除
movie_names = ['加勒比海盗', '骇客帝国', '第一滴血', '指环王', '霍比特人', '速度与激情']
print('------删除之前------')
print((movie_names))
for name in movie_names:
    print(name)
del movie_names[2]  # 这里根据下标进行删除，del关键字在前
print('------删除之后------')
for name in movie_names:
    print(name)
# del 可以删除整个列表 del movie_names 删除列表定义！！！
print("-" * 20)

# 5.2 pop方法，取出最后一个元素，可以赋值给另一个变量(有返回值）
# pop.()括号内可以指定下标位置进行取出，若括号内无内容则默认取出最后一个元素
# 接5.1
movie_name = movie_names.pop()
print(movie_names)
print("pop弹出元素", movie_name)

# 5.3 remove方法，指定元素名称进行删除
# 接5.1
print('------删除之前------')
for name in movie_names:
    print(name)
movie_names.remove('指环王')  # 删除指定的数据
print('------删除之后------')
for name in movie_names:
    print(name)
print("_" * 20)

# 5.4 clear方法，清空列表中的元素，列表还存在，仍对应相关地址，与del区别
k = [1, 54, "sduuy", "北京", 258.22]
print(k)
print(id(k))
k.clear()
print(k)
print(id(k))
print(("-" * 20))

# 6.1 sort方法仅可以对列表进行数据排序
# sort方法是将列表按特定顺序重新排列，默认为由小到大，参数reverse=True可改为倒序，由大到小。
float_list = [1.5, 62, 23.564, 44.222]
print(float_list.sort())  # sort函数返回值为None
print(float_list)
float_list.reverse()  # 倒序，将列表索引从大到小排列
print(float_list)
print(("-" * 20))

# 6.2.sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
# list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作
# sorted 语法 sorted(iterable[, cmp[, key[, reverse]]])，sorted可操作性对象为一切可遍历的对象！！，返回值均为list
str1 = "dsefmnij"
str2 = "-".join(str1)
print(str2)
list3 = str2.split("-")
print(list3)
list3.sort()
print(list3)
list4 = sorted(list3, reverse=True)  # 通过sorted函数返回新列表
print(list4)
str3 = sorted(str1)
print(str3)

print("-"*20)

# 6.4 zip函数
"""将多个序列压缩成一个对象，就是
将序列中对应位置的元素重新合成一个个新的元组，返回一个object元组迭代器"""
# 6.4.1zip(interable,...)
a = [1, 2, 3]
b = [5, 6, 7]
c = zip(a, b)
# print(c) 输出迭代器的类型object at...
# 提取迭代器的方法，list(),next(),for循环
print(list(c))  # output [(1, 5), (2, 6), (3, 7)]

# 6.4.2zip()与*运算相结合用来拆解列表
x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print(zipped)
print(*zipped)  # 将迭代器拆包成元组
print("-" * 20)

# 6.4.3 列表长度不相等，取决于最短元素
var1 = "123"
var2 = ["a", "b", "c", "d"]
var3 = ("A", "B", "C", "D", "E")
# 调用zip,组成新的迭代器
res = zip(var1, var2, var3)
for i in res:
    print(i)

print(iter(var2))  # <list_iterator object at 0x00000223CA5934C0>
