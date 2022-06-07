"""
    计算20的阶乘
    当前阶乘能被5整除，则打印中间结果
    输入自定义数值1-100
"""
sum = 1
i = 1
a = int(input("输入要执行阶乘的数："))
if 1 <= a <= 100:
    while i <= a:
        sum *= i
        if i % 5 == 0:
            print("当前执行到:{}\t当前阶乘结果:{}".format(i, sum))
        i += 1

else:
    print("输入的值不在1-100范围内")

print(sum)
