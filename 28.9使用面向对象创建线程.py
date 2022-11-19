from  time import sleep #导入的是sleep方法
import threading


# def sing():
#     for i in range(5):
#         print('正在唱歌: ',i)
#         sleep(1)

#
# def dance():
#     for i in range(5):
#         print('正在跳舞',i)
#         sleep(1)
#

class Sing(threading.Thread):  # 继承threading文件中的Thread类
    # 当前类没有写构造函数父类T
    # 如果这个类中需要写实例属性，那么在重写__init__方法时，需要运行继承的threading.Thread中的__init__方法
    # 否则就相当于覆盖掉了父类Thread的__init__
    def __init__(self,name,):
        super().__init__()

    def sing(self):
        for i in range(5):
            print('正在唱歌: ', i)
            sleep(1)
    # 重写一个run方法
    # target获取到的函数引用传递给run方法，run方法负责运行任务的一个方法
    # start()-->方法与run()方法解耦合
    # 通过start()找到run方法，并调用run()方法，相当于普通用户并不能直接调用run()方法
    # 这里重写了run方法，就不需要用target
    def run(self):
        self.sing()


class Dance(threading.Thread):
    def dance(self):
        for i in range(5):
            print('正在跳舞', i)
            sleep(1)

    def run(self):
        self.dance()


if __name__ == '__main__':
    s=Sing('zwj')
    d=Dance()

    s.start()
    d.start()
