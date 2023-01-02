import requests

#equests 提供了一个叫做session类，来实现客户端和服务端的会话保持

# 会话保持有两个内涵：
#
# - 保存cookie，下一次请求会带上前一次的cookie
# - 实现和服务端的长连接，加快请求速度

url = ' http://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice'
session = requests.session()

# session实例在请求了一个网站后，对方服务器设置在本地的cookie会保存在session中，下一次再使用session请求对方服务器的时候，会带上前一次的cookie

response = session.get(url)

print(response.cookies)

print('-'*20)

url1 = 'http://www.cninfo.com.cn/new/disclosure'
res = session.get(url1)
print(res.request.headers)
