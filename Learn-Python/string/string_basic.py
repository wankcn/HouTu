str = "my name is wankcn"
str1 = 'hello'
str2 = "WORLD"
str3 = 'she sad:"have fun!"'
str4 = " I'm Best"

# 转换为大写
a = str.upper()
print(a)
# 转换为小写
a = str2.lower()
print(a)
# 首字母大写
a = str1.capitalize()
print(a)
# 每个单词首字母大写
a = str3.title()
print(a)
# 大小写互换
a = str4.swapcase()
print(a)

# 制表符和换行符
table = "姓名\t年龄\nwankcn\t23"
print(table)

# 删除空白
space_str = "    hello world"
print(space_str)
# 用len()获取字符串长度
lstr = len(space_str)
print(lstr)  # 字符串长度
nospace_str = space_str.strip()
print(nospace_str)  # 前后无空格的字符串
print(len(nospace_str))  # 去空格后的字符串长度

# 查找字符串 find的可以指定查询的起始位置
source = "nice to meet you, i need you help"
print(source.find("ee"))  # 出现的位置
index = source.find("ee", 17, 22)  # 不在范围内则返回-1
print(index)

#  ee是否存在字符串
isin = "ee" in source
print(isin)

# 字符串替换
# 关于replace()替换函数的使用，要替换的"a"字符串不存在，则会直接返回原字符串
str7 = "wankcn is good, chenxi is good, liuxit is good"
s = str7.replace("is", "is a")  # 不填写数字 默认全部更换
print(s)
s = str7.replace("is", "is a", 2)
print(s)

# 在字符串text中从下标为2的位置开始往后查找，返回第一个e所在位置的下标即2
text = "everyone"
print(text.find("e", 2))

i = 0
while i < 5:
    print("循环第{}次".format(i))
    i += 1
