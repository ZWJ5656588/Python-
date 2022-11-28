import sys
import os


print("-----------------------")
# 拿到当前文件的执行路径(不包括文件名)
print(os.path.dirname(__file__))
# 拿到当前文件完整的执行路径(包括文件名)
print(__file__)
print(os.path.abspath(__file__))
# 拿到文件所在目录的绝对路径
print(os.getcwd())

# 上一级的目录
Source_path=os.path.dirname(os.path.dirname(__file__))
# shopingcartAAA目录添加到解释器
print(Source_path)

sys.path.append(Source_path)
print(sys.path)

# __main__
# 打印执行文件
# print(__name__)

print("-"*40)

from core import src
# 以start.py作为执行文件才可以运行下面的代码，if main 后面的代码拒绝被导出

if __name__ == '__main__':
    src.run()




