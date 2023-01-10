import requests
import pymysql
import json

class MangGuoTV:
    def __init__(self):
        self.url = "https://pianku.api.mgtv.com/rider/list/pcweb/v3"
        self.client = pymysql.connect(host = 'localhost',user = 'root',password ='', db='spider')
        self.cursor = self.client.cursor()
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

    def create_table(self):
        sql = """
        create table  mangguo(
            id int primary key auto_increment not null ,
            title varchar(255) not null ,
            updateinfo varchar(255) not null ,
            story varchar(1000) 
        );
        """
        # try语句检查创建表过程是否成功
        try:
            self.cursor.execute(sql)
            print('create table successfully')
        except Exception as e:
            print(f'erro as {e} ')
            self.client.rollback()

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
            title = item['title']
            updateInfo = item['updateInfo']
            story = item['story']
            self.save_data(title,updateInfo,story)

    def save_data(self,title,updateInfo,story):
        sql = """
        insert into mangguo (id, title, updateinfo, story) values (%s,%s,%s,%s)
        """
        try:
            # 变量以元组形式传入excute方法，%s可以替换任何文本 避免""带来的不便
            self.cursor.execute(sql,(0,title,updateInfo,story))
            print('insert data succcessfully')
            self.client.commit()
        except Exception as e:
            print(f'erro as {e}')
            self.client.rollback()

    def main(self):
        self.create_table()
        for page in range(1,11):
            self.get_data(page)
        self.client.close()

if __name__ == '__main__':
    mangguotv = MangGuoTV()
    mangguotv.main()