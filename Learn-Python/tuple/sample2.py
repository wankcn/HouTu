# 序列类型件的互相转换
l1 = ['a', 'b', 'c']
t1 = ('a', 'b', 'c')
s1 = "abc123"
s2 = "abc,123"
r1 = range(1, 4)
# list() - 转换成列表
l2 = list(t1)
print(l2)
print(list(s1))
print(s2.split(","))  # 以符号分割 返回依然是列表

# 把range转换成list
print(list(r1))

# 转换成元组
print(tuple(l1))
print(tuple(s1))
# 带特殊符号的字符串只能转换成列表 不能转换成元组 需要split分割
print(tuple(s2))
print(tuple(s2.split(",")))

# 将元组列表转换成字符串  str join对列表进行连接
print(str(l1))
print(",".join(l1))  # .前面代表多个元素的分隔符
# join必须要求所有元素都是字符串

# 将包含数字的序列输出
s3 = ""
for i in r1:
    s3 += str(i)
print(s3)

# range是单向转换
