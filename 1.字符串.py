my_str="welcom to www.tulingxueyuan.com"
#1.1split 方法
print(my_str.split("."))#split返回值是一个列表
a=my_str.split()
print(type(a))
print("-"*20)

# 1.2replace方法
print(my_str.replace("w", "W"))
print(my_str.replace("w", "W", 2))  # 最后的count表示从左到右替换的个数
print("-" * 20)

# 1.3upper,lower使字符出串所有字母变换大小写
a = my_str.upper()
print(a)
print(a.lower())
print(my_str)
print("-" * 20)

#1.4join 方法 （重点）
my_str2="_"
str_list=["welcome","to","Beijing"]
#返回一个新的字符串
print(my_str2.join(str_list))
print(my_str2)
print("-"*20)

#1.5strip方法，删除字符串两端的空白
my_str3 = "   welcome to www.tulingxueyuan.com   "
print(my_str3.strip())
print(my_str3)
print("-"*20)

#1.6字符串简单拼接
str1="HELLO"
str2="我是外星人"
print(str1+","+str2)
print("-"*20)

#1.6关键字查询
import keyword
print(keyword.kwlist)
print("-"*20)

#1.7
"""查询字符串中字符的索引值可用find.()/rfind.() 若str存在于该字符串中，则返回其索引值，不存在返回-1,
也可以使用index,但index方法在不存在时直接报错，且index可用用于列表，而find/rfind不可以"""
str5="sdsaijein"
print(str5.find("a"))
print(str5.index("a"))
list1=[5,6,"sd",6589]
k=list1.index(6)
print(k)