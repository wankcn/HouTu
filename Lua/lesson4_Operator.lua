print("\n//--------------------  算术")
-- + - * / % ^
-- 没有自增自减 没有复合运算符
a = 1 b = 2
print("加法 "..a + b)
print("123" + 1)   -- 得 124   lua把字符串转换成数值
print("123.4" + 1)

print("减法 "..a - b)
print("123" - 1)   -- 122

print("乘法 "..1 * 2)
print("123" * 2)   -- 246

print("除法 "..1 / 2)
print("123" / 2)   -- 61.5

print("取余 "..1 % 2)
print("123" % 2)   -- 246

print("幂运算 ".. 2 ^5)

print("\n//--------------------  条件")
-- > < >= <= == ~=
print(3>1)
print(3<1)
print(3>=1)
print(3<=1)
print(3==1)
print(3~=1)

print("\n//--------------------  逻辑")
-- and or not lua中也支持短路 
print(true and false)
print(true and true)

print(true or false)
print(false or false)

print(not true)

print("\n//--------------------  位")
-- 不支持位运算符 需要自己去实现
print("\n//--------------------  三目")
-- 不支持三目运算符









print("\n\n\n\n\n")


