import  os
"""1.认识os模块
os表示操作系统相关的一个模块
os模块是与操作系统交互的一个接口
它可以围绕文件和目录进行操作"""
#1.    目录的获取 创建 删除
print(os.getcwd())
# 生成目录
# os.mkdir('dirname1')

# 空目录，若目录不为空则无法删除
# os.rmdir('dirname1')

# 拿到当前脚本工作的目录，相当于cd
# os.chdir('dirname1')

# # # # 删除文件
# os.remove('aaaa.py')   对文件删除remove，对目录删除用rmdir
# os.rmdir('dirname1')   也就是说，先用remove删除目录下的文件，删完文件后才能用rmdir删除目录

# 可生成多层递归目录
# os.makedirs('dir1/dir2/dir3/dir4')

# 在dir2下面创建一个文件，会产生保护机制只删除到dir2，因为dir目录下有文件，没有使用remove删除，所以形成对目录的保护
# os.removedirs('dir1/dir2/dir3/dir4')

# 拿到当前文件夹目录下的文件名或者目录名放入列表！！！
# 绝对路径
print(os.listdir(r'C:\Users\zwj\Desktop\Coputer Science Study\Python\Pycharm文件\pythonProject 源码\图灵学院\24.模块详解1\24.4 os模块'))
#相对路径
print(os.listdir('..'))  # 访问到了运行的文件上一级别目录，返回上一级别目录下的所有文件或者目录！！

# 重命名文件/目录
# os.rename('oldname','newname')

# 运行终端命令 了解
# os.system('tasklist')  #查看系统任务进程

print('1'+'-'*20)

#2. os路径相关操作
# os.path 下面的方法 path是路径
# 将path分割成目录和文件名二元组返回
print(os.path.split('/a/b/c/d.txt'))
# # 文件夹
print(os.path.split('/a/b/c/d.txt')[0])
# # 文件
print(os.path.split('/a/b/c/d.txt')[1])
#返回path的目录。其实就是os.path.split(path)的第一个元素
print(os.path.dirname('/a/b/c/d.txt'))
# # 返回path最后的文件名。即os.path.split(path)的第二个元素
print(os.path.basename('/a/b/c/d.txt'))
# 判断路径是否存在 文件和文件夹都可以 如果path存在，返回True；如果path不存在，返回False
print(os.path.exists(r'C:\Users\zwj\Desktop\Coputer Science Study\Python\Pycharm文件\pythonProject 源码\图灵学院\3.数据类型实例应用'))
print(os.path.exists(r'C:\Users\zwj\Desktop\Coputer Science Study\Python\Pycharm文件\pythonProject 源码\图灵学院\24.模块\24.3 json模块序列化与反序列化\24.3json模块.py'))
print(os.path.exists(r'D:\python代码A8\day11模块\2.time_test.py'))
print(os.path.exists(r'D:\python代码A8\day11模块\2.timedddd_test.py'))
# 如果path是一个存在的文件，返回True。否则返回False
print(os.path.isfile('C:\\Users\zwj\Desktop\Coputer Science Study\Python\Pycharm文件\pythonProject 源码\图灵学院\8.国庆作业.py'))
print(os.path.isfile(r'D:\python代码A8\day11模块\2.time_test.py'))
# 也可以用相对路径
print(os.path.isfile(r'./4.hash.py'))
print(os.path.isfile(r'../day11模块/4.hash.py'))
# 如果path是一个存在的目录，则返回True。否则返回False
print(os.path.isdir('D:\python代码A8\day11模块'))
print(os.path.isdir(r'D:\python代码A8\day11模块\2.time_test.py'))
# 拼接一个绝对路径，会忽略前面的路径
print(os.path.join('a','b','c','D:\\','f','d.txt'))
print(os.path.join('D:\\','f','d.txt'))

print('2'+'-'*20)