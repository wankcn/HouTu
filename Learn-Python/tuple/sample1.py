# 元组的使用
tuple1 = (1, 2, 3, 4, 5, 6, 7)
# 创建
t = 1, 2, 3, 4, 5, 6, 7
print(t)
print(type(t))

# 获取数据与列表完全相同
print(t[5])
# 倒叙索引
print(t[-2])
print(t[1:4])  # 范围取值
print(3 in t)  # 成员运算符

# 元组在创建后内容不可变
# t[2] = 1   # 'tuple' object does not support item assignment
# 元组内的列表允许被修改
t2 = (['wankcn', 21], ['wank', 22])
item = t2[0]
print(item)
item[1] = 25
print(t2)

# 元组运算符 同样适用于列表
t3 = (1, 2, 3) + (4, 5, 6)
print(t3)
t4 = ('wa',) * 2
print(t4)



"""
    列表与元组的区别：
           列表                 元组
    内容允许扩展         |   内容不可变
    内存存储动态变化      |   创建后固定不变
    效率较低            |   效率较高
    运行时数据需要变更使用 |   用于保存稳定不变的数据
    保存天气数据、股市数据 |  保存国家名、元素周期表
"""