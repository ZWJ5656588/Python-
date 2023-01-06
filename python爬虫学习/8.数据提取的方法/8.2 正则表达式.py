import re
# 1. 单个匹配
res = re.match('b','apple')
# print(res.group())
# 如果没有匹配成功 res = None 则不能再使用.group()方法

# 1.1 '.'除了\n都能匹配
res1 = re.match('.','sadas58')
print(res1.group())

# 1.2 []使用
res2 = re.match('[hH123]','2Hello')
print(res2.group())
res3 = re.match('[A-Z0-9a-z]','jjsadawd246')
print(res3.group())

# 1.3 \s匹配空白 \d匹配数字 \w 匹配非特殊字符(汉字是非特殊字符)



# 2. 匹配多个字符
'''
- pattern.match（从头找一个）
- pattern.search（找一个）
- pattern.findall（找所有）返回一个列表，没有就是空列表re.findall("\d","tu1ling2") >> ["1","2"]
- pattern.sub（替换）
  - re.sub("\d","_","tu1ling2") >> ["tu_ling_"]
- re.compile（编译）
  - 返回一个模型P，具有和re一样的方法，但是传递的参数不同
  - 匹配模式需要传到compile中
'''

# 2. search的用法 匹配一个从头到尾寻找 找到第一个匹配项为止
rs = re.search('\d','说的你捏所看的5hh61')
print(rs.group())


# 3. findall 匹配全部数据 返回一个匹配结果的列表
# 如果匹配失败 返回一个空列表
# findall直接打印接收列表的变量 不使用group()方法
fi = re.findall('\d','小明考了100分')
print(fi)


# 4. sub替换数据
sub = re.sub('\d','2','小明考了58分')
print(sub)


# 5. 修饰符re.S
S = re.match('.','\n',re.S)
print(S.group())   # re.S扩展了'.'的匹配范围

print('-'*30)

# 6. 匹配多个字符
# 6.1 *的使用(0或无限多次)
res_1 = re.match('0*','0000')
print(res_1.group())
res_2 = re.match('0*','0100010')
# 遇到匹配失败的字符停止 因为最少是0次 所以匹配失败.group()也不会报错
print(res_2.group())

print('-'*30)

# 6.2 +的使用(1次或者无限次)
# res_3 = re.match('.+','')  报错 没有匹配成功
# print(res_3.group())

# 6.3 {m},{m,n}
# 需求：匹配8到20位的密码，可以是大小写，英文字母 数字
result = re.match('[a-zA-Z0-9_]{8,20}','zweewrewrwellsd_96')
print(result.group())

print('-'*30)

# 7. 开头^ 结尾$
# 7.1 数字开头数字结尾 中见随意
re_1 = re.match('^\d.*\d$','1asda_6un231')
print(re_1.group())

# 7.2 ^[] 和 [^]相反
re_2 = re.match('^[abcd].*',"anien666@")
print(re_2.group())
re_3 = re.match('[^abcd].*',"vnien666@")
print(re_3.group())

print('-'*30)


# 8. 匹配分组
# 8.1  匹配 163 126 qq邮箱  (
# '\.'转义 ！！！
res__1 = re.match(".*163\.com|.*126\.com|.*qq\.com",'hello@163.com')
if res_1:
    print(res__1.group())

# 8.2 匹配出非汉字的邮箱
res__2 = re.match('[a-zA-Z0-9_]{4,20}@(163|126|qq)\.com','hello@qq.com')
if res__2:
    print(res__2.group(0))
    print(res__2.group(1))

# 8.3
match_res = re.match('<([a-zA-Z1-6]+)><([a-zA-Z1-6]+)>hh</\\2></\\1>','<html><div>hh</div></html>')
print(match_res.group(0))
print(match_res.group(1))
print(match_res.group(2))