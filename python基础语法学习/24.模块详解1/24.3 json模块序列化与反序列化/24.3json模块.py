"""序列化
            dumps  处理字符串
            dump   处理文件
反序列化
	        loads 处理字符串
            load  处理文
"""

"""我们把对象(变量)从内存中变成可存储或传输的过程称之为序列化
序列化就是将内存中的数据结构转换成一种中间格式存储到硬盘或者基于网络传输
反序列化就是硬盘中或者网络中传来的一种数据格式转换成内存中数据结构
"""
#1.1 以字典为例进json序列化
import json
dic={'name':'dahai','age':18,'sex':'man','locked':True}
#序列化:内存中的数据类型----->中间格式json
#dumps(数据类型)
json_str=json.dumps(dic)  #处理成json字符串
print(json_str)
print(type(json_str))

# 1.2 写入json文件中
with open('24.3.db1.json', 'wt', encoding='utf-8') as f1:
    f1.write(json_str)  #存储到硬盘中

# 1.3 dump方法将上述过程合为一步
with open('24.3.db2.json', 'w', encoding='utf-8') as f2:
    json.dump(dic,f2)  #传文件对象和要序列化的对象

print('1.'+'-'*20)


#2.1  反序列化
import json
with open('24.3.db1.json','r',encoding='utf-8')as f3:
    json_str=f3.read()
    print(json_str)
    print(type(json_str))

#2.2 将json_str转化为内存中的数据类型,loads处理字符串
dic=json.loads(json_str)
print(dic)

#2.3 两步合为一步
with open('24.3.db2.json','r',encoding='utf-8') as f4:
    dic=json.load(f4)  #只传文件对象！！
print(dic)

print('2'+'-'*20)

