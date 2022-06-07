import pygame


# bmi计算器
height = float(input("输入身高(m)："))
weight = float(input("输入体重(kg)："))

bmi = weight / pow(height, 2)
print("BMI值为：{}".format(bmi))

# 从上到下依次匹配 满足多条件下执行第一条，后面被忽略
if bmi <= 18.4:
    print("偏瘦")
elif bmi > 18.4 and bmi <= 23.9:
    print("正常")
elif bmi > 23.9 and bmi <= 27.9:
    print("过重")
else:
    print("肥胖")
