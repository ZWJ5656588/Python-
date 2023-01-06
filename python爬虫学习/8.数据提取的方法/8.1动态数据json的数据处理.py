import requests

# json数据在xhr请求中的preview以类似于字典的形式存储
# 我们要将请求来的json动态数据拿出来

# 获取url
url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=9124930296321073629&ipn=rj&ct=201326592&is=&fp=result&fr=ala&word=%E5%9B%BE%E7%89%87&queryWord=%E5%9B%BE%E7%89%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&expermode=&nojc=&isAsync=&pn=60&rn=30&gsm=3c&1673016546169='

# 请求头
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
'Accept': 'text/plain, */*; q=0.01',
'Host': 'image.baidu.com'


}
#发送请求
response = requests.get(url,headers = headers).json()
for index,i in enumerate(response['data']):
    if i:
        thumbURL = i['thumbURL']
        print(thumbURL)
        res = requests.get(thumbURL).content
        with open('8.1 .1爬取图片存储/{}.png'.format(index),'wb') as f:
            f.write(res)


