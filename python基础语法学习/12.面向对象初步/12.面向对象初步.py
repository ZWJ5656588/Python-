# 1.类的介绍
# 使用面向对象的方式对功能进行升级
# 创建类 class——关键字,不能作为变量名称
class Person:  # 大驼峰命名，不用加括号

    def __init__(self, name, age):  # 构造函数，专门用来生产实例属性
        # 对于只一个类的一些属性
        self.name = name
        self.age = age

    def print_info(self):  # 在类中创建一个函数，在这个函数上声明属性（变量）,看到self就表示是实例方法
        print(f"姓名：{self.name},年龄：{self.age}")  # self表示的实例方法只能被实例方法调用，p_2调用之后。self.name->p_2.name


# 如何使用这些类？
# 1.需要这个类进行实例化
p_1 = Person("朱文峻", 21)   # Person（parameter1，parameter2）->返回值调用一些魔术方法，return给一个实例对象
p_2 = Person("刘薇薇", 21)   # “刘薇薇”实参传入类中__init__方法中的name,再赋给self.name,
print(type(p_2))            # <class '__main__.Person'>
print(Person)
print(p_2)                  # 类本身和实例对象不在一个内存空间。类属性和方法[实例方法，静态方法，类方法]存在类本身。实例对象只能存实例属性
print(p_1.print_info)       # 打印实例方法的地址
print(p_2.print_info())
print("-" * 20)

"""类Person创建的两个实例对象p_1,p_2传递给变量，注意是对象"""

p_1.print_info()  # 实例化调用方法，赋给variable p_1
p_2.print_info()  # 存储信息不用担心信息混乱，不需要关注索引对应关系
p_2.name  # 实例属性可以且只能被实例对象调用，
print("-" * 20)


# 2.类和对象
# 在使用对象的过程中，为了将具有共同特征的行为的一组对象的抽象定义，提出了另外一个概念——类
# 类生产对象，创建类，传参实例化，调用实例方法
# 在实例化时返回一个对象，如果对同一个类进行多次实例化时，会在内存开辟对个对象，并且互不干扰


# 3.self参数的解释
class StudentInfo:  # 大驼峰，单词首字母均大写
    # 创建类的属性

    def __init__(self, name, address):
        # 实例属性，只能被实例对象所调用
        self.name = name
        self.address = address

    # 实例方法
    def info(self):  # self其实就是实例对象，self不需要传参
        print(f"我叫{self.name},来自于{self.address}")


# 创建一个类的实例对象
stu_info = StudentInfo("朱文峻", "淮南")
# 创建一个类对象
stu_info1 = StudentInfo  # 类对象就是拿到类的引用
print(stu_info1)
print("-" * 20)

# 调用实例方法的两种办法
stu_info.info()  # 方法1，通过实例对象调用这个方法的时候将这个实例对象传入到方法里面，可以认为self==stu_info，括号里不需要再传self
StudentInfo.info(stu_info)  # 方法2，通过类找到方法，将实例对象传进去
print("-" * 20)


# 4.__init__方法
class Hero(object):
    """定义了一个英雄类，可以移动和攻击"""

    def __init__(self, new_name, new_skill, new_hp, new_atk, new_armor):
        self.name = new_name
        self.skill = new_skill
        self.hp = new_hp
        self.atk = new_atk
        self.armor = new_armor

    def move(self):
        """实例方法"""
        print("%s 正在前往事发地点..." % self.name)  # 实例方法访问实例属性

    def attack(self):
        """实例方法"""
        print("发出了一招强力的%s..." % self.skill)

    def info(self):
        print("英雄 %s 的生命值 :%d" % (self.name, self.hp))
        print("英雄 %s 的攻击力 :%d" % (self.name, self.atk))
        print("英雄 %s 的护甲值 :%d" % (self.name, self.armor))


# 实例化英雄对象时，参数会传递到对象的__init__()方法里
taidamier = Hero("泰达米尔", "旋风斩", 2600, 450, 200)  # 位置形参传入，形参位置和实例化传入实参的位置一样
gailun = Hero("盖伦", "大宝剑", 4200, 260, 400)

# 调用对象方法
taidamier.attack()
taidamier.move()
gailun.move()

print("-"*20)





#-------------------------------大海老师复习总结课
#示例1.类 对象概念
class Teacher:
    # 相同的特征/属性/变量
    name = '大海'
    age = 18
    sex = '男'
    # 函数/方法/技能
    def course(self):
        # self到底是什么？
        # self当做一个位置形参
        print(self)          #打印的是实例对象的引用
        self.address="长沙"   #定义类属性
        print('course')
        return 222
    # print('类定义是运行的')


print(Teacher.__dict__)  #内置方法，键值对形式表示实例
name = 'aaa'
print(name)
# # 调用类的属性
print(Teacher.name)
print(Teacher.age)
print(Teacher.sex)
# 修改类属性的值
print(Teacher.name)
#
Teacher.name = '夏洛'  #修改类属性
#
print(Teacher.name)
# 添加类的属性

Teacher.play = '篮球'
#print(Teacher.play)
print(Teacher.__dict__)
# 删除类的属性
del  Teacher.play
#
# print(Teacher.play)
print(Teacher.__dict__)
teacher=Teacher()
#print(teacher.address)  报错，没运行course方法无法获得实例属性address
teacher.course()
print(teacher.address)
teacher.address="成都"   #修改实例属性
print(teacher.address)

print("-"*20)

#示例2.
class Teacher:
    # 相同的特征/属性/变量
    school = 'tuling'
    xxx = '我是类的属性,也可能是对象的属性'
    yyy = 111
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    # 函数/方法/技能
    def course(self):
        # self到底是什么？
        # self当做一个位置形参
        print(self)
        # print('course')
        #
        # print('-------------------')
        # print('我是大海的属性%s'%self.name)
        # print('我是大海的属性%s'%self.age)
        # return '11111'
        # 类中定义的属性和方法是所有对象共享的,类可以用，对象也可以用
        # 类的属性给对象调用(原装)


# 实例初始化的时候必须传入参数，生成了对象的属性
dahai = Teacher('大海', 18, '男')
xialuo = Teacher('夏洛', 16, '男')
xishi = Teacher('西施', 18, '女')
# 对象属性的查找
# 添加一个对象属性
dahai.xxx= '我是对象的属性'
# 属性查找优先找对象，对象没有才去类里面找
print(dahai.xxx)


print(id(dahai.yyy), dahai.yyy)   #类属性只创建了一个
print(id(xialuo.yyy), xialuo.yyy)
print(id(xishi.yyy), xishi.yyy)
        # # # 类自己用
print(id(Teacher.yyy), Teacher.yyy)
        # 对象小气
#print(Teacher.name)类对象无法调用实例属性

# ？？？？？？
# 对象调用类的方法,不需要传入参数？

print(id(dahai.course))
print(dahai)
dahai.course()

print(id(xialuo.course))
print(xialuo)
xialuo.course()

print(id(xishi.course))
print(xishi)
xishi.course()
print('===============')
# 类调用方法必须传入self参数对应的对象,因为方法里面需要使用这个self对象
Teacher.course(dahai)
Teacher.course(xialuo)
Teacher.course(xishi)
print("-"*20)


#示例3.
# 我们一起来探究一下真相
# self绑定给对象方法
# 简单来说就是对象在调用方法的时候会自动把该对象传入
# 该方法的参数一般这个参数我们用self表示
# self绑定给对象方法
class A:
    # @selfmethed省略了
    # 因为类里面的方法大部分情况下是给实例化后的对象用
    def f(self,n):
        print(self,n)
        print('我是self的方法')
#
a = A()
a1 = A()
print(a)
print('=================')
# # 是哪个对象调用的self参数的方法，那么传入的self就是那个对象
a.f(1)
print(a1)
print('-----------------')
a1.f(1)
# # 类调用必须传入对象 不会自动传入对象 自己手动传入对象
print('*****************')
A.f(a,1)
A.f(a1,2)

# 绑定类的方法是给类用的

class B:
    @classmethod
    def f(cls,n):# cls是一个规范，代表是绑定类的方法
        print(cls,n)
        print('我是绑定类的方法')
print(B)
print('============')
B.f(1)
# # 一般不这样用，绑定给类的方法给对象用
b  = B()
print(b)
b.f(1)


# 非绑定方法/静态方法
class C:
    @staticmethod
    def f(n):
        print(n)
        print('我是非绑定方法/静态方法')
# # # 纯粹的函数，不会自动传入类
C.f(2)
c = C()
# # # 纯粹的函数，不会自动传入对象
c.f(3)
'''
1、绑定方法（精髓在于自动传值）
特性：绑定给谁就应该由谁来调用，谁来调用就会将谁当作第一个参数自动传入
    绑定方法分为两类:
        1.1 绑定给对象方法
            在类内部定义的函数（没有被任何装饰器修饰的），默认就是绑定给对象用的
        1.2 绑定给类的方法：
            在类内部定义的函数如果被装饰器 @classmethod 装饰，
            那么则是绑定给类的，应该由类来调用，类来调用就自动将类当作第一个参数自动传入
2、非绑定方法（不会自动传值，就是一个 普通函数）
    类中定义的函数如果被装饰器 @staticmethod 装饰，那么该函数就变成非绑定方法
    优点
        既不与类绑定，又不与对象绑定，意味着类与对象都可以来调用
    缺点
        但是无论谁来调用，都没有任何自动传值的效果，就是一个普通函数
3 作用
    如果函数体代码需要用外部传入的类，则应该将该函数定义成绑定给类的方法
    如果函数体代码需要用外部传入的对象，则应该将该函数定义成绑定给对象的方法
    如果函数体代码既不需要外部传入的类也不需要外部传入的对象，则应该将该函数定义成非绑定方法/普通函数
'''

