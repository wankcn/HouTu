# 字典的取值操作
mine = {
    'name': '万康',
    'sex': '男',
    'age': 21
}

# 指定取值名称
name = mine['name']
print(name)

# get函数取值
sex = mine.get('sex')
print(sex)
# 为不存在赋予默认值
birth = mine.get('birth', '列表里不存在')
print(birth)
# 判断key存在dict
print('name' in mine)
print('dept' in mine)
print('dept' not in mine)


print("---------------遍历字典---------")
# 遍历字典
# for k in 字典 得到的是字典里的key
for key in mine:
    v = mine[key]
    print(key, v)

print("---第二种方法---")

for key, value in mine.items():  # items包含每一个键值对
    print(key, value)
