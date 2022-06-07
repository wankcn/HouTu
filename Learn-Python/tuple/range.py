# range用于表示数字序列，内容不可变
# r = range(0-99)左闭右开   #产生0-99数字序列

r1 = range(10, 20)  # 10-19
print(r1)  # 节省内存
print(type(r1))
print(r1[9])  # 打印19
print(r1[3:5])

# 增加步长
r2 = range(10, 20, 2)
print(r2)  # 10,12,14,16,18
for i in r2:
    print(i, end=" ")

print(r2[0:2])  # 输出的是range(10,14,2)

print(12 in range(10, 20))  # True

r3 = range(1, 10, 2)  # 1,3,5,7,9
for i in range(1, 10, 2):
    print(i)
print(r3[3:5])   # 截取7，9 此时左闭右开不包含9 后面在+2 为：7，11
