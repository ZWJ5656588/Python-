# 1. 登录注册（ POST 比 GET 更安全）
# 2. 需要传输大文本内容的时候（ POST 请求对数据长度没有要求，get请求的长度限制 IE：对URL的最大限制为2083个字符，
# 若超出这个数字，提交按钮没有任何反应。Firefox：对Firefox浏览器URL的长度限制为：65536个字符。Safari：URL最大长度限制为80000个字符。Opera：URL最大长度限制为190000个字符。）
#
# 所以同样的，我们的爬虫也需要在这两个地方回去模拟浏览器发送post请求
import requests

# 获取目标的url地址
url = 'http://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice#szse'

# 发送请求

# post方法携带载荷中的表单数据 比get 方法多了一个data字典 data字典里面是请求体的内容
data = {
    'column': 'szse_latest',
    'pageNum': '3',   # 更改表单数据
    'pageSize': '30',
    'sortName': '',
    'sortType': '',
    'clusterFlag': 'true',
}
# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
}

# 请求体的数据 可能是表单数据 也有可能是载荷数据 载荷数据用json字典形式

# 静态数据可以在网页源代码直接看
# 动态数据发送了ajax或是xhr 需要我们在抓包工具的网络中通过 Fetch/XHR中查看标头查看
response = requests.post(url,headers=headers,data=data)
print(response.text)
