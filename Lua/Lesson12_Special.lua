print("\n//--------------------  特殊用法")

print("\n//--------------------  多变量赋值")
local a,b,c = 1,2
print(a)
print(b)
print(c)


-- 多变量赋值，如果值多了，会自动省略
local a,b,c = 6,7,8,3,4,5
print(a)
print(b)
print(c)

print("\n//--------------------  多返回值")
-- 多返回值，要用几个返回值，就用几个变量去存
-- 少省多补
function Test()
	return 10,20,30,40	
end

a,b,c = Test()
print(a,b,c)

a,b,c,d,e = Test()
print(a,b,c,d,e)


print("\n//--------------------  and / or")
-- 逻辑与，逻辑或
-- and 和 or 任何东西都可以用连接
-- 在lua中，只有nil和false才会认为是假
-- 支持短路运算 and 有假则假  / or 有真则真
-- 只需要判断第一个是否满足，就会停止计算
print(1 and 2,1 or 2)

-- 有真则真
print(nil and 2)
print(true and 3)


-- lua不支持三目运算符 使用and 和or 特性模拟三目运算符
-- 取两个值之间的最大值
x = 3
y = 22

-- and 有假则假  / or 有真则真
local res = (x>y) and x or y
print(res)










