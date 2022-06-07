# 循环嵌套
"""
  口口口口
  口口口口
  口口口口
  口口口口
"""

for x in range(1, 5):
    for y in range(1, 5):
        print("口", end="")
    print()

print("------------分割线--------")
i = 1
while i <= 4:
    i += 1
    i2 = 1
    while i2 <= 4:
        print("口", end="")
        i2 += 1
    print()
