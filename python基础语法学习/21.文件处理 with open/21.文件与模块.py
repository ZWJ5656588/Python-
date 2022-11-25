# 1.写入硬盘
"""# @Author : 大海
# @File : 2.文件操作.py
'''
1 什么是文件
    文件是操作系统为用户/应用到硬盘中
    内存程序提供的一种操作硬盘的抽象单位
2 为何要用文件
    用户/应用程序对文件的读写操作会由操作系统转换成具体的硬盘操作
    所以用户/应用程序可以通过简单的读\写文件来间接地控制复杂的硬盘的存取操作
    实现将内存中的数据永久保存
        user=input('>>>>: ') #user="大海"
3 如何用文件
    文件操作的基本步骤:
        f=open(...) #打开文件,拿到一个文件对象f,f就相当于一个遥控器,可以向操作系统发送指令 ,f是迭代器
        f.read() # 读写文件,向操作系统发送读写文件指令
        f.close() # 关闭文件,回收操作系统的资源
    上下文管理:
        with open(...) as f:
            pass
'''"""

# 2.1  绝对路径读取,windows默认编码集是gbk，Linux默认是utf-8
f=open(r"C:\Users\zwj\Desktop\Coputer Science Study\Python\Pycharm文件\pythonProject 源码\图灵学院\21.文件处理 with open\21.a.txt",encoding='utf-8')
print(f.name)  #访问实例属性name
f1=f.read()
print(f1)
f.close()

print("-"*20)


# 2.2 相对路径读取
f=open(r"21.a.txt",encoding="utf-8")
f2=f.read()
print(f2)
f.close()

print("-"*20)

with open(r"21.a.txt",mode="rt",encoding="gbk") as f:
    print(f.read())


# 2.3 rt只读文本的操作
'''
一 文件的打开模式
    r: 只读模式(默认的)
    w: 只写模式
    a: 只追加写模式
二 控制读写文件单位的方式(必须与r\w\a连用)
    t : 文本模式(默认的),一定要指定encoding参数
        优点: 操作系统会将硬盘中二进制数字解码成unicode然后返回
        强调: 只针对文本文件有效
    b: 二进制模式,一定不能指定encoding参数
        优点: 不用指定字符编码，视频，图片文件
'''
print("-"*20)
#2.3.1 rt只读
with open(r"21.a.txt",mode="rt",encoding="utf-8") as f:
    res1=f.read()
    print("1>>>>",res1)
    res2 = f.read()
    print("2>>>>", res2)
    print(f.writable())
    print(f.readable())

print("-"*20)

#2.3.2 一行一行读取
with open(r"21.a.txt", mode="rt", encoding="utf-8") as f:
    print(f.readline(),end="")  #一行一行读
    print(f.readline())  #一行一行读，print自带换行

print("-"*20)

#2.3.3 文件每一行添加到列表,readlines方法
l=[]
_f=open(r"C:\Users\zwj\Desktop\Coputer Science Study\Python\Pycharm文件\pythonProject 源码\图灵学院\21.文件处理 with open\21.a.txt",encoding="utf-8")
for line in _f:
    l.append(line)
print(l)
path=r"21.a.txt"
with open(path,'rt',encoding='utf-8') as f13:
    print(f13.readlines(1))   #取第一行，将\n也作为列表中的元素

print("-"*20)

#2.4 wt只写模式
# 1 当文件不存时,新建一个空文档(无则创建)
# with open('b.txt',mode='wt',encoding='utf-8')as f:
#     pass
# 2 当文件存在时,清空文件内容，文件指针跑到文件的开头（有则清空）
# with open('b.txt',mode='wt',encoding='utf-8')as f:

with open("21.b.text",mode='wt',encoding="utf-8") as f:
    f.write("大")
    f.write("大")
    f.write("大")
    f.write("大\n")
    f.write("大\n")
    f.write("大\n")
    f.write("大\n")
with open("21.b.text",mode='wt',encoding="utf-8") as f:   #清空上一次的写入
    f.write("xiao\n")
    f.write("xiao\n")
    f.write("xiao\n")
#一次性写入多行
    f.write("giao\ndd\n2466\n88sdd\ngiggigigigigi")
    f.write("tacotusedayggggggggggg")
#列表内容写入
    info=["\nxiaohai\n","1262\n","48799\n"]
    for element in info:
        f.write(element)



#2.5 at只追加模式
# 1 当文件不存时,新建一个空文档，文件指针跑到文件的末尾(开头就是末尾)
# with open('c.txt',mode='at',encoding='utf-8')as f:
#     pass
# 2 当文件存在时,文件指针跑到文件的末尾
# with open('c.txt',mode='at',encoding='utf-8')as f:
with open(r"21.c.text",mode="at",encoding="utf-8") as ff:
    ff.write("da\n")
    ff.write("da\n")
    ff.write("da\n")
    ff.write("da\n")
    ff.write("da\n")
    ff.write("xxxxxxx")



# w模式
# 在文件打开不关闭的情况下，连续的写入，
# 下一次写入一定是基于上一次写入指针的位置而继续的
# a模式关闭了下次打开是在文件末尾写，所以不会覆盖之前的内容


"""t模式只能对文本进行操作！！！！
b模式可以操作语音和视频等二进制文件！！！！"""


#2.6 b模式对图片或者视频的操作
with open("21.1.jpg",mode="rb") as jpg:
    data=jpg.read()
    print(type(data))  # bytes类型，二进制文件，不是视频就是图片


with open("21.2.jpg",mode="wb") as jpg:
    jpg.write(data)    #写入21.1.jpg的数据,相当于复制了一张图片


#2.7 b模式也可以进行对文本的操作，不过要进行编码或者解码
#encode 编码
#decode 解码
#解码   读的时候转换成字符
with open('21.rb模式.txt',mode='rb')as f:
     data = f.read()
     print(data)
     print(data.decode('utf-8'))

#编码  写的时候把字符转换成二进制写入
with open('21.wb模式.txt',mode='wb')as f:
    f.write('大海\n'.encode('utf-8'))
    f.write('大海\n'.encode('utf-8'))
    f.write('大海\n'.encode('utf-8'))


print("-"*20)

#3. 文件指针！！！

# 文件内指针移动,只有t模式下的read(n),n代表的字符的个数
# b模式文件内指针的移动都是以字节为单位
# t模式  read(n)字符的个数

with open('21.指针移动.txt',mode='rt',encoding='utf-8')as f:
    print(f.read(1),end="")
    print(f.read(1),end="")
    print(f.read(1),end="")
    print(f.read(2),end="")
    print(f.read(3),end="")
# b模式  read(n)# b模式文件内指针的移动都是以字节为单位

print("-"*20)

with open('21.指针移动.txt',mode='rb')as f:
    print(f.read(1).decode('utf-8'))
    print(f.read(1).decode('utf-8'))
    print(f.read(1).decode('utf-8'))
    # 三分之一个汉字，utf-8中硬盘里写入汉字需要3个字节
    print(f.read(3).decode('utf-8'))  #要对应文件中的汉字,read(3)读取一个汉子
    print(f.read(3).decode('utf-8'))
    print(f.read(3).decode('utf-8'))

print("-"*20)

# 3.4 seek指针

# f.seek(offset,whence)有两个参数:
# offset: 代表控制指针移动的  有方向
# whence: 代表参照什么位置进行移动字节数
#        whence = 0: 参照文件开头(默认的),特殊,可以在t和b模式下使用
#        whence = 1: 参照当前所在的位置,必须在b模式下用
#        whence = 2: 参照文件末尾,必须在b模式下用
# t模式 移动的字节数算 读的按照字符算

with open('21.seek指针.txt',mode='rt',encoding='utf-8')as f:
    f.seek(3,0)          #写指针时offsest是按照字节数计算
    print(f.read(1))     #t模式读取时按照字符读取
    print(f.read(1))


# b模式 移动的字节数 读的也是字节数
# with open('seek.txt',mode='rb')as f:
#     f.seek(2,0)
#     print(f.read(3).decode('utf-8'))
print("-"*20)
#        whence = 1: 参照当前所在的位置,必须在b模式下用

with open('21.seek指针.txt',mode='rb')as f:
    msg = f.read(6)
    print(msg.decode('utf-8'))
    # 查看到当前指针的位置
    print(f.tell())
    # 当前指针的位置 还移动了3个字节
    f.seek(3,1)
    print(f.read(3).decode('utf-8'))
    f.seek(-3,2)
    print(f.tell())
    print(f.read(3).decode('utf-8'))

#        whence = 2: 参照文件末尾,必须在b模式下用
# with open('seek.txt',mode='rb')as f:
#     f.seek(0,2)
#     print(f.tell())
#     f.seek(-3,2)
#     print(f.read(3).decode('utf-8'))

