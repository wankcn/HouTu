#  字典的常用操作
# 1 设置字典默认值


emp1 = {'name': 'wankcn', 'score': 'A'}
emp2 = {'name': 'chenxi'}

# 如果已存在则忽略，不存在就设置
emp2.setdefault('score', 'C')
print(emp2)

# if 'score' not in emp2:
#     emp2['score'] = 'C'
# print(emp2)


# 2 查看字典视图
"""
1 获取所有的keys
2 获取所有的values
3 获取所有的键值对 items
"""
ks = emp1.keys()
print(ks, type(ks))

vs = emp1.values()
print(vs, type(vs))

its = emp1.items()
print(its, type(its))

print("--视图对象随着原始数据联动")
emp1['sex'] = '男'
print("keys{}\nvalues{}\nitems{}".format(ks, vs, its))
# 3 字典的格式化输出
# 老版本格式化
emp_str = "姓名:%(name)s,性别:%(sex)s,成绩:%(score)s" % emp1
print(emp_str)
# 新版本
emp_str1 = "姓名：{name},性别：{sex},成绩：{score}".format_map(emp1)
print(emp_str1)
