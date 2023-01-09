import  csv

# 1. 单行写入
with open('9.3.1 data.csv','w',encoding = 'gbk') as f:  # excel默认编码gbk
    writer = csv.writer(f)  # 传入句柄
    writer.writerow(['id','name','age'])
    writer.writerow(['10001','百川','18'])
    writer.writerow(['10002','里的','8'])
    writer.writerow(['10003','存储','28'])
    writer.writerow(['10004','收到','38'])

# 多行写入

