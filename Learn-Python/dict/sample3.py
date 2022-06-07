# 字典的更新与删除
mine = {
    'name': '万康',
    'sex': '男',
    'age': 21,
    'english_score': 95,
    'math_score': 89
}
print(mine)
# 数据的更新 默认加在最后
mine['chinese_score'] = 78
print(mine)
# 数据的更新 默认加在最后
mine['chinese_score'] = 88
print(mine)
# 多个k,更新
mine.update(math_score=55, chinese_score=66)
print(mine)
# 有则更新，无则加勉


# 删除操作
# 1. 删除指定的k,v
mine.pop('chinese_score')
print(mine)
# 2. 删除最后一个kv
kv = mine.popitem()
print(kv)
print(mine)
# 3.clear 清空字典
mine.clear()
print(mine)
