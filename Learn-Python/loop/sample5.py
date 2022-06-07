"""
    超着1000以内的质数
    除1和它本身，不能被任何数整除的数
"""
# i = 2
# for x in range(1000):
#     x = int(x)
#     for i in x:
#         if x % i != 0:
#             print("{}是质数".format(x))
#     i += 1
# print("#######################")
j = 2
while j <= 1000:
    num = j
    i = 2
    is_prime = True  # 标识当前数字是否为质数 True-是  False 不是
    while i < num:
        if num % i == 0:
            is_prime = False
            break
        i = i + 1
    if is_prime == True:
        print("{}是质数".format(num))
    j = j + 1
