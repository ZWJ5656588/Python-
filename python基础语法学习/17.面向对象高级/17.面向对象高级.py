"""如果用函数进行开发，全局变量在内存中只有一份
    用实例属性开发，每个实例对象会开辟相应的实例属性，且互不干扰"""


# 1.1 多态的回顾
class MiniOS:
    """MiniOS操作系统类"""

    def __init__(self, name):
        self.name = name
        self.apps = []  # 将个软件的软件名传入列表中

    def __str__(self):
        return "%s 安装的软件列表为 %s" % (self.name, str(self.apps))  # 列表转换为字符串

    def install_app(self, app):  # 我们要传实例对象到qpp形参中，课直接使用app.调用传入实例对象的属性
        # 判断是否已经安装软件
        if app.name in self.apps:
            print(f"已经安装了{app.name},无需再次安装")
        else:
            app.install()
            self.apps.append(app.name)


class App(object):
    def __init__(self, name, version, desc):
        self.name = name
        self.version = version
        self.desc = desc

    def __str__(self):
        return f"{self.name}当前的版本是{self.version}-{self.desc}"

    def install(self):
        print(f"将{self.name}[{self.version}的执行程序复制到程序目录。。。]")


class Pycharm(App):
    pass


class Chrome(App):
    def install(self):  # 方法重写
        print("正在解压压缩陈程序")
        super().install()  # z这个super（）括号内省略了 Chrome,self，python2.0中写成super(Chrome,self)
        #App.install()


linux = MiniOS("Linux")
print(linux.apps)  # 空列表
# 实例化子类
pycharm = Pycharm("Pycharm", "1.0", desc="Python开发的IDE环境")
chrome = Chrome("Chrome", "2.0", "谷歌浏览器")
# 调用install方法
linux.install_app(pycharm)  # 对象关联

linux.install_app(chrome)
linux.install_app(chrome)
print(linux.apps)

print("-" * 20)


# 2.1静态方法与类方法 （加装饰器）
# 静态方法在类中没有实例对象参数，没有类对象参数，只有普通形参
class Foo:
    def __init__(self, name):
        self.name = name

    def old_fuc(self):
        print("实例方法")

    @classmethod
    def class_func(cls):
        print("类方法")

    @staticmethod
    def old_fuc():
        print("静态方法")


f = Foo("中国")
# 实例方法与静态方法同名，则调用静态方法
f.old_fuc()
f.class_func()
Foo.class_func()
print("-" * 20)


# 3.多继承以及MRO


# 4.内建属性
# 4.1  查看内建属性 dir
class Test:
    name = "zwj"

    def __init__(self, *args):
        print(args)
        self.name, self.address = args  # *args把传过来的两个元素放在元组里面，args就是一个元组

    def info(self):
        print(f"{self.name},{self.address}")


test = Test("朱文峻", "成都")
test.info()
print(dir(test))  # dir(实例对象)包含所有方法，所有属性
print(dir(Test))  # dir(类对象)包含类方法、实例方法、静态方法，类属性 但没有实例属性

# 4.2 new方法，生成实力所需要的属性
"""帮助类在内存中开辟一个空间，可以将几个实例对象的内存放在一个内存里面
    __new__控制内存的数量，单例模式会用到
    
    第一次创建实例对象时，占用一个内存空间
    第二次创建实例对象是，将上一次的引用进行重新赋值"""


# 4.3 class方法
class Person:
    def info(self):
        return None


p = Person()
print(p.__class__.info(p))  # p>Person>info,通过__class__方法
print(p.__class__)  # 输出实例对象关联的类的引用


# 4.4 repr方法
class Test:
    def __repr__(self):
        return "1"


test = Test()
print(test)
print("-" * 20)


# 4.5.1 getattribute
# 属性拦截器
class Tuling:
    def __init__(self, sub):
        self.sub1 = sub
        self.sub2 = "java"

    def __getattribute__(self, item):  # item以字符串形式获取传入属性的名称
        if item == "sub1":  # sub1属性的字符串
            print("现在访问的是sub1属性")
            return "C++"  # 重新返回该属性对应的值
        else:
            return object.__getattribute__(self, item)


t = Tuling("Python")
print(t.sub1)

# 获取sub2的值
print(t.sub2)
print("-" * 20)


# 4.5.2 属性拦截器getattribute的注意事项
class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattribute__(self, item):  # 调用某个属性时，这个item会拿到属性的名称
        print(item)
        return object.__getattribute__(self, item)  # 属性的获取机理就是传到object类调用__getattribute__方法
        # return self.name #无线递归,报错,所以不能在getattribute中返回实例属性self


test = Test("安娜", 20)
print(test.name)
print(test.age)

print("-" * 20)


# 5.1 __doc__，表述类的描述信息
class Foo:
    """描述类信息"""

    def func(self):
        pass


print(Foo.__doc__)  # 输出类的描述信息
print("-" * 20)

# 6.1 __module__和__class__
"""module表示当前操作的对象在哪个模块"""
"""class表示当前操作的对象类是什么"""

# 7.1__call__方法 又称回调函数
"""可以把一个类当函数使用"""


class Foo:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print("如果对类实例化添加了括号，则会执行__call__方法")


Foo()()
foo = Foo()
foo()


# 8.1 __dict__方法
class Province:
    country = "中国"  # 类属性

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def func(self, *args, **kwargs):
        print("这是一个方法")


# 获取类的属性
print(Province.__dict__)

# 获取实例对象的属性
p = Province("成都", "666")
print(p.__dict__)  # 通过实例对象.__dict__只能获取到实例属性的键值对
print("-" * 20)


# 9.1
class Foo1:
    def __getitem__(self, item):
        print("__getitem__被调用", item)

    def __setitem__(self, key, value):
        print("__setitem__被调用", key, value)

    def __delitem__(self, key):
        print("__delitem__被调用", key)


foo = Foo1()

# 在当前这个实例对象中创建一个字典key
res = foo["name"]  # foo["name"]，自动调用_getitem__(self, item):
print(res)
foo["name"] = "安娜"  # foo["name"]="安娜"，调用__setitem__(self, key, value):
# ，这些值都会存在于self实例对象中
del foo["name"]  # del关键字，自动触发删除字典的__delitem__(self,key):方法


# 10.1动态绑定!!!
# 10.1.1动态绑定属性
"""Python解释器进行一行一行翻译时，可以在翻译的过程中进行代码修改"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("安娜", 18)
p.gender = "女"  # 动态绑定一个实例属性
print(p.gender)

p_2 = Person("双双", 18)
# print(p_2.gender)  ，报错，，，实例对象p和实例对象p_2在不同的两个地址存储，给实例对象p动态绑定一个属性不会影响p_2
# 可以创建一个类属性，进行对象共享
Person.gender = None
print(p_2.gender)
Person.gender = "未知"  # 通过类属性进行修改
print(p_2.gender)

print("-" * 20)

# 10.1.2 动态绑定方法
import types  # 导入包


# 定义了一个类
class Person(object):
    num = 0

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def eat(self):
        print("---默认的实例方法---")


# 在类外定义方法
# 定义一个实例方法
def run(self, speed):
    print("----实例方法--1--")
    print("%s在移动, 速度是 %d km/h" % (self.name, speed))
    print("----实例方法--2--")


# 定义一个类方法
@classmethod
def test_class(cls):
    print("----类方法--1--")
    print("num=%d" % cls.num)
    cls.num = 100
    print("num=%d" % cls.num)
    print("----类方法--2--")


# 定义一个静态方法
@staticmethod
def test_static():
    print("----静态方法--1--")
    print("---static method----")
    print("----静态方法--2--")


# 创建一个实例对象
p = Person("安娜", 18)
# 调用在class中的方法
p.eat()

# 给这个对象添加实例方法
p.run = types.MethodType(run, p)  # p.run看做一个属性，括号内填入方法名的引用和要绑定到的实例对象
# 调用实例方法
p.run(180)

# 给Person类绑定类方法
Person.test_class = test_class

# 调用类方法
Person.test_class()
print("\n换种方式调用\n")
p.test_class()
print("\n")

# 给Person类绑定静态方法
Person.test_static = test_static  # 千万不要加括号，只有调用方法的时候才加括号
# 调用静态方法
Person.test_static()
print("\n换种方式调用\n")
p.test_static()
print("-" * 20)


# 11.1property属性,把实例方法转为实例属性调用
class Page:
    def __init__(self, current_age):
        self.current_age = current_age
        # 每页显示的数据条数
        self.per_items = 10


    def start(self):  # 被@property修饰的方法不能传递除实例对象本身的额外参数
        # 1
        val = (self.current_age - 1) * self.per_items
        return val

    @property
    def end(self):
        val = self.current_age * self.per_items
        return val


p = Page(2)  # 第二个页面是第十到第二十的数据
print(p.start())
print(p.end)
print("-" * 20)

# 11.2 @property属性
"""@property装饰器下定义一个方法名method
@method.setter,添加或修改属性
@method.deltet，删除属性"""

class Goods:
    def __init__(self):
        self.price = 100

    # 获取价格
    @property
    def _price(self):
        return self.price

    # 设置价格
    @_price.setter
    def _price(self, value):           #方法名与@property定义的一致
        self.price = value
        return self.price

    # 删除价格
    @_price.deleter
    def _price(self):                 #方法名与@property定义的一致
        del self.price


goods = Goods()
print(goods.price)

# 正确修改proprerty修饰下的属性
goods._price = 200  #python解释器遇到这种键值对，在@property下自动调用@方法名+setter的方法
print(goods._price)

#错误修改方proprerty修饰下的属性



"""property方法中有个四个参数

- 第一个参数是方法名，调用 对象.属性 时自动触发执行方法
- 第二个参数是方法名，调用 对象.属性 ＝ XXX 时自动触发执行方法
- 第三个参数是方法名，调用 del 对象.属性 时自动触发执行方法
- 第四个参数是字符串，调用 对象.属性.__doc__ ，此参数是该属性的描述信息
"""

print("-"*20)

# 11.3类属性的方式调用property
class Foo(object):
    def get_bar(self):
        print("getter...")
        return 'a...'

    def set_bar(self, value):
        """必须两个参数"""
        print("setter:", value)
        return 'set value' + value

    def del_bar(self):
        print("deleter...")
        return 'b...'

    BAR = property(get_bar, set_bar, del_bar, "description...")
    #类属性使用需要考虑参数位置,BAR指向property方法的应用地址


obj = Foo()

obj.BAR  # 自动调用第一个参数中定义的方法：get_bar
obj.BAR = "c"  # 自动调用第二个参数中定义的方法：set_bar方法，并将“c”当作参数传入
desc = Foo.BAR.__doc__  # 自动获取第四个参数中设置的值：description...,  (类对象.property类属性名.__doc__)
print(desc)
del obj.BAR  # 自动调用第三个参数中定义的方法：del_bar方法

print("-"*20)


# 11.4利用property方法改进 getter和 setter方法
class Money(object):
    def __init__(self):
        self.__money=0

    def get_money(self):
        return  self.__money

    def set_money(self,value):
        if isinstance(value,int):
            self.__money=value
        else:
            print("erro:value不是整形数字")


money=Money()
print(money.get_money())
money.set_money(100000000)
print(money.get_money())
money.set_money(1522.055)
print(money.get_money())

print('-'*20)

"""property类属性升级"""
class Money:
    def __init__(self):
        self.__money=0

    def get_money(self):
        return self.__money

    def set_money(self,value):
        if isinstance(value,int):
            self.__money=value
        else:
            print("传入的值不是一个整数")

    # 类属性操作
    money=property(get_money,set_money,"这是对金额的操作")


m=Money()
print(m.money)
m.money=200
print(m.money)

print("----------------------")

"""property装饰器升级"""
class Money:
    def __init__(self):
        self.__money=0.0

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self,value):
        if isinstance(value,float):
            self.__money=value
        else:
            print("value值不是浮点类型")


# 修改私有属性较为方便
m=Money()
print(m.money)
m.money=50.0
print(m.money)
m.money=50
print(m.money)

