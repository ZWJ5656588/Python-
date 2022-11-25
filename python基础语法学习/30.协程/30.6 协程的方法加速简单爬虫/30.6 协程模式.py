'''在一个线程中如果遇到了IO等待的时间，那么线程会充分利用这个等待时间去执行其他的任务。

案例：使用requests模块完成图片下载
'''
import asyncio
import os
import aiohttp  # 异步爬虫库
import time

os_path=os.getcwd()

async def download_image(session,url):
    print("发送请求：",url)
    async with session.get(url,verify_ssl=False) as response:
        content=await response.content.read()
        file_name=url.rsplit('/')[-1]
    async with open(os_path+'\\'+file_name,'wb') as f:
        # with 前加上async可以通过协程切换
            f.write(content)


async def main():
    async  with aiohttp.ClientSession() as session:
        url_list=[
            'http://pic.bizhi360.com/bbpic/98/10798.jpg',
            'http://pic.bizhi360.com/bbpic/92/10792.jpg',
            'http://pic.bizhi360.com/bbpic/86/10386.jpg'
        ]
        tasks=[asyncio.create_task(download_image(session,url=url))
              for url in url_list]
        await asyncio.wait(tasks)


if __name__ == '__main__':
    start_time=time.time()
    asyncio.run(main())
    end_time=time.time()
    print(f'耗时{end_time-start_time}')

# 写入的同时会运行访问其余图片链接的操作，线程不会等待，三个链接一起发送完成之后，把三个链接的数据
