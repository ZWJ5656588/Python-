import threading
from time import sleep, ctime


def sing():
    for i in range(3):
        print(f'正在唱歌: {i}')
        sleep(1)

def dance():
    for i in range(3):
        print(f'正在跳舞: {i}')
        sleep(1)

if __name__ == "__main__":
    print(f'程序开始: {ctime()}')
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()

    print(f'程序结束：{ctime()}')



    while True:
        length = len(threading.enumerate())
        print(f'当前线程数量: {length}')
        if length <= 1:
            break
        sleep(0.5)