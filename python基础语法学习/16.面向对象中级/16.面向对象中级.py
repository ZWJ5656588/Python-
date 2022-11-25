# 1.1静态方法
class Test:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(self.name)

    def __todo(self):
        print("这是要做的事情")

    def set_def(self):
        self.__todo()

    @staticmethod  # 调用静态方法,可以使用实例对象或者类对象进行调用
    def info_2():
        print("今天天气不错")


# 测试静态方法调用
test = Test("安娜")
test.info_2()

# 使用类对象进行静态方法的调用 ！！！与一般实例方法不同
Test.info_2()
"""1.静态方法可以用实例对象还有类对象调用

   2.静态方法没有self,无法访问实例属性
   
   3.静态方法在类的内部，确定作用域在类中"""

test.set_def()  # 通过实例方法调用私有方法


# 1.2静态方法实例
class Calculator(object):
    """计算器类"""

    def __init__(self):
        # 定义2个默认值
        self.num1 = 0
        self.num2 = 0

    @staticmethod
    def show_menu():
        """因为打印菜单功能方法并不需要self指向的对象，所以就考虑使用静态方法"""
        print("    双双牌计算机 V2022.10")
        print("1. 加法")
        print("2. 减法")
        print("3. 乘法")
        print("4. 除法")
        print("5. 退出")

    def get_nums(self):
        self.num1 = int(input("请输入第1个数:"))
        self.num2 = int(input("请输入第2个数:"))

    def add(self):
        print(self.num1 + self.num2)

    def min(self):
        print(self.num1 - self.num2)

    def mul(self):
        print(self.num1 * self.num2)

    def div(self):
        print(self.num1 / self.num2)

    def run(self):
        while True:
            self.show_menu()
            op = input("请输入要进行的操作:")
            if op == "1":
                self.get_nums()
                self.add()
            elif op == "2":
                self.get_nums()
                self.min()
            elif op == "3":
                self.get_nums()
                self.mul()
            elif op == "4":
                self.get_nums()
                self.div()
            elif op == "5":
                break


# 创建一个计算器对象
cal = Calculator()
# 调用计算器的运行方法
cal.run()


# 2.1类属性
class Test:
    # 类属性
    nums = [1, 2, 3]

    def __init__(self):
        self.nums = [1, 2, 3, 4]

    def print_nums_1(self):
        print(self.nums)  # 如果在类中声明类属性与实例属性并且同名，则实例方法访问的是实例属性
        print(Test.nums)  # 实例方法中用类对象.类属性调用


#  @classmethod


test = Test()
test.print_nums_1()


# 2.2修改类属性
class Tool(object):
    tools_num = 0  # 定义一个类属性，用来存储共享的数据

    def __init__(self, name):
        self.name = name
        Tool.tools_num += 1  # 通过类对象调用类属性进行修改

    def print_info(self):
        print("工具的总数为：", Tool.tools_num)

    @staticmethod
    def print_info2():
        print("工具的总数为：", Tool.tools_num)


tieqiao = Tool("铁锹")
chutou = Tool("锄头")
dianciluo = Tool("电磁炉")

print("工具的总数为：", Tool.tools_num)  # 可以直接通过 类名.类属性操作
tieqiao.print_info()  # 可以通过Tool创建的任意实例对象调用方法，在方法中获取
Tool.print_info2()  # 通过类名调用非绑定方法

# 3.1类对象
"""类对象的作用

我们知道实例对象是类 （即类对象）创建出来的，所以类对象对于实例对象而言是共享的，既然是共享的那么就干脆将实例对象都有的而且不变化的内容存储到 类对象 即可，这样会减少内容的占用

那，哪些东西在类对象中存储呢？

- 类属性
- 所有的方法

对你没有看错，除了熟知的类属性之外，类对象中存储了class定义的所有的方法（无论是魔法方法、实例方法、静态方法 、类方法都在类对象中存储），因为方法(即函数)的代码是不变的，变化的仅仅是数据而已。
"""
print("-"*20)


# 4.1 如何调用实例对象
class Student:
    school = "西南交通大学"

    def student_name(self, name):
        self.name = name
        print(self)         # 打印的就是实例对象      ,                  <__main__.Student object at 0x00000185CE9DB7C0>，，0x开头是该实例对象的地址
        return f"学生{self.name}就读于{Student.school}"


stu_1 = Student()
print(stu_1.student_name("朱文峻"))
print(id(Student))                   # 类对象八进制数地址                 1674208161392
print(stu_1)                         # 打印实例对象，与print(self)对应    <__main__.Student object at 0x00000185CE9DB7C0>
print(id(stu_1))                     # 实例对象八进制地址                 1674208720832   与十六进制0x00000185CE9DB7C0对应
print(stu_1.student_name)            # 打印实例方法引用                   <bound method Student.student_name of <__main__.Student object at 0x00000185CE9DB7C0>>
print(id(stu_1.student_name))        # 实例方法八进制地址                 1674208779712，与实例对象的地址有所不同

print("-"*20)


#5.1 Python中一切皆对象，统一了类和类型的概念
class Foo:
    def find(self):
        self.str="你是大傻逼"
        print("我是绑定对象的方法")


foo1=Foo()
foo1.find()
print(type(foo1.str))
print(str)                           #str本质上也是一个类
name="朱文峻"                         #name是str类的实例对象
print(name.replace("文峻","勇"))      #name实例对象打点调用类str类中的存储的replace方法

#type可以查看哪个对象是哪个类生成的
#type可以查看哪个变量是什么数据类型

print("-"*20)

#5.2 面试题讲解
class Parent:
    x = 1


class Child1(Parent):
    pass


class Child2(Parent):
    pass


print(Parent.x, Child1.x, Child2.x)
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
Child1.x = 3
print(Parent.x, Child1.x, Child2.x)   #child2实例对象没有.x属性，要到父类里面找，改变Parent.x会影响未重写的子类属性