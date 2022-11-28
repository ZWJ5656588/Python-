import json
user_dic={"name":"zwj","password":"123"
          ,"locked":False,"account":"15000",
          "shopping_cart":{},"bankflow":[]}
# user_dic["name"] 作为这个注册的json文件名
# print(user_dic["name])
with open((user_dic["name"]+".json"),mode="wt",encoding="utf-8") as f:
    # 将要序列化的对象写入文件，参数是(序列化对象,文件对象)
    json.dump(user_dic,f)