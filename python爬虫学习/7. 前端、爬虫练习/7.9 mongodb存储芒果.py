import requests
import pymongo


class MangGuoTV:
    def __init__(self):
        self.url = "https://pianku.api.mgtv.com/rider/list/pcweb/v3"
        self.client = pymongo.MongoClient(host= 'localhost',port = 27017)
        self.db = self.client['mydb']['mangguo']
        self.headers = {
                "accept": "application/json, text/plain, */*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
                "cache-control": "no-cache",
                "origin": "https://www.mgtv.com",
                "pragma": "no-cache",
                "referer": "https://www.mgtv.com/lib/2?lastp=list_index&lastp=ch_tv&kind=19&area=10&year=all&sort=c2&chargeInfo=a1&fpa=2912&fpos=",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-site",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
        }

    def get_data(self,page):
        params = {
            'allowedRC': '1',
            'platform': 'pcweb',
            'channelId': '2',
            'pn': str(page),  # 页面参数
            'pc': '80',
            'hudong': '1',
            '_support': '10000000',
            'kind': '19',
            'area': '10',
            'year': 'all',
            'chargeInfo': 'a1',
            'sort': 'c2'
        }
        response = requests.get(url = self.url,headers = self.headers,params = params).json()
        self.analyze_data(response)

    def analyze_data(self,response):
        res = response['data']['hitDocs']
        for item in res:
            data_list = {}
            data_list['title'] = item['title']
            data_list['updateInfo'] = item['updateInfo']
            data_list['story'] = item['story']
            self.save_data(data_list)

    def save_data(self,data_list):
       self.db.insert_one(data_list)

    def main(self):
        for page in range(1,11):
            self.get_data(page)
            print('insert successfully')



if __name__ == '__main__':
    mangguotv = MangGuoTV()
    mangguotv.main()