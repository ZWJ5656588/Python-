import time
import multiprocessing

nums=[11,22,33]

# 一个进程里面至少有一个进程在执行代码，进程实际上就是先把资源全部复制，执行要执行的部分（target传入的函数地址)
# 进程与进程间互不影响，不共享全局变量
# 进程相对于线程消耗资源！，代码全部copy，每一个空间互不干涉

def test_1():
    nums.append(44)
    print('子进程1的全局变量的值为：',nums)
    time.sleep(2)
    print("子进程1结束")


def test_2():
    print('在子进程2中的全局变量的值为:',nums)  #各子进程打印的列表都是各自复制的，独有的，互不干扰的


def main():
    p_1=multiprocessing.Process(target=test_1)
    p_2=multiprocessing.Process(target=test_2)

    p_1.start()
    #p_1.join()
    p_2.start()
    p_1.join()

    nums.append(55)
    print(nums)


if __name__ == '__main__':
    main()

# 当前创建了三个进程，每个进程独立占用了三个空间。列表有三份，内存资源占用较多
# 如果要实现进程与进程之间的数据交换，该如何实现？ —————— 答案 队列！