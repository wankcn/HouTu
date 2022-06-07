# 集合的运算
college1 = {"软件工程", "土木", "风景园林", "会计", "金融"}
college2 = set(["软件工程", "土木", "风景园林", "会计", "金融", "历史", "法律"])

# 交集 获取重复部分新建一个集合
c3 = college1.intersection(college2)
college1.intersection_update(college2)  # 更新原始集合为交集内容
print(c3)
print(college1)

# 并集 两个集合所有元素合并去重
college1 = {"软件工程", "土木", "风景园林", "会计", "金融"}
college2 = set(["软件工程", "土木", "风景园林", "会计", "金融", "历史", "法律"])
c4 = college1.union(college2)
print(c4)  # 并集没有更新

# 差集 两个集合之间差异的部分
c5 = college1.difference(college2)  # difference得到A在B中不存在的部分
print(c5)
c6 = college1.symmetric_difference(college2)  # 双向差集 联合A在B中不存在的和B中A不存在的
print(c6)

# update 将原有集合更新
