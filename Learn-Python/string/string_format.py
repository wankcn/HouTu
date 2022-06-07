name = "wankcn"
age = 23
height = 170.5
str1 = "我叫" + name + ",今年" + str(age) + "岁。身高" + str(height) + "。"
print(str1)
str2 = "我叫{0},年龄{1},身高{2}"
# format 格式化字符串
str2 = str2.format(name, age, height)
print(str2)

# format赋用别名 避免任意打乱顺而程序紊乱
str3 = "我叫{p1},我在{p4}班,年龄{p2},身高{p3}"
str3 = str3.format(p1=name, p2=age, p3=height, p4="3-2")
print(str3)

# 数字的格式化输出
num = 1234567.89555
str4 = format(num, "0.2f")
print(str4)

# 金币金额三位一分号分隔
account = "wankcn"  # 账户
amt = 123456789
str5 = format(amt, "0,.3f")  # ,号前面是整数,后面是小数部分
print(str5)
# 数字格式化输出时，需要在{}内增加:前缀
str6 = "请您向{}账户转账Y{:0,.3f}"
print("---------------------")
str6 = str6.format(account, amt)
print(str6)

# 早起的字符串格式化
# 我叫wankcn 今年23岁 体重59.7kg
name = "wankcn"
age = 23
weight = 59.7
str7 = "我叫%s，今年%d岁，体重%.2fkg" % (name, age, weight)
print(str7)


