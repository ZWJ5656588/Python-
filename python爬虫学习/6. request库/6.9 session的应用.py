# 动手尝试使用session来获取到巨潮资讯首页请求返回的cookie，在访问巨潮资讯的动态接口页面

# 1. 准备url地址和请求参数
# 2. 构造session发送get请求
# 3. 使用session访问动态接口数据，看看是否请求成功

import requests

url = 'http://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice'
# 获取到url地址
url1 = 'http://www.cninfo.com.cn/new/disclosure'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
    'Connection': 'keep-alive',
    'Host': 'www.cninfo.com.cn'


}
session = requests.session()
response = session.get(url, headers=headers)
# 观察第一次请求的返回的cookie信息

print(response.content.decode('utf-8'))
print('-'*30)
print(response.cookies)



res = session.get(url1, headers=headers)
print('-'*30)

# 观察第二次请求携带的cookie信息
print(res.request.headers['Cookie'])
