import requests

url_list=[
'https://t7.baidu.com/it/u=1595072465,3644073269&fm=193&f=GIF',
'https://t7.baidu.com/it/u=1819248061,230866778&fm=193&f=GIF',
'https://t7.baidu.com/it/u=2168645659,3174029352&fm=193&f=GIF',
]
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'Host':'t7.baidu.com'

}
for i in url_list:
    response = requests.get(i,headers = headers)
    res_data = response.content
    with open('7.6.{}.jpg'.format(url_list.index(i)+1),'wb') as f:
        f.write(res_data)
