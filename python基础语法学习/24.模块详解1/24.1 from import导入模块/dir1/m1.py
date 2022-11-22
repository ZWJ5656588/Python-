from .m2 import f2  # 使用相对导入，从此文件夹的目录开始
#或者使用就绝对导入，寻找执行文件的目录，用from import下翻
from dir1 import m3


#给定的文件夹
#import m2 使用绝对导入时，从执行文件的目录下找，报错
#import spam 报错


def f1():
    print('from f1')
    f2()
    m3.f4()