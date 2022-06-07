# 遍历其它序列

a = 'abcdefg'
for i in range(0, len(a)):
    letter = a[i]
    print(letter)
#######################################################
# 操作斐波那契额数列
# 1，1，2，3，5，8，13，...
result = []
for i in range(0, 50):
    if i == 0 or i == 1:
        result.append(1)
    else:
        result.append(result[i - 2] + result[i - 1])
print(result)
#######################################################
# 判断质数
l = 776351721
flag = True
for i in range(2, l):  # 除去1和它本身
    if l % i == 0:
        flag = False
        break
if flag is True:
    print("{}是质数".format(l))
else:
    print("{}不是质数".format(l))
#########################################################
# 有四个数字1、2、3、4，能组成多少个互不相同且数字不重复的两位数
count = 0
# 定义一个空列表用于存放数据
num = []
for i in range(1, 5):
    # 使用for循环得到另一个数j
    for j in range(1, 5):
        if i != j:
            # 将数据添加到列表中
            result = i * 10 + j
            num.append(result)
            count += 1
print(count)
# 输出得到的数据
print(num)
