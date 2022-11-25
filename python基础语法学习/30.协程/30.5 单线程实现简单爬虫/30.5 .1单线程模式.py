'''协程以最小的损耗加快程序运行速度，因为协程仅在单线程中运行'''
import requests  # 同步爬虫库
import os
import  time

os_path=os.getcwd()
print(os_path)

# 1. 单线程模式实现
def download_image(url):
    print("开始下载",url)
    response=requests.get(url)   # 必须等待第一章图片完成写入你才能访问第二个链接
    print("下载完成")

    # 保存图片
    file_name=str(url).rsplit('/')[-1]
    # 以字符串结尾位置开始计数，默认切分最大次数，[-1]取切完列表最后一个元素
    with open (os_path+'\\'+file_name,'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    start_time=time.time()
    url_list=[
        'http://pic.bizhi360.com/bbpic/98/10798.jpg',
        'http://pic.bizhi360.com/bbpic/92/10792.jpg',
        'http://pic.bizhi360.com/bbpic/86/10386.jpg'
    ]
    for item in url_list:
        download_image(item)
    end_time = time.time()
    print(f'耗时{end_time - start_time}')

