import requests

# 1. 获取资源地址
url = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'


# 响应本身就是一个图片,没有响应头 不需要提取数据 并且是二进制类型
# gets是请请求类型
response = requests.get(url)

print(response.content)

# 以二进制+写入的方式打开文件
with open('baidu.png', 'wb') as f:
    # 写入response.content bytes二进制类型
    f.write(response.content)