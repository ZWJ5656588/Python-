import csv
import requests

class Bilibili():
    def __init__(self,page):
        self.url = "https://api.bilibili.com/x/web-interface/wbi/search/type"
        self.headers = {
        'cookie': "",
        'origin': 'https://search.bilibili.com',
        'referer': 'https://search.bilibili.com/video?keyword=%E7%BE%8E%E5%A5%B3&from_source=webtop_search&spm_id_from=333.1007&search_source=5&page=2&o=36',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
        }
        self.params = {
            "__refresh__": "true",
            "_extra": "",
            "context": "",
            "page": page,
            "page_size": "42",
            "from_source": "",
            "from_spmid": "333.337",
            "platform": "pc",
            "highlight": "1",
            "single_column": "0",
            "keyword": "美女",
            "qv_id": "INfNHP4ImVTcEOEWOOIEhcCJJsw6PUgC",
            "ad_resource": "5654",
            "source_tag": "3",
            "category_id": "",
            "search_type": "video",
            "dynamic_offset": "0",
            "w_rid": "c87217358e5ca845e964b464af6c5bc0",
            "wts": "1673195296"
        }
        self.page = page

    def get_data(self):
        result = requests.get(self.url,headers = self.headers,params = self.params).json()
        self.save_data(result)

    def save_data(self,result):
        with open('9.4.1 b站爬取.csv', 'a', encoding='utf-8', newline='')as f:
            fieldnames = ['author', 'arcurl', 'tag']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if self.page == 1:
                writer.writeheader()
            for res in result['data']['result']:
                item = {}
                item['author'] = res['author']
                item['arcurl'] = res['arcurl']
                item['tag'] = res['tag']
                writer.writerow(item)

    def main(self):
        self.get_data()

# 循环创建对象进行调用
if __name__ == '__main__':
    for i in range(1,11):
        bizhan = Bilibili(i)
        bizhan.main()
