# 相对导入
#         from .文件夹 import 模块
#         from ..文件夹 import 模块
#         from ...文件夹 import 模块

# 相对导入: 参照当前所在文件的文件夹为起始开始查找,称之为相对导入
#        符号: .代表当前所在文件夹的文件,..代表上一级文件夹,...代表上一级的上一级文件夹
#        优点: 导入更加简单
#        缺点: 只能在导入包中的模块时才能使用,不能在执行文件中用

# 1.相对导入应用
#from .dir1 import  m1  报错
#执行文件只能用绝对导入！！,相对导入是一种被动导入的方式
#C:\Users\zwj\Desktop\Coputer Science Study\Python\Pycharm文件\pythonProject 源码\图灵学院\24.模块\24.1 from import导入模块\dir1
from  dir1 import m1
m1.f1()
m1.f2() #f2方法已经导入到m1模块中

