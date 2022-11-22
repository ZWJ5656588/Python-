import socket
import threading

# 让服务器完成多个请求的应答

class Message(threading.Thread):
    '''消息控制类'''
    def __init__ (self,new_socket,client_info):  #new_socket应是一个套接字实例对象
        super(Message, self).__init__()
        self.new_socket=new_socket
        self.client_info=client_info

    def run(self):
        # 接收/发送数据
        while True:
            recv_content=self.new_socket.recv(1024)
            #判断消息是否为空
            if len(recv_content)!=0:
                print(f'{self.client_info}:{recv_content}')
                self.new_socket.send(recv_content)
            else:
                #消息为空则关闭套接字
                self.new_socket.close()
                break

    def __del__(self):   # 只关闭套接字 ,指向的引用删完才会调用__del__方法
        self.new_socket.close()


class TCPServer(threading.Thread):
    '''TCP套接字创建类'''
    def __init__(self,port):
        # 调用父类thread的初始化方法
        # super().__init__()
        threading.Thread.__init__(self)

        # 创建套接字
        self.sever_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        # 绑定本地信息
        self.sever_socket.bind(('127.0.0.1',port))  # 端口号由参数传入,以元组形式

        # 将套接字由默认的主动连接模式改为被动监听模式
        self.sever_socket.listen(128)

    def run(self):
        # 等待客户端连接
        while True:
            new_socket,client_info=self.sever_socket.accept()
            # 连接上客户端，解堵塞
            print(f'客户端已连接:{client_info}')
            Message(new_socket,client_info).run()  # 实例对象调用父类thread类中的run()方法

    def __del__(self):
        # 关闭套接字
        self.sever_socket.close()


def main():
    print('TCP服务器已启动...')
    tcp_sever=TCPServer(port=8888)
    tcp_sever.run()


if __name__ == '__main__':
    main()




