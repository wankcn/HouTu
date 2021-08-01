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

--------------------------------------------------------------------------
print("\n//--------------------  多脚本执行")
-- 关键字 require("脚本名")
require("Test")
print("打印Test的testA",testA)            -- 可以使用
print("打印Test的testLocalA",testLocalA)       -- 脚本的本地变量无法使用 为nil

print("\n//--------------------  脚本卸载")  
-- 如果是require加载执行的脚本 加载一次过后不会再执行
require("Test")   -- 再次require 没有打印“456”

-- package.loaded["脚本名"] 返回bool 表示当前有没有在执行脚本名
bool = package.loaded["Test"]
print(bool)
-- 卸载脚本 
package.loaded["Test"] = nil
-- 卸载后在执行脚本 可以打印出来内容“466”
local textLA = require("Test") 
-- require执行脚本的时候可以把外部需要获取的本地变量return出去
print(textLA)  -- 使用其他类的局部变量，可以返回回来

 
--------------------------------------------------------------------------
print("\n//--------------------  大G表")
-- _G 这是一个固定写法，可以在Lua里面直接使用
-- 是一个总表 table 
-- 它把我们声明的所有的全局变量都声明在其中
print("打印_G表看一下///////////////////////")
for k,v in pairs(_G) do
	print(k,v)
end

-- _G表不会存储本地变量




