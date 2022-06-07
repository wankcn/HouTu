# list的其他使用方法
persons = ['张三', '赵六', '李四', '王五', '赵六', '钱七', '孙八']

# 统计出现次数
ctn = persons.count('赵六')
print(ctn)

# 追加操作 追加整体列表
persons.append(['杨九', '侯十'])  # 额外创建了一个新的列表
print(persons)
# 使用拓展的方法添加多个 追加元素单个的
persons.extend(['杨九', '侯十'])
print(persons)

# 判断数据是否存在列表中 存在True 不在False
b = '张三' in persons
print(b)

# 列表的复制
persons1 = persons.copy()
print(persons1)

# is 判断是否指向同一块内存
print(persons1 == persons)
print(persons1 is persons)

# clear用于清空列表
persons.clear()
print(persons)
