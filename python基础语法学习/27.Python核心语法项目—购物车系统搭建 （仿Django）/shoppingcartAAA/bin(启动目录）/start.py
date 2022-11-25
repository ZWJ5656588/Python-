import sys
import os
# 拿到当前文件的执行路径/所在的绝对路径目录
print(os.path.dirname(__file__))
# 上一级的目录
Source_path=os.path.dirname(os.path.dirname(__file__))
print(Source_path)
