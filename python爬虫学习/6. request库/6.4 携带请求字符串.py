import  requests

# 通过字典的方式携带参数
url = 'https://www.baidu.com/s'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
}
# 通过字典携带参数
kw = {
    'wd':'python'
}
response=requests.get(url,params=kw,headers=header)
response.encoding = 'utf-8'
print(response.text)

# 在url地址中， 很多参数是没有用的，比如百度搜索的url地址，其中参数只有一个字段有用，其他的都可以删除
# 如何确定那些请求参数有用或者没用：挨个尝试！ 对应的,在后续的爬虫中，越到很多参数的url地址，都可以尝试删除参数