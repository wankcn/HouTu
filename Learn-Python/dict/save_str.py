source = "001,wankcn,男,21,1996-05-01,3000¥002,chenxi,女,20,1997-10-20,1000¥003,louxiyi,女,20,1998-10-20,2000"
per_list = source.split("¥")
print(per_list)

# key是身份ID，values是完整的学生信息
all_per = {}
# 取出索引值
for i in range(0, len(per_list)):
    # print(i)  # 取出索引值
    n = per_list[i].split(",")
    print(n)  # 打印取出的新列表
    # 创建学生字典 把列表n存进字典个人信息字典per
    per = {"id": n[0], "name": n[1], "sex": n[2], "age": n[3], "birth": n[4], "wear": n[5]}
    print(per)
    # 往字典里添加新的键值，有则忽略，无则加勉
    all_per[per["id"]] = per  # 键值 key是id，value是per的完整信息
print(all_per)

id = input("请输入学生编号:")
per = all_per.get(id, '不存在此学生信息')
print(per)
# 格式化输出
print("学号：{id}，姓名：{name}，性别：{sex}，年龄：{age}，生日：{birth}，工资：{wear}".format_map(per))
