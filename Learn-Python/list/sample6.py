# 嵌套列表 多维列表
# [[name,sex,wage],[name,sex,wage],[name,sex,wage],[name,sex,wage]]

str = '张三，男，2000'
l = str.split('，')
print(l)

# 员工信息
emp_list = []

while True:
    info = input("请输入员工信息：")
    if info == "":
        print("程序结束")
        break
    info_list = info.split("，")
    if len(info_list) !=3:
        print("输入不正确，请重新输入")
        continue
    print(info_list)
    emp_list.append(info_list)
    print(emp_list)
