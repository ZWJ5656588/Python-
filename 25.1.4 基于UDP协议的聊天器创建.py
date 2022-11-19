"""使用函数封装功能"""
import socket



# 功能函数写在main主函数之前
def send_msg(udp_socket):   # 传入主函数创建的udp实例对象
    msg=input('请输入要发送的数据')
    dest_ip=input('请输入对方的ip地址')
    dest_port=int(input('请输入对方的端口号:'))
    udp_socket.sendto(msg.encode('gbk'),(dest_ip,dest_port))


def recv_msg(udp_socket):
    recv_data=udp_socket.recvfrom(1024)
    recv_ip=recv_data[1]
    recv_message=recv_data[0].decode('gbk')
    print(f'地址端口为{recv_ip}的电脑给您发来消息:{recv_message}')

# 1.主函数创建套接字，绑定端口，选择发送/接收服务
def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地信息
    udp_socket.bind(('', 8886))
    while True:
        # 选择功能
        print('='*30)
        print('1:发送消息')
        print('2:接收消息')
        print('exit:退出聊天器')
        op_num=input('请输入要操作的功能序号:')
        # 根据用户选择调用相应函数
        if op_num=='1':
            send_msg(udp_socket)
        elif op_num=='2':
            recv_msg(udp_socket)
        elif op_num=='exit':
            break
        else:
            print('输入有误，重新输入')




if __name__ == '__main__':
    main()

