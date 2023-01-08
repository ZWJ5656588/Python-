import re
import requests

for i in range(1,11):
    url = f' https://www.qqtxt.cc/list/1_{i}.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
        'Host': 'www.qqtxt.cc'
    }
    res = requests.get(url,headers = headers)
    res.encoding = 'gbk'
    result = res.text
    ress = re.findall("<li><span class=\"s2\">《<a href=\".*\" target=\"_blank\">(.*)</a>》</span><span class=\"s3\">",result)
    print(f'第{i}页','\n',ress)
