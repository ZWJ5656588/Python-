import  json
import requests
from lxml import etree

# 任务 获取4399小游戏中游戏名称和游戏相应的链接

headers = {
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    "Sec-Fetch-Dest": "image",
    "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-User": "?1",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
    "Referer": "https://www.4399.com/flash/",
    "Intervention": "^<https://www.chromestatus.com/feature/5718547946799104^>; level=^\\^warning^^",
    "authority": "cnzz.mmstat.com",
    "pragma": "no-cache",
    "cache-control": "no-cache",
    "sec-fetch-dest": "image",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    "intervention": "^<https://www.chromestatus.com/feature/5718547946799104^>; level=^\\^warning^^",
    "accept": "image/webp,image/apng,image/*,*/*;q=0.8",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "no-cors",
    "referer": "https://www.4399.com/flash/",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
    "cookie": "cna=IEpqGm1y4WECAXAc+xIbsbJ7; sca=285b7eef; atpsidas=3377f9eb435d2c0a95191c63_1668555937_1; atpsida=5018c3f7a1da83ddcaa40722_1673143035_1"
}
cookies = {
    "_4399stats_vid": "16731430356793930",
    "UM_distinctid": "1858f18a980b46-0963154a1d726-5313f6f-144000-1858f18a981975",
    "Hm_lvt_334aca66d28b3b338a76075366b2b9e8": "1673143036",
    "Hm_lpvt_334aca66d28b3b338a76075366b2b9e8": "1673143101"
}

data_list = []  # 准备储存到json数组

def get_data_from_4399(_url,page):
    response = requests.get(_url, headers=headers, cookies=cookies)
    response.encoding = 'gbk'
    # print(response.text)
    # print(response)

    # 创建Element对象
    html = etree.HTML(response.text)

    #取出对应的标签信息 此时仍为Element对象
    a_list = html.xpath('//ul[@class="n-game cf"]/li/a')

    #转化为数据信息
    for a in a_list:
        item = {}
        item['href'] = 'https://www.4399.com'+a.xpath('./@href')[0]
        item['game'] = a.xpath('./b/text()')[0]
        print(item)
        data_list.append(item)

    with open(f'9.2.1 4399game_data/第{page}页游戏数据.json', 'w', encoding='utf-8') as  f:
        json.dump(data_list,f,ensure_ascii=False,indent=2)


# 循环存储10页 封装成函数调用
url1='https://www.4399.com/flash/'
get_data_from_4399(url1,1)
for i in range(2,11):
    url2 = f'https://www.4399.com/flash/new_{i}.htm'
    get_data_from_4399(url2,i)