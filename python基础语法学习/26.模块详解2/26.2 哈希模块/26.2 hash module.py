"""1 只要传入的内容一样，得到的hash值必然一样=====>文件完整性校验
2 不能由hash值返解成内容=======》把
密码做成hash值，不应该在网络传输明文密码
3 只要使用的hash算法不变，无论校验的内容有多大，得到的hash
值长度是固定的,这样不影响传输"""

import hashlib
# # 1创建hash工厂
m=hashlib.md5()
# # 2在内存里面运送
# m.update('helloworld'.encode('utf-8'))
# print(m.hexdigest())
#fc5e038d38a57032085441e7fe7010b0
# # 一点一点的给，因为可能二进制会很长 ,这个要好一些
m.update('hello'.encode('utf-8'))
m.update('world'.encode('utf-8'))
# # 3、产出hash值
print(m.hexdigest())
# fc5e038d38a57032085441e7fe7010b0
# fc5e038d38a57032085441e7fe7010b0

# 3. 哈希密码加盐

# 输入密码的时候是沿着网络传输到别的服务器上面，黑客可以把包抓下来
# 所以发给服务端是hash值，也就是密文
# 但是还是可以抓下来
# 常用密码字典
# 什么生日 ， 123 ， 身份证 等等 密码有强烈的个人习惯
# 那么我用一样的hash算法，是不是可以得到一样的hash值 密文 那么明文肯定是一样的
# 撞库风险
# 密码前后加盐
import hashlib
pwd = 'abc123'
m = hashlib.md5()
#
m.update('大海老师'.encode('utf-8'))
m.update(pwd.encode('utf-8'))
m.update('大帅比'.encode('utf-8'))
#
#
print(m.hexdigest())
# 服务器也有相应的规则
# 黑客破解成本远大于收益成本
# 中间加盐
import hashlib
pwd = 'abc123'
m = hashlib.md5()
print(pwd[0])    # a
print(pwd[1:])   # bc123
m.update('大海老师'.encode('utf-8'))
m.update(pwd[0].encode('utf-8'))
m.update('大帅比'.encode('utf-8'))
m.update(pwd[1:].encode('utf-8'))
m.update('夏洛老师'.encode('utf-8'))
print(m.hexdigest())
