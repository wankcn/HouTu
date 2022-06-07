# list的增删查改
persons = ['张三', '赵六', '李四', '王五', '赵六', '钱七', '孙八']
# 列表的追加
persons.append("杨九")
print(persons)
persons.insert(2, '牛二')
print(persons)
# 用insert追加
persons.insert(len(persons), '侯大')
print(persons)

# 替换
persons[2] = '宋二'
print(persons)
persons[3:5] = ['王五', '李四']
print(persons)

# 删除
persons.remove('宋二')
print(persons)
persons.pop(4)  # 按照索引值删除
print(persons)

# 删除连续值 范围删除
persons[4:7] = []
print(persons)
