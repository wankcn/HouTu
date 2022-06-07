# 列表与字典更新

a = [1, 2, 3, 4, 5]
b = {
    1: 2,
    2: 3,
    3: 4,
    4: 5
}

print(a)
print(b)

print("更新")
a[1] = 1111
b[1] = 1111
print(a)
print(b)
a[4] = 1111  # 列表只能修改
b[5] = 1111  # 字典有则更新，无则加勉
print(a)
print(b)
