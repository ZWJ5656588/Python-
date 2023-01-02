# cookie放在headers中

import requests

url = 'https://cplusplus.com/articles/y807M4Gy/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
    'Cookie':'__utmz=62705790.1666250015.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __gads=ID=78e2440d7078ccdb-22cd53c56cd700cd:T=1666250038:S=ALNI_MZT0ZZL8lexg_q79AmrAg3zXheC8g; _ga=GA1.1.1727020546.1666250113; __gpi=UID=00000b66ce9954fe:T=1666250038:RT=1668486413:S=ALNI_Mailp7hDH8Lwj8eN0P0G5Q9Ut4xDQ; tryBeta=1; _ga_7TV1TJ13CV=GS1.1.1668486414.4.1.1668486514.0.0.0; cto_bundle=_laCB18yajdmN1lVbWw2Y0hVJTJCV3VsOXhVYTYwTlk2N1BUQ3A0aVdIUDdKTHRQUE5JU0F4VDg2V1R4UjdHbEZHZTQ2bkJoYmg1UHZsWWNIRmthbVhFcFlIJTJGcm9saENjJTJGYlJ6bmolMkJ1T1VqSHhRWUYlMkY1MEYxbjQxR2JhSDJEV3c1aGQ1dWg5WXd2ODFrNGZJeFklMkZJajRHbTQzZEElM0QlM0Q; __utma=62705790.1283822501.1666250015.1671354413.1672360272.5; __utmc=62705790; __utmt=1; __utmb=62705790.6.10.1672360272'
}

response = requests.get(url,headers = headers)

print(response.text)

print('-'*20)

print(response.request.headers)

# cookie有过期时间 ，所以直接复制浏览器中的cookie可能意味着下一程序继续运行的时候需要替换代码中的cookie，
# 对应的我们也可以通过一个程序专门来获取cookie供其他程序使用；
# 当然也有很多网站的cookie过期时间很长，这种情况下，直接复制cookie来使用更加简单


# cookie当做参数传递
# cookie当做键值对参数传入get()/post()方法中