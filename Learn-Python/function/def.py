# 函数的使用技巧一 设置默认值
def exchange(a, c="u"):
    if a == "c" and c == "u":
        return 1
    else:
        return 2


e = exchange("c", "a")
print(e)


# 以行参形式传参
def x(a, b, c):
    print(a + b + c)


x(a=2, c=4, b=3)  # 增加可读性  关键字传参
print(x)


##############################################
# *d代表之后所有参数传参必须是关键字传参
def x(a, b, *, c):
    print(a + b + c)


r = x(2, 3, c=4)  # 增加可读性  关键字传参
print(r)
