# pip3 install redis
from redis import Redis

redis_obj=Redis(host='localhost',port=6379,db=0)

# # 添加字符串
# result=redis_obj.set('name','anna')
# print(result)  # 返回布尔值

# # 获取数据
# result=redis_obj.get('name')
# print(result.decode())

# #修改数据
# result=redis_obj.set('name',"安娜")
# print(result)
# result2=redis_obj.get('name')
# print(result2.decode())

# 获取key
result=redis_obj.keys()
print(result)

