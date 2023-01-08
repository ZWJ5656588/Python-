import requests
from bs4 import BeautifulSoup

url = 'https://www.zhihu.com/explore'

headers = {
'cookie': '',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS 10114) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'

}

html = requests.get(url, headers=headers).text

soup = BeautifulSoup(html, 'lxml')
title_list = soup.select('div .css-1g4zjtl a')
# print(title_list)
for title in title_list:
    print(title.get_text())
    with open('9.1.1 zhihu_explore_data.txt', 'a', encoding='utf-8')as f:
        f.write(title.get_text() + '\n')
        # 因为要达到for循环追加数据的效果 所以使用a方法 若没有\n 则一直追加数据在一行