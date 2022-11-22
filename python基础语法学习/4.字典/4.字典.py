#1.1字典中，key不可以重复，value可以重复，{}，且key必须是不可变类型，key一定程度上符合集合中元素性质
teacher_info={
    "name":"朱文峻",
    "age":21,
    "adress":"北京",
    "institution":"北京航空航天大学",
    1:"北京"
}
print(teacher_info)
print("-"*20)

#2.1遍历字典的键
for key in teacher_info.keys():
    print(key)
print("-"*20)

#2.2遍历字典的值
for value in teacher_info.values():
    print(value)
print("-"*20)

#2.3遍历字典中所有键值对 item方法,for遍历以后返回对应的元组
for item in teacher_info.items():
    print(item)
print("-"*20)

#3.1如果查询的key在字典中不存在，则回报错
#print(teacher_info["money"])
#如果不确定key是否存在与字典中，但不想让程序报错，返回None
teacher_info = {
    "name": "顾安",
    "age": 18,
    "home": "湖南省长沙市"
}
print(teacher_info.get('QQ', ))  # 当前字典不存在QQ这个键

