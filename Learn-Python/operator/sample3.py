# 位运算符
a = 60
b = 13
c = 0

# oct 8进制 0o
# bin 2进制 0b
# hex 16 进制 0x
d = hex(a)
print(d)

c = a & b
print(c)

c = a | b
print(c)

c = a ^ b
print(c)

# 11000011=195
# -(~11000011+1)
# -(00111100+1)
# -00111100
c = ~a
print(c)

# 00111100
# 00111100000
c = a << 3
print(c)

# 00111100
c = a >> 3  # 右移三位 前面加3个零 后面去三个位
print(c)
# 00000111100
# 00000111

a, b = 34, 27
c = a & b
print(c)  # c=2
a, b = 56, 19
c = a | b
print(c)  # c=59
