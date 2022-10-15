#1.类的介绍
#使用面向对象的方式对功能进行升级
#创建类 class——关键字,不能作为变量名称
class Person:    #大驼峰命名，不用加括号


    def __init__ (self,name,age): #构造函数，专门用来生产实例属性
        #对于只一个类的一些属性
        self.name=name
        self.age=age


    def print_info(self):  #在类中创建一个函数，在这个函数上声明属性（变量）,看到self就表示是实例方法
        print(f"姓名：{self.name},年龄：{self.age}")  #self表示的实例方法只能被实例方法调用，p_2调用之后。self.name->p_2.name

#如何使用这些类？
#1.需要这个类进行实例化
p_1=Person("朱文峻",21)  #Person（parameter1，parameter2）->返回值调用一些魔术方法，return给一个实例对象
p_2=Person("刘薇薇",21)#“刘薇薇”实参传入类中__init__方法中的name,再赋给self.name,
print(type(p_2))  #<class '__main__.Person'>
print(Person)
print(p_2)        #类本身和实例对象不在一个内存空间。类属性和方法[实例方法，静态方法，类方法]存在类本身。实例对象只能存实例属性
print("-"*20)

"""类Person创建的两个实例对象p_1,p_2传递给变量，注意是对象"""

p_1.print_info()   #实例化调用方法，赋给variable p_1
p_2.print_info()  #存储信息不用担心信息混乱，不需要关注索引对应关系
p_2.name          #实例属性可以且只能被实例对象调用，
print("-"*20)

#2.类和对象
#在使用对象的过程中，为了将具有共同特征的行为的一组对象的抽象定义，提出了另外一个概念——类
#类生产对象，创建类，传参实例化，调用实例方法
#在实例化时返回一个对象，如果对同一个类进行多次实例化时，会在内存开辟对个对象，并且互不干扰


#3.self参数的解释
class StudentInfo: #大驼峰，单词首字母均大写
    #创建类的属性

    def __init__(self,name,address):
            #实例属性，只能被实例对象所调用
            self.name=name
            self.address=address

    #实例方法
    def info(self):#self其实就是实例对象，self不需要传参
        print(f"我叫{self.name},来自于{self.address}")


#创建一个类的实例对象
stu_info=StudentInfo("朱文峻","淮南")
#创建一个类对象
stu_info1=StudentInfo #类对象就是拿到类的引用
print(stu_info1)
print("-"*20)

#调用实例方法的两种办法
stu_info.info()             #方法1，通过实例对象调用这个方法的时候将这个实例对象传入到方法里面，可以认为self==stu_info，括号里不需要再传self
StudentInfo.info(stu_info)  #方法2，通过类找到方法，将实例对象传进去



