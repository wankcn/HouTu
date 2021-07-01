print("\n//--------------------  条件分支语句")
a = 9
-- if 条件 then 内容 end
if a > 5 then
	print("打印信息")
end

-- if 条件 then 内容
-- else 内容 end
if a > 5 then
	print("满足")
else
	print("不满足")
end

-- 多分支
--[[
if 条件 then
	内容
elseif 条件 then
	内容
else
	内容
end
]]
if a > 5 then
	a = a + 1
	-- elseif 连着写
elseif a == 5 then
	a = a - 1
else 
	a = 0
end

-- lua中没有switch语法。 不支持三目运算符


if a >= 3 and a <= 9 then
	print("a在3-9之间")
end




print("\n\n\n\n\n\n")