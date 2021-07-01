print("\n//--------------------  函数")
--[[
function 函数名()
	内容
end

-- 特殊写法
a = function()
end
]]

print("\n//--------------------  无参数无返回值")
function F1( ... )
	print("F1函数")
end
F1()

-- 有点类似事件和委托的写法
F2=function()
	print("F2函数")
end
F2()


print("\n//--------------------  有参数")
function F3( a)
	print(a)
end
F3("123") F3(1) F3(true)  -- true不能通过..拼接
F3()                      -- 没有传参数默认位nil
F3(1,2,3)                 -- 如果传入参数和参数个数不匹配 会补空或者丢弃  


print("\n//--------------------  有返回值")
function F4(a)
	return a , 123, true
end
temp= F4(1)  print(temp)
temp= F4("123")  print(temp)

-- 返回多个参数 前面声明多个变量接取 如果变量不够，只接取对应位置的返回值
function F4(a)
	return a , 123, true
end
temp1,temp2,temp3= F4(5)   print(temp1,temp2,temp3)


print("\n//--------------------  函数的类型")
-- 函数类型就是function
F5 = function()
	print("123")
end
print(type(F5))

print("\n//--------------------  函数的重载")
-- 不支持函数重载 调用默认最后声明的函数
--[[
function F6()
	print("!!!")
end

function F6(str)
	print(str.."!!!")
end
F6()     -- 调用的是第二个F6() 本身不报错，但是这个函数会报错是因为默认没有传参数 为nil nil不支持字符串拼接报错
]]

print("\n//--------------------  变长参数")
function F7(...)
	-- 变成参数使用用一个表存起来 再使用
	arg={...}
	for i=1,#arg do
		print(arg[i])
	end
end

F7(1,2,3,4,true,"123",nil,2)

print("\n//--------------------  函数嵌套")
function F8()       -- F8返回一个函数
	-- F9 = function()
	-- 	print(123)
	-- end
	-- return F9
	return function ()
		print("123")
	end
end

f9 = F8()
f9()    -- f9变成了内部函数

-- 在Lua里闭包的体现 在函数里面返回一个函数 改变了函数里变量的生命周期

function F9(x)
	-- 改变传入参数的生命周期
	return function(y)
		return x+y 
	end
end

f10 =F9(6)
print(f10(5))


print("\n\n\n\n\n")
