import re
res = re.match('b','apple')
# print(res.group())
# 如果没有匹配成功 res = None 则不能再使用.group()方法


res1 = re.match('.','sadas58')
print(res1.group())








#  匹配 163 126 qq邮箱  (不能排出汉字)
res_1 = re.match(".*163\.com|.*126\.com|.*qq\.com",'hello@163.com')
if res_1:
    print(res_1.group())