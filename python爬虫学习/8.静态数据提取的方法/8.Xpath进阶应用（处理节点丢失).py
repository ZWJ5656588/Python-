import requests
from lxml import etree


# 1. 标签分组方法  先分组 再单个提取


# 获取到url地址
url = 'https://www.qqtxt.cc/xuanhuan/'
# 伪装请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
# 发送请求
response = requests.get(url, headers=headers)
response.encoding = 'gbk'
res = response.text
# 转换字符串数据类型为element对象数据
html = etree.HTML(res)

# 获取li标签信息 标签内属性内容不一致不影响整体标签的获取 避免zip匹配出错
li_list = html.xpath('//*[@id="newscontent"]/div[1]/ul/li')
# 打印信息
# print(li_list)
for li in li_list:
    # print(li)
    # 变量li是Element对象 继续使用Xpath方法
    # './其余标签(属性)'表示从当前标签开始往后查找
    title_test = li.xpath('./span[1]/a/text()')[0]  # 如果标签属性为空,xpath返回空列表 则[0]抛出错误 避免下一步匹配出错
    href_test = li.xpath('./span[1]/a/@href')[0]    # 取出列表中的元素
    print(title_test,':',href_test)

print('-'*50)

for li in li_list:
    # 用三元运算处理
    href_test1= li.xpath('./span[1]/a/@href')[0]
    title_test1 = li.xpath('./a/text()')[0]  if li.xpath('./a/text()') else None
    print(title_test1,href_test1)