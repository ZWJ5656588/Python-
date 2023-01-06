import requests
from lxml import  etree



# 获取网页资源地址  查看网页源代码 查看页面数据动静态
for i in range(1,11):
    url = "https://www.qqtxt.cc/list/1_{}.html".format(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
    }
    response = requests.get(url, headers=headers)

    # 根据抓包工具中元素中charset中显示的编码类型
    response.encoding = 'gbk'
    # print(response.text)

    # 利用etree.HTML，将字符串转化为Element对象,Element对象具有xpath的方法,
    # 返回结果的列表，能够接受bytes类型的数据和str类型的数据

    html_data = etree.HTML(response.text)
    # print(html_data)  # <Element html at 0x2ad51cf1e40> 具有了xpath方法

    #  Element对象转换为字符串
    html_str = etree.tostring(html_data,encoding='utf-8',method='html').decode()
    # print(html_str)

    # 获取小说的标题和属性 Xpath返回值是列表
    title_list = html_data.xpath('//li/span[@class="s2"]/a[@target="_blank"]/text()')  #/text()要加 否则拿到的是Element对象
    href_list =html_data.xpath('//li/span[@class="s2"]/a/@href')
    # print(title_list,'\n')
    # print(href_list)
    # print('\n')
    #
    # 循环取值
    # 利用zip函数把两个列表对应的索引封装到一个元组中 以两列表中最小的长度截断
    # zip函数返回一个迭代器对象 可用for循环遍历
    # z = zip(href_list,title_list)
    # print(list(z))

    # 循环取出元素
    # href,title组成一个二元组，遍历的同时进行拆包

    print('第{}页'.format(i))
    for href,title in zip(href_list,title_list):
        item = {}
        item['href'] = href
        item['title'] = title
        print(item)
    print('\n')


# 假设在某种情况下，某个小说的href没有，那么会怎样呢？
#
# 数据的对应全部错了，这不是我们想要的，接下来通过2.3小节的学习来解决这个问题