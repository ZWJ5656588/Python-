import pymongo

# 1. 创建mongo连接 端口号27017
client = pymongo.MongoClient(host = 'localhost',port = 27017)

connection = client['mongo-dara-info']['test_python']

# 2.1 插入单条数据
# key要带引号
# connection.insert_one({'name':'anna','age':18})

# 2.2 查询多个数据
# data_list = [{'name':f'test{i}'} for i in range(10)]
# # 直接传入列表结果集
# connection.insert_many(data_list)

# 3.1 查询一条数据
t_1 = connection.find_one({'name':'anna'})


# 3.2 查询多条数据
t_2 = connection.find()
# t_2是返回的游标对象，要对游标对象进行处理才能拿到数据
# print(t_2)

# 3.2.1 遍历拿出游标对象中的数,类似于迭代器 只能取出一次
for item in t_2:
    print(item)

# # 3.2.2 转换成列表对象读取数据
# print(list(t_2))

# 4.1 更新一条数据
connection.update_one({'name':'test1'},{'$set':{'name':'new_test1'}})

# 更新全部数据
connection.update_many({"name": "test1"}, {"$set": {"name": "new_test1"}})

# 删除一条数据
connection.delete_one({"name": "test10"})
# 删除全部数据
connection.delete_many({"name": "test9"})