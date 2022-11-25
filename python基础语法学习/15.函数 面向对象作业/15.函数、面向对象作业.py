# 1.

def func(a, b=[]):
    b.append(a)  # apppend方法返回值是新的列表，

    print(b)
    print(id(b))


func(1)  # 函数调用后，默认参数b列表的地址并不改变，并存储在内存中

func(1, [1, 2, 3])  # 即使给b重新赋值，默认参数的地址仍然没有改变并保留在内存中

func(1)

func(1)
print("-" * 20)


# 2.

def func(a, b={}):
    b[a] = 'v'

    print(b)


func(1)

func(2)

# 3.

a = 1


def fun(a):
    a = 2


fun(a)

print(a)


# 4.写一个函数，将三个数从小到大输出

def print_num(a, b, c):
    if a > b:
        temp = a
        a = b
        b = temp
    if a > c:
        temp = a
        a = c
        c = temp
    if b > c:
        temp = b
        b = c
        c = temp
    print(a, b, c)


print_num(25, 129, 656)
print_num(656, 25, 129)


# 5.写一个函数，计算1-990之间的和，用for循环
def sum():
    sum = 0
    for i in range(1, 991):
        sum += i
    return sum


print(sum())
print("大傻逼" + "250")

print("-" * 20)


# 6.student类介绍个人信息
class Student:

    def __init__(self, *args, **kwargs):
        self.info = kwargs

    def print_info(self):
        print(f"我的名字是{self.info['name']},性别{self.info['gender']},年龄{self.info['age']}")


dic_info = {'name': '朱文峻', 'gender': '男', 'age': '21'}
zwj = Student(**dic_info)
zwj.print_info()

print("-" * 20)


# 7. 声明一个电脑类

class Computer:

    def __init__(self, brand, color, memory_space):
        self.brand = brand
        self.color = color
        self.memory_space = memory_space

    def play_game(self):
        print("这是打游戏方法")

    def write_code(self):
        print("这是写代码方法")

    def watch_video(self):
        print("这是看视频方法")


cpu1 = Computer("dell", "white", "256GB")
del cpu1.color
# print(cpu1.color) 报错
cpu1.play_game()
cpu1.write_code()
cpu1.watch_video()

print("-" * 20)


# 8.创建一个Person类，添加类属性用来统计Person类对象个数

class Person(object):
    count = 0

    def __init__(self):
        Person.count += 1

    @classmethod
    def print_count(cls):
        print(f"累计创建的实例对象个数为{Person.count}")


p1 = Person()
p2 = Person()
p3 = Person()
p4 = Person()
p5 = Person()
Person.print_count()

print("-" * 20)


# 9.声明一个矩形类

class Rectangle:

    def __init__(self,length,width):
        self.length=length
        self.width=width

    def calculate_circumferernce(self):
        print(f"该矩形的周长是{(self.length+self.width)*2}")

    def calculate_area(self):
        print(f"该矩形的面积是{self.width*self.length}")


r1=Rectangle(7,6)
r1.calculate_area()
r1.calculate_circumferernce()
r2=Rectangle(9,7)
r2.calculate_circumferernce()
r2.calculate_area()

print("-"*20)

#10.
class Box:
    def __init__(self,length,width,height):
        self.l=length
        self.w=width
        self.h=height

    def cal_volume(self):
        print(f"该立方体体积是{self.h*self.w*self.l}")

    def cal_superficial_area(self):
        print(f"该立方体表面积是{2*(self.h*self.w+self.w*self.l+self.l*self.h)}")


b1=Box(1,2,3)
b1.cal_volume()
b1.cal_superficial_area()


