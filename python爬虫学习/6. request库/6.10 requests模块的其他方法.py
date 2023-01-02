import requests
from retrying import retry

# 1. cookiejar的处理方法
'''1. response.cookies是CookieJar类型
2. 使用requests.utils.dict_from_cookiejar，能够实现把cookiejar对象转化为字典
'''

url = "http://www.baidu.com"
#发送请求，获取resposne
response = requests.get(url)
print(type(response.cookies))

#使用方法从cookiejar中提取数据
cookies = requests.utils.dict_from_cookiejar(response.cookies)
print(cookies)

print("-"*20)



# 2. request证书错误处理

url1 = 'https://175.178.218.98'
try:
    response = requests.get(url1)
except Exception as e:
    print(e)

# 为了在代码中能够正常的请求，我们修改添加一个参数 verify = Flase 忽略SSL证书
response1 = requests.get(url1,verify=False)
print(response1.text)
# 打印出byte类型的响应体
with open('6.11博客爬取.html', 'wb') as f:
    f.write(response1.content)


# 3. 设置延迟参数