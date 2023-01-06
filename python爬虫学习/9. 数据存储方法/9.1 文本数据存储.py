import requests
from bs4 import BeautifulSoup

url = 'https://www.zhihu.com/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
html = requests.get(url,headers = headers).text
soup = BeautifulSoup(html,'lxml')
