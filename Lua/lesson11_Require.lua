print("\n//--------------------  全局变量和本地变量")
-- 全局变量
a = 1 
b = "123"

for i =1,2 do
	c = "wenruo"
end

print(c)

-- 局部变量使用local 只作用于对应的语句块
for i =1,2 do
	local d ="!"
end
print(d)  -- 打印是一个nil值

fun = function()
	tt="123123"
end
print("函数没有执行打印tt", tt)  -- 不执行等于没有声明

fun()
print("执行函数以后打印tt",tt)   -- 是一个全局的 全局浪费内存

local aaa = "脚本内的局部变量"
print("aaa",aaa)

print("\n//--------------------  多脚本执行")
-- 关键字 require("脚本名")
print("\n//--------------------  脚本卸载")  
print("\n//--------------------  大G表")