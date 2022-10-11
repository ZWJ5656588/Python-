# 1.1定义一个函数，完成了独立输出“佛祖镇楼”的功能，可以重复调用
def print_fozu():  # 函数名一般小写，单词与单词之间用下划线隔开
    print("                            _ooOoo_  ")
    print("                           o8888888o  ")
    print("                           88  .  88  ")
    print("                           (| -_- |)  ")
    print("                            O\\ = /O  ")
    print("                        ____/`---'\\____  ")
    print("                      .   ' \\| |// `.  ")
    print("                       / \\||| : |||// \\  ")
    print("                     / _||||| -:- |||||- \\  ")
    print("                       | | \\\\\\ - /// | |  ")
    print("                     | \\_| ''\\---/'' | |  ")
    print("                      \\ .-\\__ `-` ___/-. /  ")
    print("                   ___`. .' /--.--\\ `. . __  ")
    print("                ."" '< `.___\\_<|>_/___.' >'"".  ")
    print("               | | : `- \\`.;`\\ _ /`;.`/ - ` : | |  ")
    print("                 \\ \\ `-. \\_ __\\ /__ _/ .-` / /  ")
    print("         ======`-.____`-.___\\_____/___.-`____.-'======  ")
    print("                            `=---='  ")
    print("  ")
    print("         .............................................  ")
    print("                  佛祖镇楼                  BUG辟易  ")
    print("          佛曰:  ")
    print("                  写字楼里写字间，写字间里程序员；  ")
    print("                  程序人员写程序，又拿程序换酒钱。  ")
    print("                  酒醒只在网上坐，酒醉还来网下眠；  ")
    print("                  酒醉酒醒日复日，网上网下年复年。  ")
    print("                  但愿老死电脑间，不愿鞠躬老板前；  ")
    print("                  奔驰宝马贵者趣，公交自行程序员。  ")
    print("                  别人笑我忒疯癫，我笑自己命太贱；  ")
    print("                  不见满街漂亮妹，哪个归得程序员？")


print_fozu()
print_fozu()
print("-" * 20)

# 1.2一些内置函数
# 1.2.1导出当前时间
from datetime import datetime

print(datetime.now())

# 1.2.2随机数
import random

a = random.uniform(1, 3)  # 输出1-3之间随机浮点数
print("a=", a)
b = random.randint(10, 50)  # 输出10-50之间随机的整数
print("b=", b)
c = random.randrange(0, 51, 2)
print("c=", c)
print("-" * 20)

# 2.1函数参数！！！
# 定义了4个函数
def add_2_nums():
    print("接下来要进行加法操作...")
    num1 = input("请输入第1个数：")
    num2 = input("请输入第2个数：")
    print("%s+%s=%d" % (num1, num2, int(num1) + int(num2)))


def min_2_nums():
    print("接下来要进行减法操作...")
    num1 = input("请输入第1个数：")
    num2 = input("请输入第2个数：")
    print("%s-%s=%d" % (num1, num2, int(num1) - int(num2)))


def mult_2_nums():
    print("接下来要进行乘法操作...")
    num1 = input("请输入第1个数：")
    num2 = input("请输入第2个数：")
    print("%s*%s=%d" % (num1, num2, int(num1) * int(num2)))


def div_2_nums():
    print("接下来要进行除法操作...")
    num1 = input("请输入第1个数：")
    num2 = input("请输入第2个数：")
    print("%s/%s=%d" % (num1, num2, int(num1) / int(num2)))


"""上述的代码，虽然能够实现2个数的加减乘除，但有个较大的问题：

4个函数中每次都需要重新获取这2个数字，我们如果想要计算1和2的加减乘除的结果，就需要输入4遍数字1，4遍数字2，这太麻烦了

想要解决这个问题，大体的思路应该是，在调用加减乘除这4个函数之前先获取要操作的2个数字，然后将这2个数字传递给函数让它们直接用即可而不是每个函数都重新获取

Python中如果在调用函数时，需要将数据传递给函数，这就用到了一个新的"传参数"""


def test(num1, num2):  # 形参：调用函数时用来存储数据的变量 优化
    print("传递过来的第1个数是:%d" % num1)
    print("传递过来的第2个数是:%d" % num2)
    print("它们俩的和是:%d" % (num1 + num2))


test(100, 200)  # 实参：在调用函数时传入具体的值
print("-" * 20)


#3.1 函数返回值
"""想要用函数的返回结果，我们需要注意2点
- 定义函数时，需要使用return将结果返回
- 调用函数时，需要存储这个返回值（当然了语法上来讲可以不存，但一般情况下都会存储，否则还要返回值干什么）"""

#3.1.1 return还有结束函数体的作用


def add(num1,num2):
    return num1+num2 #返回给add，可以通过变量的形式获取到结果


add(1,2) # 此时调用不会输结果
result=add(1,2) #此时return返回的结果会存在变量result中
print(result)
print(add(1,2))
print("-"*20)


#3.1.2 一个函数中只能有1个return被执行，可用通过return返回列表、元组、集合、字典等从而实现一次性返回多个数
def create_nums():
    print("---1---")
    return 1, 2, 3 #默认返回元祖


ret = create_nums()  # 此时ret存储了列表(1,2,3)
print(ret)
print("-"*20)

#3.1.3 函数的调用和引用
"""函数名如果带着圆括号，则表示立即调用函数，调用要执行函数的功能及返回值 
，若不加圆括号，则是引用函数，引用其地址"""
def test():
    print("鸡你太美")
    return "顶针珍珠"
print(test())
print(test)# <function test at 0x0000019690C99480> 表示为function类型，test变量名，内存地址0x009994A8
print(("-"*20))

def a1():
    return 5+8


def b1():
    return a1
c=b1()
print(c)
d=c()
print(d)
print("-"*20)


#3.1.4一个函数中有多个return,与 if else合用
def create_nums(num):
    print("---1---")
    if num == 100:
        print("---2---")
        return num + 1  # 函数中下面的代码不会被执行，因为return除了能够将数据返回之外，还有一个隐藏的功能：结束函数
    else:
        print("---3---")
        return num + 2
    print("---4---") #print不会被执行，因为pr在def代码块中，不在if的代码块中 return会将def结束


result1 = create_nums(100)
print(result1)  # 打印101
result2 = create_nums(200)
print(result2)  # 打印202
print("-"*20)

#4.1有参数返回值的函数
#4.1.1计算1-num的累计和


def add_nums1(num):
    sum_result=0
    for x in range(1,num+1):
        sum_result+=x
    return sum_result


result=add_nums1(75)
print(result)

#5.1 函数之间的独立性
"""我们知道函数是一个具有独立功能的代码块，在前面的学习中知道一般情况下把一个个功能都单独做成一个个函数，像之前实现加减乘除就定义了4个函数
在开发时，把独立功能做成一个函数其实就是封装的思想，通过这种方式能够让代码更加整洁
打个比方，当我们离开家乡去远方上学时，往往会大包小包的拎着，每个包中肯定是相类似的物品，这样不仅携带方便在打开包裹取东西时也非常方便，这其实就是”封装“
Python中，根据封装的级别不同，我们会陆陆续续学习到函数、类、对象、模块、包等
"封装"最大的特点就是高内聚低耦合，大白话讲：相关的功能全部封装到函数中（这是高内聚），尽量减少函数与函数之间的依赖（低耦合），也就是说一个函数的改的对其他的函数来说没有影响
因此以后我们在编写代码的时候，谨记“高内聚低耦合”，尽量做到与函数与函数之间没有关系
大家要注意哦“低耦合"可不是"零耦合"，也就是函数之间多多少少还是有千丝万缕的关系，大白话讲：函数之间还是有些关系的"""

def add_1(num1,num2):
    return num1+num2


def add_2(num1,num2):
    return num1-num2


res=add_1(1,2)
print(res)
res=add_2(2,3)
print(res)  #封装，在函数题修改代码对其他函数没有任何影响
print("-"*20)

#5.2 函数之间的相互关系
"""根据代码的不同，存在3种关系
- 可能共用同一个变量，会导致一函数添加了数据，另外一个函数删除了数据
- 可能一个函数的返回值，被当做另外一个函数的参数
- 可能一个函数体中调用了另外一个函数"""

# 5.2.1 多个函数使用同一个全局变量
g_num = 0  # 全局变量


def test_1():
    global g_num   #global是py中的一个关键字，作用是告诉py解释器要在函数体对全局变量进行修改，一般用在int float,序列类型可以不声明
    # 将处理结果存储到全局变量g_num中
    g_num = 100


def test_2():
    print(g_num)  #如果第一个函数中g_num不用global声明，打印值仍为0，认为函数1中的g_num为局部变量，函数2无法访问

# 先调用test_1得到数据并且存到全局变量中
test_1()
# 再调用test_2打印test_1()处理过后的数据
test_2()
print("-"*20)

#5.2.2 函数返回值当做实参变量
def test_1():
    return 50


def test_2(num):
    print(num)


# 先调用test_1获取该函数的返回值
result = test_1()
# 调用test_2时将test_1的返回值传入进去
test_2(result)

#5.2.3 函数中调用另一个函数（函数嵌套）
def test_1():
    # 通过return将一个数据结果返回
    return 20


def test_2():
    # 在test_2函数体中调用test_1并获取test_1的返回值
    result = test_1()
    # 在当前函数体中处理数据
    print(result)


# 调用test_2完成数据处理
test_2()
print("-"*20)

#6.1 全局变量和局部变量
"""在一个函数中如果定义了一个变量，则优先使用函数体内的局部变量，
若函数体内没有找到，则会跳出函数体寻找全局变量，如没有找到，则报错"""

#6.1.2 修改全局变量 global
"""global关键字作用于不可变类型 整型"""
globals_int=10
globals_list=[1,2,6,9,8]


def test_3():
    """如果需要修改整型则需要添加关键字global"""
    global globals_int
    globals_int=201

    #修改列表类型全局变量
    globals_list.append(4)


def test_4():
    print(globals_int)
    print(globals_list)


test_3() #先调用test_()修改全局变量
test_4()



