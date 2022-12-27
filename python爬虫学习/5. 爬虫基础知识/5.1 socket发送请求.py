import socket
import re

# 获取资源地址
url = 'http://image11.m1905.cn/uploadfile/2021/0922/thumb_0_647_500_20210922030733993182.jpg'

# 创建套接字对象,发送请求
client = socket.socket()

# 创建连接
client.connect(('image11.m1905.cn',80))
# 'image11.m1905.cn'通过dsn可转化为相应的ip地址 http协议的端口号是80

# 构造http请求
# 请求方法 熟记http请求方式图解  注意空格千千万不能丢 否则请求失败
http_req = 'GET' + ' '  + url + ' HTTP/1.0\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36\r\n\r\n'
client.send(http_req.encode())

# 创建一个二进制变量接收结果数据

result = b''
data = client.recv(1024)
#  循环接收数据
while data:
      result += data
      data = client.recv(1024)
# print(result)

# 保存响应体中的数据
images = re.findall(b'\r\n\r\n(.*)',result,re.S)[0]
print(images)

# 保存数据
with open('5.1.1小姐姐.jpg',mode='wb') as f:
      f.write(images)