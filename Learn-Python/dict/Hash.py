# 散列值
h1 = hash('abc')
print(h1)
h2 = hash('bcd')
print(h2)

# 数字哈希值是自己
h3 =hash(8813)
print(h3)

"""
    同一次运行中是和h1相同的
    每一次运行会生成唯一的哈希值
"""
h4 = hash('abc')
print(h4)
h5 = hash('def')
print(h5)

"""
keys ==》 哈希值 ==》内存地址：值
1。数据存储是根据哈希的散列值存储的 
2。并不是按照keys顺序排列 
3。速度快  优先字典存储结构化数据
"""
