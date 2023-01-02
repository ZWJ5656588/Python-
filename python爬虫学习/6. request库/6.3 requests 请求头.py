import requests

url = 'https://www.baidu.com/'
# 请求头以键值对的形式 保证爬取下来的数据的完整性
headers={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}

# 我们在使用百度搜索的时候经常发现url地址中会有一?，那么该问号后边的就是请求参数，又叫做查询字符串
response=requests.get(url,headers=headers)
print(response.text)

print('-'*20)

# 查看用户代理的请求头
print(response.request.headers)