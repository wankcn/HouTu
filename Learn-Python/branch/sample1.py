
# 判断一个数数否为水仙花数

num = int(input("请输入一个三位数："))

# 分别求出三位数的个位，十位，百位
bw = num // 100
sw = (num - bw * 100) // 10
# 定义变量total，保存各位数字立方和
gw = num - bw * 100 - sw * 10
# 用if语句判断条件是否成立，并做出相应的输出
if bw ** 3 + sw ** 3 + gw**3 == num:
    print("{} 是水仙花数".format(num))
else:
    print("{} 不是水仙花数".format(num))