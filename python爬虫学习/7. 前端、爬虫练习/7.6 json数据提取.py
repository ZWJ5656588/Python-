import requests

url_list= ['https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=detail&logid=8448492901266749772&cl=&lm=&ie=utf-8&oe=utf-8&adpicid=0&lpn=0&st=&word=%E5%9F%8E%E5%B8%82%E5%BB%BA%E7%AD%91%E6%91%84%E5%BD%B1%E4%B8%93%E9%A2%98&z=2&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=albumsdetail&simics=&srctype=&bdtype=&rpstart=&rpnum=&cs=2529476510%2C3041785782&catename=&nojc=&album_id=7&album_tab=%E5%BB%BA%E7%AD%91&cardserver=&tabname=&pn=0&rn=30&gsm=&1673056278228=', # 第一页
           'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=detail&logid=8448492901266749772&cl=&lm=&ie=utf-8&oe=utf-8&adpicid=0&lpn=0&st=&word=%E5%9F%8E%E5%B8%82%E5%BB%BA%E7%AD%91%E6%91%84%E5%BD%B1%E4%B8%93%E9%A2%98&z=2&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&simics=&srctype=&bdtype=&rpstart=&rpnum=&cs=2529476510%2C3041785782&catename=&nojc=&album_id=7&album_tab=%E5%BB%BA%E7%AD%91&cardserver=&tabname=&pn=30&rn=30&gsm=0&1673056420558=', # 第二页
            'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=detail&logid=8448492901266749772&cl=&lm=&ie=utf-8&oe=utf-8&adpicid=0&lpn=0&st=&word=%E5%9F%8E%E5%B8%82%E5%BB%BA%E7%AD%91%E6%91%84%E5%BD%B1%E4%B8%93%E9%A2%98&z=2&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&simics=&srctype=&bdtype=&rpstart=&rpnum=&cs=2529476510%2C3041785782&catename=&nojc=&album_id=7&album_tab=%E5%BB%BA%E7%AD%91&cardserver=&tabname=&pn=60&rn=30&gsm=0&1673056423061=' # 第三页
]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'Host': 'image.baidu.com'
}


for page in range (0,3):
    print(f'第{page+1}页')
    res = requests.get(url_list[page],headers = headers).json()['data']
    for index,i in enumerate(res):
         if i:
            print(str(index),':',i['thumbURL'])
            result = requests.get(i['thumbURL']).content
            with open(f'7.6 爬取图片存储/{index+30*page}.png','wb') as f:
                f.write(result)


