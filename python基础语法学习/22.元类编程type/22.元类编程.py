#1.
class ObjectCreate:
    pass


#1.1打印对象
def print_obj(obj):
    print(obj)


print_obj(ObjectCreate)

#1.2.判断当前对象中是否存在某种属性
print(hasattr(ObjectCreate,'new_attribute'))

#1.3动态创建一个类属性
ObjectCreate.new_attribute='这是一个类属性'
print(hasattr(ObjectCreate,'new_attribute'))

#1.4将类对象赋值给另一个变量
class_obj=ObjectCreate
print(class_obj)
print(class_obj())


#2.使用函数动态创建类
def choose_class(name):
    if name=='foo':
        class Foo:
            pass
        return Foo
    else:
        class Bar:
            pass
        return Bar


my_class=choose_class('foo')
print(my_class)

my_class=choose_class("bar")
print(my_class)


#3. type创建类
B=type('B',(),{'name':'zwj'})     #第二个参数是继承的父类
print(help((B)))

print("-"*20)


#3.1  调用类属性
Foo=type('Foo',(),{'name':'anna'})  #字典创建类属性

print(Foo.name)


#3.2 type继承
class Father:
    address="成都"

Son=type('Son',(Father,),{'name':"双双"})  #()是一个元组

print(Son)
print(Son.name)
print(Son.address)

print("-"*20)

#3.3 使用type创建一个带有方法的类
#创建父类
Father_1=type('Father',(),{'father_name':'zwj'})

#定义构造方法
def __init__ (self,address):
    self.address=address
    print(f"我在{self.address}")

#定义方法
def print_info(self):
    print('这是一个动态添加的实例方法，通过实例方法打印类属性:',self.father_name)  #子类的方法调用父类类属性

#定义子类
Son=type('Son',(Father_1,),{'__init__':__init__,'print_info':print_info})

#判断子类中是否存在指定的属性/方法
print('Son',hasattr(Son,'print_info'))

son=Son("成都")
son.print_info()

print("-"*20)


#3.4
def __init__(self):
    self.name="zwj"

def obj_self(self):
    print("这是一个实例方法",self.name)

@classmethod
def obj_class(cls):
    print("这是一个类方法")

@staticmethod
def obj_static():
    print("这是一个静态方法")


Father=type(
    'Father',
    (),
    {
        'address':"长沙",
        "__init__":__init__,
        "obj_self":obj_self,
        "obj_class":obj_class,
        "obj_static":obj_static
    }
)


father=Father()
father.obj_class()
Father.obj_class()

print("-"*20)


# 4. 重要的__metaclass__属性，自定义元类
# -*- coding:utf-8 -*-

class UpperAttrMetaClass(type):
    """
    __new__ 是在__init__之前被调用的特殊方法
    __new__是用来创建对象并返回值的方法
    而__init__只是用来将传入的参数初始化给对象
    你很少用到__new__，除非你希望能够控制对象的创建：例如单例模式
    这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
    如果你希望的话，你也可以在__init__中做些事情
    还有一些高级的用法会涉及到改写__call__特殊方法，但是我们这里不用
    """
    def __new__(cls, class_name, class_parents, class_attr):
        # 遍历属性字典，把不是__开头的属性名字变为大写
        new_attr = {}
        for name, value in class_attr.items():
            if not name.startswith("__"):
                new_attr[name.upper()] = value

        # 方法1：通过'type'来做类对象的创建
        return type(class_name, class_parents, new_attr)  # 如果__new__不返回任何实例，则__init__不会被调用

        # 方法2：复用type.__new__方法
        # 这就是基本的OOP编程，没什么魔法
        # return type.__new__(cls, class_name, class_parents, new_attr)


# python3的用法   __metaclass__可以重写type来创建类，作用域是整个模块都有效
class Foo(object, metaclass=UpperAttrMetaClass):
    # 约束类UpperAttrMetaClass地址给到metaclass,__metaclass__会运行UpperAttrMetaClass
    bar = '我是一个类属性'


# python2的用法
# class Foo(object):
#     __metaclass__ = UpperA  ttrMetaClass
#     bar = '我是一个类属性'


print(hasattr(Foo, 'bar'))
# 输出: False
print(hasattr(Foo, 'BAR'))
# 输出:True

f = Foo()
print(Foo.BAR)

# 输出:'我是一个类属性'


print("-"*20)

# 5.
def upper_attr(class_name, class_parents, class_attr):
    # 遍历属性字典，把不是__开头的属性名字变为大写
    new_attr = {}
    for name, value in class_attr.items():
        if not name.startswith("__"):
            new_attr[name.upper()] = value

    # 调用type来创建一个类
    return type(class_name, class_parents, new_attr)


class Foo(object, metaclass=upper_attr):
    bar = '我是一个类属性'


print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))

f = Foo()
print(f.BAR)


