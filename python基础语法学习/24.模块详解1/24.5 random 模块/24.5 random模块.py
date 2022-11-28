# 1. random模块
import random
# 左闭右开
# 0 - 1 随机浮点 不包含1 random 0-1 闭开
#[0,1) 闭是包含 开是不包含,生成0到1之间的浮点数
print(random.random())
# randint 1 - 3 [1,3] 左闭右闭 整型
print(random.randint(1,3))
# randrange 1 - 3 [1,3) 左闭右开
print(random.randrange(1,3))
# 随机选⼀个
print(random.choice([1,4,3]))  #列表中选
# 随机选指定个数sample(列表，指定列表的个数)
print(random.sample([1,4,3],2))
# 打乱顺序shuffle(列表)
l = [1,2,3,4,5]
random.shuffle(l)
print(l)
# [1,2] 左闭右闭 浮点
print(random.uniform(1,2))

print('1'+'-'*20)

# 2 生产验证码函数，整型数字和字母结合
def make_code(i):
    res=''
    for i in range(i):
        n=str(random.randint(0,9)) #转化为字符串类型数字
        #65到90刚好是ASCII码表对应的大写字母，用chr方法转化为字母
        #chr()函数将数字转化为ASCII码，ord()方法将ASCII编码转化为十进制数字
        d=chr(random.randint(65,90))
        x=chr(random.randint(65,90)).lower()
        s = random.choice([n, d, x])
        res += s
    return res


print(make_code(6))  #六位验证码
