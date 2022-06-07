# continue学习
start = 101
end = 183
for a in range(start, end+1):
    if a%17!=0:
        continue
    print(a)

