# 1.1缺省参数
# 也叫做默认参数，是指定义函数时形参变量有默认值，如果调用函数时没有传递参数，那么函数就用默认值，如果传递了参数就用传递的那个数据。
def print_info(name, class_name, grade, department_name, school_name="图灵学院"):
    print("老师好：我是来自 %s(大学) %s系 %s年级 %s班级 的学生，我叫%s" % (
        school_name,
        department_name,
        grade,
        class_name,
        name
    ))


print_info("顾安", "爬虫", "二", "软件工程")
print_info("顾安", "爬虫", "二", "软件工程", "图灵python")

"""缺省参数只能在形参的最后（即最后侧）
- 缺省参数全挨在一起（在右侧），不是缺省参数挨在一起（在左侧）"""

# >>> def printinfo(name, age=35, sex): 参数位置错误
# ...     print name
# ...
# File "<stdin>", line 1
# SyntaxError: non-default argument follows default argument
print("—" * 20)


# 1.2命名参数
# 指：在调用函数时，传递的实参带有名字，这样的参数叫做命名参数  #关键字参数
def test(a, b, c=100, d=200):
    print("a=%d, b=%d, c=%d, d=%d" % (a, b, c, d))


# 下面的方式都成功
test(11, 22)  # c,d使用默认值
test(11, 22, 33)
test(11, 22, 33, 44)
test(11, 22, d=33, c=44)

# # 下面的方式都失败
# test(c=1, d=2)  # 缺少a、b的值
# test(c=1, d=2, 11, 22)  # 11, 22应该在左侧
print("—" * 20)

# 1.3不定长参数
"""不定长参数：定义函数的时候形参可以不确定到底多少个，这样的参数就叫做不定长参数

不定长参数有2种方式表示

- *args ：表示调用函数时多余的未命名参数都会以元组的方式存储到args中（位置不定）
- **kwargs：表示调用函数时多余的命名参数都会以键值对的方式存储到kwargs中 （关键字不定）

注意：

- *和**是必须要写的，否则就变成了普通的形参了
- 当我们说不定长参数的时候，就是指*args和**kwargs"""

def test(a, b, *args, **kwargs):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))      #元组
    print(kwargs, type(kwargs))  #字典，

test(11, 22, 33, 44, 55, 66, name='顾安', address='长沙')
#**kwargs一定要在最后，*args可以在中间，但是不推荐使用，代码混乱
""""- *args后可以有缺省参数，想要给这些缺省参数在调用时传递参数，需要用命名参数传递，否则多余的未命名参数都会给args
- 如果有`kwargs的话，kwargs`必须是最后的"""
print("—" * 20)


def sum_nums_3(a, *args, b=22, c=33, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


sum_nums_3(100, 200, 300, 400, 500, 600, 700, b=1, c=2, mm=800, nn=90)  #传参时，mm,nn没有引号，打印时自动添加表示字符串类型
print("—" * 20)


# 2.1返回值拆包
def test(a, b, c):
    print(a + b + c)


nums = [11, 22, 33]
test(*nums)  # 此时的*的作用就是拆包，此时*nums相当于11, 22, 33 即test(11, 22, 33)  传参拆包
print("—" * 20)



def test(a=1, b=2, c=3):
    return a,b,c


a,b,c=test()
print(a)
print(b)
print(c)

print("—" * 20)


nums = (11, 22, 33)
test(*nums)  # 对于数组来说也是可以用*拆表
print("—" * 20)


def test(a, b, c):
    print(a + b + c)


print("—" * 20)

nums = {11, 22, 33}
test(*nums)  # 集合同上
print("—" * 20)

# 2.2**对字典进行拆包，返回的是命名参数。
"""使用**可以对字典进行拆包，拆包的结果是命名参数"""


def test(name, age, address):
    print(name)
    print(age)
    print(address)


info = {
    "name": "顾安",
    "age": 18,
    "address": "长沙"
}

test(**info)
'''
当前**info相当于以下代码：
	name='顾安'
	age=18
	address='长沙'

** 主要对字典进行拆包
'''

# 匿名函数lambda
# lambda x,y:x+y.定义了一个匿名函数，冒号后面代表要返回的结果，用于仅仅一次的情况
print(lambda x, y: x + y)   #打印匿名函数地址

# 3.1
result = lambda a, b: a + b
result(1, 2)


# 3.2
def func(a, b, obj):
    print(f"a={a}")
    print(f"b={b}")
    print(f"result={obj(a, b)}")


func(1, 2, lambda x, y: x + y)  # lambda匿名函数可以作为传统函数的实参进行传递


print("—" * 20)

# 3.3
students = [
    {"name": "顾安", "age": 38},
    {"name": "安娜", "age": 20},
    {"name": "双双", "age": 60},
]
# 根据名称进行排序，lambda函数
print(students)
# unicode编码集
students.sort(key=lambda x: x["age"])# key后面是排序规则
print(students)
students.sort(key=lambda x: x["name"])
print(students)

print("—" * 20)


#3.4 max(可迭代对象）
salaries={
          "xialuo":300000,
          "xishi":30000,
          "dahai":3000
}

print(max(salaries))

"""max底层是for循环，默认比较字典的key
比较的是key,返回的也是key,现在要比较value，返回key"""
"""写一个函数来改变比较规则"""
def run(name):
    return salaries[name]

# max(可迭代对象，key=函数名)
# 这个key=函数名(地址，引用,不能加括号)，可以改变max的比较规则
#底层for循环实现
# for i in salaries:
#     print(run(i))
print("-"*20)

"""实现value的比较，返回key"""
print(max(salaries,key=run))  #注意传递的是run函数的地址
print(min(salaries,key=run))
"""run函数只需要地址不需要调用，传入方法，此时定义成匿名函数！！！"""
print(max(salaries,key=lambda name:salaries[name]))
print(min(salaries,key=lambda name:salaries[name]))


print("-"*20)

#3.4.1
#sorted方法进行迭代器的排序
salaries2={
          "xialuo":600000,
          "xishi":60000,
          "dahai":6000
}
print(salaries2.items())    #输出dict_items([('xialuo', 600000), ('xishi', 60000), ('dahai', 6000)])
print("-"*20)

"""与max,min一样，都是通过底层for实现，同时将可迭代对象转换为迭代器"""
# 循环遍历薪资
for v in salaries.values():
    print(v)
for k in salaries.keys():
    print(k)

print("-"*20)

# 若不做key=lambda处理，比较什么返回什么
print(sorted(salaries2.values(),reverse=True))   #反叙，从大到小
print(sorted(salaries2.keys(),reverse=False))

print("-"*20)

print(sorted(salaries2.keys(),key=lambda x:salaries2[x],reverse=True))




# 求最大值
print(max(salaries, key=lambda name:salaries[name]))

# 但是我们是要比较薪资，返回的却是人名
# 薪资反序
print(sorted(salaries,key=lambda name:salaries[name],reverse=True))
print(sorted(salaries,key=lambda name:salaries[name],reverse=False))

print("-"*20)


# 4.1递归函数
# 实现计算阶乘 n = 1 * 2 * 3 * ... * n
#
# 阶乘分解：
#
#     1 = 1
#     2 = 2 × 1
#     3 = 3 × 2 × 1
#     4 = 4 × 3 × 2 × 1
#
# 循环方法：
def result_nums(n):
    ret = 1
    for x in range(1, n + 1):
        ret *= x
    return ret


res = result_nums(4)
print(res)
print("-"*20)

#4.1.2 先回溯再递推
"""第几个同学定义为n
age(n)=age(n-1)+2,n>1
age(n)=18,        n=1"""
def age (n):
    if n==1:
        return 18  #递推开始条件，也是回溯的结束
    elif n>1:
        return age(n-1)+2  #回溯

print(age(10))
print("-"*20)


#4.1.3 嵌套列表取数字
L = [1,[2,[3,[4,[5,[6,[7,[8,[9,]]]]]]]]]
def get_number(list):
    for n in list:
        if isinstance(n,int):
            print(n,end=" ")
        else:
            return get_number(n)

get_number(L)

print("\n"+"-"*20)



#4.2  可变类型形参不会销毁
def func(a,b=[]):

    b.append(a)   #apppend方法返回值是新的列表，

    print(b)

func(1)

func(1)

func(1)

func(1)

print("-"*20)


#  5.1 推导式
print([i*10 if i%2==0 else i+5 for i in range(1,10)])
"""等效于"""
L=list()
for i in range(1,10):
    if i%2 ==0:
        L.append(i*10)
    else:
        L.append(i+5)
print(L)

print("-"*20)

#5.1.1列表生成式排序
ts_file=['1.ts','8.ts','3.ts','5.ts','10.ts','9.ts','4.ts','6.ts','7.ts','2.ts']
print(ts_file)
_file=[i.replace(".ts",'')for i in ts_file]
print(_file)
int_file=[int(i)for i in _file]
print(int_file)
sorted_file=sorted(int_file)
print(sorted_file)
str_sortedfile=[str(i)+".ts"for i in sorted_file]
print(str_sortedfile)                   #结果

print("-"*20)

#5.1.2 字典生成式
# 字典生成式

dict1={k+'aaa':v for k,v in {'name':'大海','age':18}.items() if k == 'age'}
print(dict1)

print("-"*20)


#6.1闭包函数、
def outer():
    # 自由变量
    name = '大海'
    print('外面的函数正在运行')
    def inner():
        print('里面的函数正在运行')
        return name
    return inner
inner=outer()
# print(name)   报错，自由变量受函数体保护，不能直接调用
print(inner())



