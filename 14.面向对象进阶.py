#类当中的方法
"""实例方法，静态方法，类方法"""
"""只有实例方法（self）可以访问实例属性（self.variable)"""

"""实例对象中保存了实例属性
   类对象中保存的是方法和类属性！！！"""

#1.1设置一个私有属性

class StudentInfo:
    #创建一个构造方法
    def __init__(self,name,age):
        self.name=name
        #私有属性
        self.__age=age


    def set_age(self,new_age):
        #私有方法可以在类的内部进行操作,用实例方法修改
        if 10 <= new_age <= 60:
            self.__age=new_age


    def info(self):
        print(f"我叫{self.name},今年{self.__age}岁")


stu=StudentInfo("朱文峻",21)
stu.info()
stu.set_age(22)
stu.info()

print("*"*20)



#将这个学生年龄修改
#stu.__age=18  因为是私有属性，无法进行修改

#2.1私有方法
class BankService:
    #调用该方法时会返回True,并且打印
    def __bank_2_bank(self,money):
        print("这里是银行之间转账的代码 ")
        return True


    def transfer(self):
        money=int(input(("请输入转账的金额： ")))
        if money > 1000000:
            if self.__bank_2_bank(money):
                print(f"转账成功，到账{money}元")
            else:
                print("转账失败")  #因为__bank_2_bank的返回值永远为True,else后不会执行
        else:
            print("都没有一百万，别转了")



bank_service=BankService() #创建实例方法
bank_service.transfer()    #调用公有方法
#bank_service.__bank_2_bank()      私有方法无法直接调用 'BankService' object has no attribute '__bank_2_bank'

print("*"*20)


#3.1引用对象关联
class Classroom(object):
    def __init__(self, name):
        self.classroom_name = name


class Student(object):
    def __init__(self, name):
        self.student_name = name
        print(self.student_name)


print("*"*20)


# 创建一个教室对象
class205 = Classroom("205班")
# 创建一个学生对象
stu01 = Student("学生1")
# 直接给教室对象添加属性
"""Classroom类型创建一个实例属性，指向Stuent类下的实例对象，该属性被class205实例对象调用"""
class205.stu = stu01
class205.stu
print("*"*20)

#3.2关联对象的调用
class Classroom(object):
    def __init__(self, name):
        self.classroom_name = name
        self.stu=None   #定义一个实例属性用来接收要关联的对象


    def add_new_stu(self,stu):
        """定义实例方法完成关联"""
        self.stu=stu



class Student(object):
    def __init__(self, name):
        self.student_name = name


# 创建一个教室对象
class205 = Classroom("205班")
# 创建一个学生对象
stu01 = Student("学生1")
# 调用方法将学生添加到对象中
class205.add_new_stu(stu01)   #将stu01这个实例对象通过Classroom的实例方法add_new_stu，传递给实例属性self.stu,完成关联

#！！！那如何调用关联的对象呢，在这个例子中也就是学生的姓名
"""最终是要stu01的实例对象调用到实例属性student_name才会被name赋值
而stu01被class205.stu这一实例属性指向，所以可以得到如下关系"""
print(stu01.student_name)
print(class205.stu.student_name)
print("*"*20)



#3.3关联多个对象的调用
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

#创建多个学生对象
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

