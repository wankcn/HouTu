persons = ['张三', '赵六', '李四', '王五', '赵六', '钱七', '孙八']

count = len(persons)  # 获取长度

i = 0
for p in persons:
    if p == '赵六':
        d = -count + i  # 倒叙索引
        print(p, i, d)
    i += 1

print("----------while循环来写-----------")
# while循环来写
i = 0
while i < len(persons):
    p = persons[i]
    if p == '赵六':
        d = -count + i
        print(p, i, d)
    i += 1
