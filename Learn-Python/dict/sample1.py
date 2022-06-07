# 字典的创建
dict1 = {}  # 空的字典
print(type(dict1))
dict2 = {
    'name': '万康',
    'sex': '男',
    'age': 21
}
print(dict2)

# 利用dict函数创建字典
dict3 = dict(name='万康', sex='男', age=21)
print(dict3)
# 利用fromkeys创建键
dict4 = dict.fromkeys(['name', 'sex', 'age'], 'N/A')  # 默认值为'N/A'
print(dict4)
