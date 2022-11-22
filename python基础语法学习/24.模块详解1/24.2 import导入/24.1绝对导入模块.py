"""模块有二种来源:1. 自定义模块 py文件，2. 内置的模块。
 1 使用python编写的.py文件
  python文件就是一系列功能的集合体
"""
# 1.import导入模块，拿到模块文件下的变量名，类名，对象名
money=200
#重复导入没有意义
import spam


print(spam.money)
print(spam.read1)
spam.read1()
a1= spam.A()
print(a1.a)
print(spam.a2)

print("1."+"-"*20)


# 2. from...import 可以跨文件夹导入,一定要设置来源文件夹！！
# 2.1 from 模块名 import 内容名
# from spam2 import money
# print(money)

#2.2
print(money)  #输出200
from  spam2 import money,read1,a2
print(a2)
print(money)
#缺点是会覆盖当前文件中全局同名变量

#2.3
from spam2 import  *    #将所有内容导入
print(a2)
print(money)

#2.4起别名
from spam2 import money as M
print(M)      #money=150
print(money)  #输出当前文件的同名全局变量 money=200

#2.5 from 文件夹 import 模块名
#绝对导入
from dir import m1
m1.f1()
m1.f2()

# 2.6 from 文件夹.模块 import 内容
from dir.m1 import f3
f3()

print("2."+'-'*20)


