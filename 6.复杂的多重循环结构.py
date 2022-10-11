# 1.1or关键字中，如果第一个表达式条件成立，则不会运行之后第n个表达式！
# 代码执行顺序，从上到下，从左到右

# 1.2布尔类型表达式可能返回的不是True，Flase
print(100 and 200)  # 返回200
print(100 and 100 > 50)
print(0 and 100 > 50)

# py中能表示false的有以下几个：Flase,0,None,空的数据结构,C语言中没有bool类型，用0,1表示
#python继承了C的一些功能

# 1.3多重if循环
ticket = True  # 用True代表有车票，False代表没有车票
knife_lenght = 9  # 刀子的长度，单位为cm
if ticket == 1:
    print("有车票，可以进站")
    if knife_lenght < 10:
        print("通过安检")
        print("终于可以见到Ta了，美滋滋~~~")
    else:
        print("没有通过安检")
        print("刀子的长度超过规定，等待警察处理...")
else:
    print("没有车票，不能进站")
    print("亲爱的，那就下次见了")
print("-" * 20)

# 1.4if代码案例,猜拳游戏
import random

player = int(input('请输入：剪刀(0)  石头(1)  布(2):'))
# 生成一个随机整数：0、1、2 中的某一个
computer = random.randint(0, 2)
# 用来进行测试
# print('player=%d,computer=%d',(player,computer))
if ((player == 0) and (computer == 2)) or ((player == 1) and (computer == 0)) or ((player == 2) and (computer == 1)):
    print('获胜，哈哈，你太厉害了')
elif player == computer:
    print('平局，要不再来一局')
else:
    print('输了，不要走，洗洗手接着来，决战到天亮')

# 2.1 while 循环
i = 0
while i < 5:
    print("当前是第%d次循环" % (i + 1))
    print(("i=%d" % i))
    i += 1
print("-" * 20)

# 2.2 1-100的偶数和
i, sum = 1, 0
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1
print(f'1-100之间的偶数和为{sum}')
print("-" * 20)

# 2.3 计算1-100之间能被3整除且能够被7整除的所有数之和
i = 1
sum1 = 0
while i <= 100:
    if i % 3 == 0 and i % 7 == 0:
        sum1 += i
    i += 1
print((sum1))
print("-" * 20)

# 2.4 print格式化输出
i = 1
while i <= 5:
    print("%d--->%d" % (i, i * i))
    i += 1
print("-" * 20)

# 2.5#while嵌套
# 2.5.1三角*图案输出
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print("\n")
    i += 1
print("-" * 20)

# 2.5.2 while多层嵌套输出9*9乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('%d*%d=%d' % (j, i, i * j), end=" ")
        j += 1
    print("\n")
    i += 1
print("-" * 20)

#3.1 for循环
#3.1.1for循环计算1-100整数和
sum2=0
for i in range(1,101):
    sum2+=i
print(sum2)

#4.1 else用在循环结构中的情况
#4.1.1 else与break并存
i=3
while i>0:
    password=input("请输入密码：（还剩%d次机会）"%i)
    if password=="123456":
        print("密码输入正确")
        break  #遇到break,continue,则不走else直接跳出循环
    i-=1
else:
    print("密码三次全部输入错误，请明日再试")
print("-" * 20)

#4.1.2 else与continue并存



#4.1.2