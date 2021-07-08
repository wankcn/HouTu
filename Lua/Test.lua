print("这是TestLua脚本")

-- 全局变量
testA = "123"

-- 局部变量
local testLocalA = "456"
print(testLocalA)


-- 把本地变量返回出去
return testLocalA