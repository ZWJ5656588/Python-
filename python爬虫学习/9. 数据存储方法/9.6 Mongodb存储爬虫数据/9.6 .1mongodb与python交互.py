import pymongo

client = pymongo.MongoClient(host='localhost',port=27017)
db = client.mydb
myset = db.testset
myset.insert_one({"name":'zhangsan','age':'18'})

#
collection = client['test']['stu_info']
# collection.insert_one({'name':'韦世豪','hometown':'山东','age':28,'gender':'true'})
collection.update_one({'gender':'true'},{'$set':{'gender':True}})