'''TCP 与 UDP 的区别
- 面向连接（确认有创建三方交握，连接已创建才作传输。）
- 有序数据传输
- 重发丢失的数据包
- 舍弃重复的数据包
- 无差错的数据传输
- 阻塞/流量控制
'''

import socket


# 1.写一个简单地TCP协议的客户端
# 1.1 建立tcp套接字
tcp_client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #ipv4网络 tcp协议  socket.AF_INET中的soket是py文件
'''AF_INET相当于socket文件的常量'''

# 1.2 建立与服务器的连接，如果当前服务器没有启动，客户端不能运行
# 定义客户端连接ip与port
sever_ip=input('请输入服务器ip地址')
sever_port=int(input("请输入服务器端口:"))
#connect()方法与服务器建立连接,连接服务器的ip,端口号组成的元组。服务器accept()方法捕捉到即可解阻塞
tcp_client_socket.connect((sever_ip,sever_port))

# 1.3 发送信息
message=input('请输入你要发送的信息:')
# tcp协议发送数据的方法是send 而udp是sendto
tcp_client_socket.send(message.encode('gbk'))

# 1.4 数据接收
# tcp协议接收数据的方法是recv 而udp是recvfrom
recv_message=tcp_client_socket.recv(1024)   #接收到的信息是一个元组

# 1.5打印数据
print(recv_message.decode('utf-8'))

# 1.6 关闭套接字
tcp_client_socket.close()

