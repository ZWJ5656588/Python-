from time import sleep,ctime
import threading


# 两个任务
def sing():
    for i in range(5):
        print('正在唱歌： ',i)
        sleep(1)


def dance():
    for i in range(5):
        print('正在跳舞：',i)


def main():   # 运行main的线程是主线程
    print(f'程序开始：{ctime()}')
    #创建两个线程对象
    t1=threading.Thread(target=sing)    # 主线程里定义两个子线程
    t2=threading.Thread(target=dance)

    t1.start()
    t2.start()

    # sleep(6)
    print(f'程序结束：{ctime()}')         # 如果主线程代码执行完毕，但子线程还在任务中，主线程会等待子线程任务执行完毕后退出程序！！


if __name__ == '__main__':
    main()


# python代码的本质是.py文件 py文件中没有函数时仍可以运行
# python的特点就是主线程等待子线程执行完毕后才会退出主线程！