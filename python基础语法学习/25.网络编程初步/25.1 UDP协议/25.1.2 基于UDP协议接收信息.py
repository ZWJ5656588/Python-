# 1.接收消息
import  socket

#1.1 创建udp套接字
udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#1.2 先发送再接收
dest_address=('192.168.236.129',8080)

#1.3 获取要发送的数据
send_data=input('请输入要发送的数据:')

#1.4 发送数据到指定ip指定port
"""sendto方法
第一个参数是发送的内容
第二个参数是接收端的ip和端口"""
udp_socket.sendto(send_data.encode('gbk'),dest_address)

#1.5 接收对方发送的数据
recv_data=udp_socket.recvfrom(1024)  #1024表示最大接收1KB

#1.6 显示对方发送的数据
"""接收到的数据recv_data是一个元组，
第一个参数是对方发送的数据
第二个参数是对方ip和端口
与sendto方法对应
 """
print(recv_data[0].decode('gbk'))    #decode解码
print(recv_data[1])

#1.7 关闭套接字
udp_socket.close()