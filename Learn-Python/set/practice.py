# 求两个列表中的交集，并集，差集

a_list = [1, 2, 3, 4, 5]
b_list = [1, 4, 7, 9]
a_set = set(a_list)
b_set = set(b_list)
# 求两个列表之间的交集
int_set = a_set.intersection(b_set)
int_list = list(int_set)
print(int_list)
# 求两个列表之间的并集
uni_set = a_set.union(b_set)
uni_list = list(uni_set)
print(uni_list)
# 求两个列表之间的差集（a_list在b_list中不存在的部分）
dif_set = a_set.difference(b_set)
dif_list = list(dif_set)
print(dif_list)

#############################################
lst = [23, 45, 22, 44, 25, 66, 78]
# 生成所有奇数组成的列表
lst1 = [i for i in lst if i % 2 != 0]
print(lst1)
# 输出结果[28, 50, 27, 49, 30, 71, 83]
lst2 = [i + 5 for i in lst]
print(lst2)
# lst2 = []
# for i in lst:
#     i += 5
#     lst2.append(i)
# print(lst2)
