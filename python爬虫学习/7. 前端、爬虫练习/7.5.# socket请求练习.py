import socket
import re

url1 ='https://pic.netbian.com/uploads/allimg/220211/004115-1644511275bc26.jpg '

client = socket.socket()

client.connect(('pic.netbian.com',80))

http_req = 'GET' + ' ' + url1 + ' HTTP/1.0\r\nHost:pic.netbian.com\r\nuser-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54\r\n\r\n'

client.send(http_req.encode())

result = b''
data = client.recv(1024)

while data:
    result += data
    data = client.recv(1024)
print(result)

