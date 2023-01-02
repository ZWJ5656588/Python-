import requests
import json

# 获取网址
url = 'https://www.baidu.com/'

# 发送请求
response = requests.get(url)

# 打印相应的数据
print(response.content.decode('utf-8'))   # 解码
# response 常用属性
print(response.text) # 获取响应体中的类型 str类型 获取的文本用text
# response.text有自动解码功能，但会出现识别错误 可以通过 response.encoding = 'utf-8'指定
print(response.content.decode('utf-8')) # 获取响应体中的内容，bytes数据类型 数据流 需要解码获取数据 content也可以获取文本 但要进行解码
# print(response.json()) # 获取响应体中的内容 获取的是字典数据类型
print(response.status_code) # 获取相应的状态码
print(response.request.headers) # 获取请求头,默认的请求头 到时候要换 不能明摆着去请求
print(response.headers) # 获取响应头 键值对
print(response.cookies) # 获取cookies表单