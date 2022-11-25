# 类当中的方法
"""实例方法，静态方法，类方法"""
"""只有实例方法（self）可以访问实例属性（self.variable)"""

"""实例对象中保存了实例属性
   类对象中保存的是方法和类属性！！！"""


# 1.1设置一个私有属性

class StudentInfo:
    # 创建一个构造方法
    def __init__(self, name, age):
        self.name = name
        # 私有属性
        self.__age = age

    def set_age(self, new_age):
        # 私有方法可以在类的内部进行操作,用实例方法修改
        if 10 <= new_age <= 60:
            self.__age = new_age

    def info(self):
        print(f"我叫{self.name},今年{self.__age}岁")


stu = StudentInfo("朱文峻", 21)
stu.info()
stu.set_age(22)
stu.info()

print("-" * 20)


# 将这个学生年龄修改
# stu.__age=18  因为是私有属性，无法进行修改

# 2.1私有方法
class BankService:
    # 调用该方法时会返回True,并且打印
    def __bank_2_bank(self, money):
        print("这里是银行之间转账的代码 ")
        return True

    def transfer(self):
        money = int(input(("请输入转账的金额： ")))
        if money > 1000000:
            if self.__bank_2_bank(money):
                print(f"转账成功，到账{money}元")
            else:
                print("转账失败")  # 因为__bank_2_bank的返回值永远为True,else后不会执行
        else:
            print("都没有一百万，别转了")


bank_service = BankService()  # 创建实例方法
bank_service.transfer()  # 调用公有方法
# bank_service.__bank_2_bank()      私有方法无法直接调用 'BankService' object has no attribute '__bank_2_bank'

print("-" * 20)


# 3.1引用对象关联
class Classroom(object):
    def __init__(self, name):
        self.classroom_name = name


class Student(object):
    def __init__(self, name):
        self.student_name = name
        print(self.student_name)


print("-" * 20)

# 创建一个教室对象
class205 = Classroom("205班")
# 创建一个学生对象
stu01 = Student("学生1")
# 直接给教室对象添加属性
"""Classroom类型创建一个实例属性，指向Stuent类下的实例对象，该属性被class205实例对象调用"""
class205.stu = stu01
class205.stu
print("-" * 20)


# 3.2关联对象的调用
class Classroom(object):
    def __init__(self, name):
        self.classroom_name = name
        self.stu = None  # 定义一个实例属性用来接收要关联的对象

    def add_new_stu(self, stu):
        """定义实例方法完成关联"""
        self.stu = stu


class Student(object):
    def __init__(self, name):
        self.student_name = name


# 创建一个教室对象
class205 = Classroom("205班")
# 创建一个学生对象
stu01 = Student("学生1")
# 调用方法将学生添加到对象中
class205.add_new_stu(stu01)  # 将stu01这个实例对象通过Classroom的实例方法add_new_stu，传递给实例属性self.stu,完成关联

# ！！！那如何调用关联的对象呢，在这个例子中也就是学生的姓名
"""最终是要stu01的实例对象调用到实例属性student_name才会被name赋值
而stu01被class205.stu这一实例属性指向，所以可以得到如下关系"""
print(stu01.student_name)
print(class205.stu.student_name)
print("-" * 20)


# 3.3关联多个对象的调用
class Classroom(object):
    def __init__(self, name):
        self.classroom_name = name
        self.stus = []  # 一般情况下在本类的其它方法中用到的实例属性，都要在__init__方法中定义

    def add_new_stu(self, stu):
        """定义新方法用来完成关联"""
        # self.stu = stu
        self.stus.append(stu)


class Student(object):
    def __init__(self, name):
        self.student_name = name


# 创建一个教室对象
class205 = Classroom("205班")

# 创建多个学生对象
stu01 = Student("学生1")
stu02 = Student("学生2")
stu03 = Student("学生3")

# 调用方法将学生添加到对象中
class205.add_new_stu(stu01)
class205.add_new_stu(stu02)
class205.add_new_stu(stu03)

# 调用学生的姓名
# 205教室.列表[下标].姓名
print(class205.stus[0].student_name)
print(class205.stus[1].student_name)
print(class205.stus[2].student_name)
print(class205.stus[0])


# 4.继承
class A:
    def __init__(self):
        self.num = 10

    # 实例对象打印实例属性
    def print_num(self):
        print(self.num)


class B(A):
    pass


b = B()
b.print_num()
print(b.num)  # 实例方法b传入实例属性self中，直接调用实例属性b.name(不加self!!)
print("-" * 20)

"""在当前案例中，除了实例方法被继承，构造函数也被继承"""


# 4.1单继承
class Animal:
    # 详细信息
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("吃饭...")

    def drink(self):
        print("喝水...")

    def sleep(self):
        print("睡觉...")

    def info(self):
        print(f"我叫：{self.name}，年龄:{self.age}")


class Dog(Animal):
    pass


dog = Dog("旺财", 3)  # 这种父类创建构造方法，子类要想调用必须传入相关参数，若其他类不想调用，则会白白浪费很多空间
# dog = Dog()  #报错
dog.eat()
dog.drink()
dog.sleep()
dog.info()
print("-" * 20)

"""现在给狗类添加一个方法
    并且调用，一般要定义在子类"""


# 4.2多继承
class Camera:
    def take_photo(self):
        """拍照功能"""
        print("正在拍照...")


class MP3:
    def play_music(self):
        """播放音乐功能"""
        print("正在播放音乐...")


class Telephone(Camera, MP3):
    def call(self):
        """打电话"""
        print("正在打电话...")

    def answer(self):
        """接电话"""
        print("正在接电话...")


phone = Telephone()
phone.call()
phone.answer()
phone.take_photo()
phone.play_music()

print("-"*20)


# 5.1方法重写

class Father:
    def play_game(self):
        print("为父正在玩游戏")

    def eat(self):
        print("父亲正在吃饭")

    def drink(self):
        print("父亲正在喝水")


class Son(Father):
    # 需要对父类打游戏的方法进行重写
    def play_game(self):
        print("儿子在打游戏")


father = Father()
father.play_game()

son = Son()
son.play_game()  # 与父类方法名相同时，以子类方法为准，称之为方法重写
son.eat()
print("-" * 20)

# 5.2 super方法
"""上一节课程我们知道，如果父类中的方法在派生的子类中不能满足其需求的话，可以在子类中通过重写解决这个问题

但是很多情况下，父类中的方法并不是全部一点都不能用，即子类的需求往往是在父类方法实现的功能基础上提出了更多的需求而已

，此时如果我们在子类中重写此方法时就会发现出现了很多冗余的代码，这个问题该怎么解决呢？

答：在子类重写的方法中通过调用父类中被重写的方法"""


class Father:
    def play_game(self):
        print("为父正在玩游戏")


class Son(Father):
    def play_game(self):
        # 在重写的方法中调用父类的打印语句 （不用复制，用super方法）
        super().play_game()  # super（）可以看做Father的实例对象，通过实例对象对应父类的实例方法play_game
        print("儿子在玩游戏")


son = Son()
son.play_game()
print(Son.__mro__)  # super（）的类看mro，是第二个类的实例对象


# 5.3super方法案例
class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__  当print（实力对象)会自动调用__str__方法
    def __str__(self):
        return "%s的年龄是：%d" % (self.name, self.age)


class Son(Father):
    def __init__(self, name, age, college):
        # 需要在子类的构造方法中调用父类的构造方法
        # 因为在父类中有两个实例属性，在子类中将两个实例属性传递给父类
        super().__init__(name, age)
        self.college = college

    def __str__(self):
        return "%s的年龄是 %d,他的学历是 %s" % (self.name, self.age, self.college)


father = Father("父亲", 40)
print(father)

son = Son("儿子", 18, "高中")
print(son)

"""子类中重写了父类的构造方法，并且父类中构造方法中的属性子类
可以用的到，则可以使用super().__init__()将父类所需要的参数进行传递
并且可以在子类中创建属于子类的独有属性"""

print("-" * 20)


# 5.4super方法进阶使用
class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__  当print（实力对象)会自动调用__str__方法
    def __str__(self):
        return "%s的年龄是：%d" % (self.name, self.age)


class Son(Father):
    def __init__(self,name,age,college):
        # 需要在子类的构造方法中调用父类的构造方法
        # 因为在父类中有两个实例属性，在子类中将两个实例属性传递给父类
        super().__init__(name,age)
        self.college = college

    def __str__(self):
        return "%s的年龄是 %d,他的学历是 %s" % (self.name, self.age, self.college)


class GrandChild(Son):
    def __init__(self,address,*args,**kwargs):  # 孙子类实例化时自动调用__init__就已经打印了“当前子类需要完成的其他事情....”
        super().__init__(*args) # 父类（儿子类）没 有打印
        self.address=address
        self.gender=kwargs['gender']
        print("当前子类需要完成的其他事情....")

    def __str__(self):
        return "%s的年龄是 %d,他的学历是 %s,住址是 %s,性别是%s" % (self.name, self.age, self.college,self.address,self.gender)



father = Father("父亲", 50)
print(father)

son = Son("儿子", 26,"研究生")
print(son)

grand_child = GrandChild("成都","孙子",2,"未上学",gender="女")
print(grand_child)  # print自动执行__str__方法，继承的是son所以此处super()的实例对象是son

print("-" * 20)


# 6.1多态
class Dog(object):
    def bark(self):
        print("狗汪汪叫...")


class Dog:
    def bark(self):
        print("狗汪汪叫")


class LongDog(Dog):
    def bark(self):
        print("细狗汪汪叫")


class ZangAo(Dog):  #没有dog方法，向父类询问
    pass


class Person(object):
    def __init__(self, name):
        self.name = name

    def person_pk_dpg(self, dog):
        print(f"{self.name}在打狗")
        self.dog=dog
        dog.bark()  # 对象关联


zwj = Person("朱文峻")

dog1 = Dog()
dog2 = LongDog()
dog3 = ZangAo()

zwj.person_pk_dpg(dog1)  # 在person_pk_dog中的dog参数存储的是一个实例对象的引用
zwj.person_pk_dpg(dog2)
zwj.person_pk_dpg(dog3)


#多态：一个类调用多个同名方法，并产生的行为不一样


#-------------------------------大海老师复习总结课
print("-"*30)
#示例1.

class Parent1:
    xxx = 333
    def run(self):
        print('我是父类的方法')


class Sub1(Parent1):
    xxx = 222
    def run(self):
        print('我是子类的方法')
    pass


obj = Sub1()
par1=Parent1()
print(Parent1.xxx)  #333
print(obj.xxx)      #222
obj.xxx=111
# 对象 << 类 << 父类
print(obj.xxx)    #子类实例属性>子类类属性>父类
obj.run()


#示例2.
'''
总结对象的相似之处得到了类
总结类的相似之处得到父类
'''
class People:
    school = '图灵学院'
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex


class Student(People):
    # def __init__(self,name,age,sex):
    #     self.name = name
    #     self.age = age
    #     self.sex = sex
    def play(self):
        print('%s play football，他 %d 岁了' % (self.name,self.age))


class Teacher(People):
    def __init__(self,workplace,*args):
        super(Teacher,self).__init__(*args)
        self.workplace=workplace
    #     self.name = name
    #     self.age = age
    #     self.sex = sex
    def course(self):
        print('%s course,性别 %s'%(self.workplace,self.sex))
# 实例化的时候子类没有__init__方法会调用父类的
stu1 = Student('周阳',30,'male')
print(stu1.__dict__)     #__dict__方法作用于实例对象只会打印出实例属性的键值对成字典
tea1 = Teacher("成都石室中学",'大海',31,'man')
print(tea1.__dict__)
stu1.play()
tea1.course()



# 但是这里有个问题子类有新的属性需要实例化的时候参数怎么办