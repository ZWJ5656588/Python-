import  socket

# 1.1 创建套接字
tcp_sever_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 1.2 绑定本地信息
address=('',6666)
tcp_sever_socket.bind(address)

# 1.3 改变状态为服务器状态 listen()方法
#最大可以支持128个客户端连接
# listen()不是阻塞代码！！！
tcp_sever_socket.listen(128)   #最多可以创建128个套接字

#1.4 等待连接  accpet()方法
# accept是阻塞代码，只有客户端连接到了此服务器，才能解阻塞
#这个方法返回值是一个元组,元组中有两个元素
#第一个元素：新创建一个套接字:数据发送/数据接收，因为第一个创建的套接字是负责连接的
#第二个元素：客户端的ip和port
#直接对返回的元组进行拆包，连接套接字一个服务器只需要一个
new_socket,client_address=tcp_sever_socket.accept()

#1.5 接听对方打过来的电话
recv_message=new_socket.recv(1024)
print(recv_message.decode('gbk'))

#1.6 回电
new_socket.send('thankyou'.encode('gbk'))

# 1.7 关闭服务器
## 关闭为这个客户端服务的套接字，只要关闭了，就意味着为不能再为这个客户端服务了，如果还需要服务，只能再次重新连接
new_socket.close()

# 2. ！！！！！tpc协议的注意事项
'''1. tcp服务器一般情况下都需要绑定，否则客户端找不到这个服务器
2. tcp客户端一般不绑定，因为是主动链接服务器，所以只要确定好服务器的ip、port等信息就好，本地客户端可以随机
3. tcp服务器中通过listen可以将socket创建出来的主动套接字变为被动的，这是做tcp服务器时必须要做的
4. 当客户端需要链接服务器时，就需要使用connect进行链接，udp是不需要链接的而是直接发送，但是tcp必须先链接，只有链接成功才能通信
5. 当一个tcp客户端连接服务器时，服务器端会有1个新的套接字，这个套接字用来标记这个客户端，单独为这个客户端服务
6. listen后的套接字是被动套接字，用来接收新的客户端的链接请求的，而accept返回的新套接字是标记这个新客户端的
7. 关闭listen后的套接字意味着被动套接字关闭了，会导致新的客户端不能够链接服务器，但是之前已经链接成功的客户端正常通信。
8. 关闭accept返回的套接字意味着这个客户端已经服务完毕
9. 当客户端的套接字调用close后，服务器端会recv解堵塞，并且返回的长度为0，因此服务器可以通过返回数据的长度来区别客户端是否已经下线
'''
tcp_sever_socket.close()