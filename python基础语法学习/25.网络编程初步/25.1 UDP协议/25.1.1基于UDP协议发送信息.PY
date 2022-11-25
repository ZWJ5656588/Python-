#1. UDP网络编程  User Datagram Protocol
# 1.1 socket概念
"""socket(简称 套接字) 是进程间通信的一种方式，它与其他进程间通信的一个主要不同是：它能实现不同主机间的进程间通信，
我们网络上各种各样的服务大多都是基于socket来完成通信的。"""

# 1.2 socket标准库,UDP协议的使用
import socket
# 当前socket模块需要有两个参数，第一个参数是网络类型-ipv4,协议类型UDP
#socket本质是一个类，socket()产生了一个实例对象(套接字对象)

#1.2.1socket模块下的socket类，打点括号实例化，再传入参数
socket_udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#1.2.3使用当前套接字对象进行数据的收发
"""需要知道当前接收消息的一方地址和接收消息软件所占用的端口
在macOS中将信息传到Ubuntu上

Ubuntu
        ip 192.168.65.176
        port(端口) 8080"""

send_address=('192.168.25.36',8080)

#1.2.4 获取用户输入的信息
send_messeage=input('请输入要发送的信息:')

#1.2.5 将接受的信息发送到ubuntu上
#发送信息时一定要将字符串转化为字节形式，使用encode()的方法,windows系统方法内传入'gbk参数
socket_udp.sendto(send_messeage.encode('gbk'),send_address)  #传入写入的数据和接收地址

#1.2.4关闭套接字，释放端口
socket_udp.close()


# 2. 获取本机的ip地址
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(('8.8.8.8',80))
print(s.getsockname())



"""UDP协议
        速度快
        结构简单
        不安全------>不能保证数据准确送达另一台计算机
        网络直播，游戏，物联网一部分等会用到UDP"""



