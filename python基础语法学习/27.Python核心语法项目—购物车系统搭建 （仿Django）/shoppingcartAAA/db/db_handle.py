from conf.setting import DB_path
import os
import json

class Serialization:
    # 运用反序列化 读取用户输入的数据
    def select(self,name):
        # print(name)
        path=(r"%s/%s.json" % (DB_path,name))
        if os.path.isfile(path):
            with open(path,'rt',encoding='gbk') as f:
                dic=json.load(f)
                return dic
        else:
            return False

    # 更新用户注册，写入序列化
    def update(self,user_dic):
        path_file=os.path.join(DB_path,"%s.json" % user_dic["name"])
        with open(path_file,"wt",encoding="gbk") as f:
            # json.dump写入
           json.dump(user_dic,f)


db_serialization=Serialization()
