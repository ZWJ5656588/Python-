import os
import time
import multiprocessing

def test():
    while True:
        print('子进程pid=%d,父进程的pid=%d' % (os.getpid(),os.getppid()))  # 使用os模块分别获取子进程和父进程号
        time.sleep(1)


def main():
    print('子进程 pid=%d,父进程pid=%d' % (os.getpid(),os.getppid()))
    p=multiprocessing.Process(target=test)
    p.start()


if __name__ == '__main__':
    main()