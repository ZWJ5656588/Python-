import requests
import pymysql
import json

class Baidu(object):
    def __init__(self):
        # 创建Mysql游标
        self.db = pymysql.connect(host = 'localhost',user = 'root',password='',db = 'spider' )
        self.cursor = self.db.cursor()
        # 获取资源地址
        self.url = 'https://talent.baidu.com/httservice/getPostListNew'
        self.headers={
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "71",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Host": "talent.baidu.com",
        "Origin": "https://talent.baidu.com",
        "Pragma": "no-cache",
        "Referer": "https://talent.baidu.com/jobs/list?search=python",
        "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Microsoft Edge\";v=\"108\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76"
    }

    # Post表单数据
    def post_data(self,page):
        data = {
            'recruitType': 'GRADUATE',
            'pageSize':'10',
            'keyWord':'C + +',
            'curPage':f'{page}',  # 页数
            'projectType':''
        }
        response = requests.post(self.url,data,headers = self.headers)
        return response.json()

    #解析数据并且调用存储数据方法
    def analyze_data(self,response):
        datat_list = response['data']['list']
        for node in datat_list:
            name = node['name']
            serviceCondition =node['serviceCondition']
            education = node['education']
            workPlace = node['workPlace']
            self.save_data(education,serviceCondition,name,workPlace)
            print(name)

    # 创建表
    def create_table(self):
        sql = """
        create table baidu(
    id int primary key auto_increment not null,
    education varchar(255) not null,
    name varchar(255) not null,
    serviceCondition varchar(255),
    workPlace varchar(255) not null
    )
     """
        try:
            self.cursor.execute(sql)
            print('Create table success')
        except Exception as e:
            print(f'Create table failed,case{e}')

    # 存储数据
    def save_data(self,education,serviceCondition,name,workPlace):
        # 插入的sql语法
        sql ='insert into baidu(id,education,name,serviceCondition,workPlace) values ("%d","%s","%s","%s","%s")' % (0,education,name,serviceCondition,workPlace)
        try:
            self.cursor.execute(sql)
            print('数据插入成功')
            self.db.commit()
        except Exception as e:
            print(f'数据插入失败，case{e}')
            # 发生错误 回滚
            self.db.rollback()

    # 主函数入口
    def main(self):
        # 先创建表
        self.create_table()
        # 循环获取并且插入
        for i in range(1,11):
            # 获取第i页的数据并接受 接收返回过来的json数据
            response = self.post_data(i)
            # 处理json数据 并且直接传递给数据存储方法进行数据库写入
            self.analyze_data(response)


        self.db.close()

if __name__ == '__main__':
    baidu = Baidu()
    baidu.main()









if __name__ == '__main__':
    baidu = Baidu()
    baidu.main()