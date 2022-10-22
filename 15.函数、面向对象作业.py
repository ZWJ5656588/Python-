#1.
def func(a,b=[]):

    b.append(a)   #apppend方法返回值是新的列表，

    print(b)
    print(id(b))

func(1)          #函数调用后，默认参数b列表的地址并不改变，并存储在内存中

func(1,[1,2,3])  #即使给b重新赋值，默认参数的地址仍然没有改变并保留在内存中

func(1)

func(1)
print("-"*20)

#2.
def func(a,b={}):

    b[a] = 'v'

    print(b)

func(1)

func(2)


#3.
a = 1

def fun(a):

    a=2

fun(a)

print(a)


#4.写一个函数，将三个数从小到大输出
def print_num(a,b,c):
    if a > b:
        temp=a
        a=b
        b=temp
    if a > c:
        temp = a
        a = c
        c = temp
    if b > c:
        temp = b
        b = c
        c = temp
    print(a,b,c)

print_num(25,129,656)
print_num(656,25,129)


#写一个函数，计算1-990之间的和，用for循环
def sum():
    sum=0
    for i in range(1,991):
        sum+=i
    return sum

print(sum())
print("大傻逼"+"250")