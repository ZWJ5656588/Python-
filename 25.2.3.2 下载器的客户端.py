import socket


def main():
    tcp_client_socket2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 连接服务器
    sever_ip='127.0.0.1'
    sever_port=9999

    # ip在前，端口在后
    tcp_client_socket2.connect((sever_ip,sever_port))

    # 输入要下载的文件名
    file_name=input('请输入要下载的文件名: ')
    # 编码后把文件名发给服务端
    tcp_client_socket2.send(file_name.encode())

    # 接收服务器发送过来的文件数据
    recv_data=tcp_client_socket2.recv(1024)

    #判断文件是否有内容
    if recv_data:  # 文件没有内容,读None，走else
        # 在当前目录下新建一个文件，检验传入的文件是否正常
        with open('传入的新文件'+file_name,'wb') as f:
            f.write(recv_data)
    else:
        print('文件已损坏...')

    tcp_client_socket2.close()


if __name__=='__main__':
    main()