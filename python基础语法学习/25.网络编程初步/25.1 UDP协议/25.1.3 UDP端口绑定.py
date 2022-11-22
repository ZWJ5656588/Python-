"""一般情况下，在一台电脑上运行的网络程序有很多，
为了不与其他的网络程序占用同一个端口号，往往在编程中，udp的端口号一般不绑定。
但是如果需要做成一个服务器端的程序的话，是需要绑定的，
想想看这又是为什么呢？
如果报警电话每天都在变，想必世界就会乱了，所以一般服务性的程序，往往需要一个固定的端口号，这就是所谓的端口绑定
"""

import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定本地相关信息，如果一个网络进程不绑定，则系统随机分配
local_addr = ('', 6688)
# 表示ip地址和端口，ip一般不写

# 进行绑定
udp_socket.bind(local_addr)

recv_data = udp_socket.recvfrom(1024)
print(recv_data[0].decode('gbk'))

udp_socket.close()
