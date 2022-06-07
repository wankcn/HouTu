# 列表的创建
# 变量名=[元素1,元素2...]
list = ['a', 'b', 1, 2, 3]
print(list)

# 列表的取值
#         0       1      2      3      4       5
list = ['张三', '李四', '王五', '赵六', '钱七', '孙八']
#         -6     -5      -4     -3    -2        -1
print(list[3])
print(list[-3])
# 范围取值  左闭右开
print(list[1:4])

# index获取元素指定索引 只返回第一次匹配到
print(list.index("赵六"))

list[0] = '万康'
print(list)
