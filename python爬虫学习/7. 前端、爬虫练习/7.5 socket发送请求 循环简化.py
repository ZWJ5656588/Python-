import socket
import re

# 获取资源地址
dic_url = {
    'url1':'https://pic.netbian.com/uploads/allimg/220211/004115-1644511275bc26.jpg',
    'url2':'https://pic.netbian.com/uploads/allimg/220215/233510-16449393101c46.jpg',
    'url3':'https://pic.netbian.com/uploads/allimg/211120/005250-1637340770807b.jpg'
}
http_list = []
# 构造套接字对象
client = socket.socket()  # 默认tcp协议

# 创建连接
client.connect(('pic.netbian.com',80))

# 构造http请求 https协议有的会开放80端口 不需要SSL证书   Host(ip,端口号)必须要加
for value in dic_url.values():
        http_req = 'GET'+' ' + value + ' HTTP/1.0\r\nHost:pic.netbian.com\r\nupgrade-insecure-requests: 1\r\nuser-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54\r\n\r\n'
        http_list.append(http_req)


# 爬取其他图片时改掉http_list[]的索引即可
http_content = http_list[2]
client.send(http_content.encode())

# 创建一个二进制变量接收数据结果
result = b''
data = client.recv(1024)

# 循环接收数据
while data:
    result += data
    data = client.recv(1024)
print(result)

# 保存响应体中的数据
images = re.findall(b'\r\n\r\n(.*)',result,(re.S))[0]


# # 写入文件
with open(f"7.5.{http_list.index(http_content)+1}.jpg",mode='wb') as f:
    f.write(images)
