import requests
import pymongo

class Aqiyi:
    def __init__(self):
        # 连接mongo
        self.client = pymongo.MongoClient(host='127.0.0.1',port=27017)
        # 连接表
        self.collection = self.client['mydb']['aqiyi']
        # 请求资源
        self.headers ={

                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en,zh-CN;q=0.9,zh;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "content-type": "application/x-www-form-urlencoded",
                "cookie": "QC005=4d8c6ce67d7b72e231d6b2b060d0c002; QC175=%7B%22upd%22%3Atrue%2C%22ct%22%3A%22%22%7D; QC008=1673278402.1673278402.1673278402.1; QC007=DIRECT; Hm_lvt_53b7374a63c37483e5dd97d78d9bb36e=1673278403; QC189=5257_B%2C5465_B%2C5592_A%2C5468_B%2C5670_B; QC191=; QC006=qkp3yjv6e7uz95m61rcpqhh7; TQC030=1; QC186=false; nu=0; T00404=d6f65d5ecbecc4271956fab42f3027eb; QC173=0; QC187=true; websocket=true; Hm_lpvt_53b7374a63c37483e5dd97d78d9bb36e=1673278702; QC010=114290438; IMS=IggQABj_8_CdBiouCiA2YjZiODlkNWI0MTcwYzhjY2UxYTkyMTdkYjM4N2JjOBAAIggI0AUQAhiwCXIkCiA2YjZiODlkNWI0MTcwYzhjY2UxYTkyMTdkYjM4N2JjOBAAggEAigEkCiIKIDZiNmI4OWQ1YjQxNzBjOGNjZTFhOTIxN2RiMzg3YmM4; __dfp=a15803e9b0962e45ab9575cbe0aa12c202520bb5035190e6e392caf5fe6276a99e@1674574402791@1673278403791",
                "origin": "https://list.iqiyi.com",
                "referer": "https://list.iqiyi.com/www/2/15-------------11-1-1-iqiyi--.html?s_source=PCW_SC",
                "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Microsoft Edge\";v=\"108\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-site",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76"
            }
        # 用param方法
        self.url = "https://pcw-api.iqiyi.com/search/recommend/list"

    def main(self):
        for i in range(1,11):
            # 每一页的请求后缀不同
            params = {
                "channel_id": "2",
                "data_type": "1",
                "mode": "11",
                "page_id": f'{i}',
                "ret_num": "48",
                "session": "8f9d9816014bcc25df89492bfd2d093e",
                "three_category_id": "15;must"
            }
            self.get_data(params)

    def get_data(self,params):
        response = requests.get(self.url,headers = self.headers,params = params).json()
        self.analyze_data(response)

    def analyze_data(self,response):
        data_list = response['data']['list']
        for video in data_list:
            item = {}
            item['title'] = video['title']
            item['playUrl'] = video['playUrl']
            item['description'] = video['description']
            # 循环调用 save_data()函数 差诶mongo中
            self.save_data(item)
            # 以字典的形式保存 方便传入mongodb中

    def save_data(self,item):
        self.collection.insert_one(item)


if __name__ == '__main__':
    aqy = Aqiyi()
    aqy.main()
