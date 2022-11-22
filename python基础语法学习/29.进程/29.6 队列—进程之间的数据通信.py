# 队列和栈 ———数据结构

# 队列:只允许在一端进行插入数据的操作，在另一端进行数据操作的特殊线性列表，队列具有先进先出FIFO(first in first onu)

# 导入multiprocessing模块下的Quenue类
import multiprocessing
from multiprocessing import *

'''模拟一个爬虫场景，当前通过一个进程进行网站的数据抓取
一个进程负责网站的数据抓取
另外一个进程负责数据读写'''

# 1. 创建一个队列对象最，
# 掌握 get put empty full 方法！

q1=Queue(3)   #Quene是一个类

# 将数据放入到队列中

q1.put('hello world')

q1.put([11,22,33])

def test():
    pass

q1.put(test)

#q1.put(1)   q1.put()方法当超出队列最大长度时，会堵塞

# q1.put_nowait(5)  q1.put_nowait()方法超出

# print(q1.get())
# print(q1.get())




def dowload_from_web(q):
    '''模拟抓取下来的数据'''
    data=[1,2,3,4]

    # 向队列写入数据
    for temp in data:
        q.put(temp)

    print('数据上传队列成功')


def get_data(q):
    queue_data=list()
    # 从队列中获取数据
    while True:
        data=q.get()   #Queue.get([block[, timeout]])：获取队列中的一条消息，然后将其从列队中移除，block默认值为True 先进先出
        # get()方法运行一次获取一个值，此处循环取值
        queue_data.append(data)
        if q.empty():    # Queue.empty()：如果队列为空，返回True，反之False ；
            break

    # 模拟数据处理
    print(queue_data)


def main():
    q=Queue()

    p_1=Process(target=dowload_from_web,args=(q,))
    p_2=Process(target=get_data,args=(q,))

    p_1.start()
    p_2.start()


if __name__ == '__main__':
    main()
