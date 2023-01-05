import re

import requests
from bs4 import BeautifulSoup

# bs4 包可以用到CSS的选择器对数据进行采集 操作简单但是效率低
url = 'http://ip.yqie.com/ipproxy.htm'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'

# 创建BeautifulSoup对象 指定解析器XML
soup = BeautifulSoup(response.text, 'lxml')
# print(soup)

# bf4格式化输出
# print(soup.prettify())
# print('\n\n')

# 1. find_all数据提取 返回列表
# 1.1 find_all 传字符串
print('1.1')
span = soup.find_all('span')
print(span,'\n')
a = soup.find_all('a')
print(a)
print('\n1.2')

# 1.2 find_all 传正则
data = soup.find_all(re.compile('^b'))
print(data)

print('\n1.3')

# 1.3 find_all传列表
data = soup.find_all(['a', 'span'])  # 标签字符串放在列表中，定位列表中的全部标签
print(data)

print('\n1.4')

# 1.4 find_all keyword参数
# 搜索所以class为....的结果
data2 = soup.find_all(attrs={'class': "blue_no_underline"})
print(data2)

print('\n\n2.1')

# 2.类似CSS选择器的select()方法 select()方法是选择
# 2.1 标签选择器
title = soup.select('title')
print(title)

print(soup.select('a'))

print(soup.select('span'))
