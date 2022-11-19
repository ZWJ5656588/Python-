import socket

def get_file(file_name):  # 读出要传输的文件内容并
    try:
        with open(file_name,'rb') as f:        # 要发送的是二进制的文件，所以用rb模式打开,不能指定encoding
            content=f.read()
            return content
    except:
        print(f'没有下载的文件:{file_name}')


#创建主函数
def main():
    # 创建一个tcp套接字
    tcp_sever_socket1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 绑定信息，本地调试，回环地址
    address=('127.0.0.1',9999)
    tcp_sever_socket1.bind(address)

    # 改为被动监听状态
    tcp_sever_socket1.listen(128)     #最多可以创建128个套接字

    # 服务器一般不能关闭，使用死循环、
    while True:
        # 返回新的套接字，用来绑定客户端，一个客户端对应一个新的套接字
        new_socket,client_address=tcp_sever_socket1.accept()   # 等待客户端连入，阻塞

        # 数据接收 客户端发送文件名称，服务器根据文件名称查找
        # 如果文件存在 通过文件对象进行读写
        # 如果不存在 报错
        recv_data=new_socket.recv(1024)  # 如果接受电影等大文件，则需要循环接收！1024B只能接受文件
        file_name=recv_data.decode()
        print(f'当前客户端{client_address}请求下载的文件为{file_name}')
        #文件读写部分做拆分
        file_content=get_file(file_name)

        # 发送文件数据给客户端 当前发送的数据是二进制格式
        if file_content:
            new_socket.send(file_content)  # file_content是二进制，无需再次编码

        # 关闭客户端产生的套接字,不影响循环
        new_socket.close()


if __name__ =="__main__":
    main()