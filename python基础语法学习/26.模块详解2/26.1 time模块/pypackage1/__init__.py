# 在__init__文件中进行相对导入
from .m1 import f1  #相对导入

f1()

from pypackage1.m2 import f2  #绝对导入

f2()