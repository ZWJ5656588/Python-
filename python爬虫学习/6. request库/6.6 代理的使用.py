import requests
# ipconfig显示的是局域网的ip
# 本机ip

# 数据分类
# 公开数据   个人隐私数据   菜鸟驿站 收货地址  2w
# 非公开数据  no           违规

# - 正向代理：对于浏览器知道服务器的真实地址，例如VPN
# -  反向代理：浏览器不知道服务器的真实地址，例如nginx

# ip池可以起到反反爬虫的效果


proxies = {
    'http' : 'http://185.147.35.240:80'
}

url = "http://httpbin.org/ip"
response = requests.get(url,proxies=proxies)
print(response.text)