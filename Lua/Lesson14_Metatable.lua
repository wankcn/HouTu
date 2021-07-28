print("\n//--------------------  元表")
print("\n//--------------------  元表的概念")
-- 任何表变量都可以作为另一个表变量的元表
-- 任何表变量都可以用自己的元表（可以理解为一张表的爸爸）
-- 当子表（有元表的这张表）中进行一些特定操作时，会执行元表中的内容

print("\n//--------------------  设置元表")

fatherMeta = {}
subTable ={}

-- 设置元表函数 第一个参数：子表 / 第二个参数：元表 
setmetatable(subTable,fatherMeta)

print("\n//--------------------  特定操作")
print("\n//--------------------  特定操作__tostring")

meta = {
	-- 当子表被当作字符串使用时，会默认调用元表中的__tostring()方法
	-- 如果在tostring后面加一个参数，当打印表的时候，默认把自己传进去 
	__tostring= function(t)
		return t.name
	end
}
myTable = {
	-- 打印子表中的name，无法在元表里得到子表。
	-- 因为通过子表关联的元表，所以无法通过元表得到属性，在__tosting里传入变量
	name = "想在子表中打印名字：文若" 
}
setmetatable(myTable,meta)
print(myTable)  

print("\n//--------------------  特定操作__call")
meta3 = {
	__tostring = function(t)
		return t.name
	end,

	-- 当子表被当作一个函数来使用时，会默认调用__call中的内容
	-- a代表myTable本身，类似于：调用。把自己作为第一个参数传进去
	__call = function(a,b) 
		print(a)    -- a是打印自己，其实是__tostring()的方法
		print(b)    -- 第一个参数是表本身，第二个参数才是传入的参数
		print("文若真厉害")
	end

}
myTable3 = {
	name = "文若"
}
setmetatable(myTable3,meta3)

-- 只有在表里面设置了元表，并且在元表里实现了__call
myTable3(1)     -- 子表当作函数使用，调用__call，默认第一个参数是自己

print("\n//--------------------  特定操作运算符重载")

meta4 = {
	-- 相当于运算符重载，当子表使用加法时调用
	__add = function(t1, t2)
		return t1.age + t2.age
	end,
	-- 运算符 - 
	__sub = function(t1, t2)
		return t1.age - t2.age
	end,
	-- 运算符 *
	__mul = function(t1, t2)
		return t1.age * t2.age
	end,
	-- 运算符 /
	__div = function(t1, t2)
		return t1.age / t2.age
	end,
	-- 取余 %
	__mod = function(t1, t2)
		return t1.age % t2.age
	end,
	-- 幂运算
	__pow = function(t1, t2)
		return t1.age ^ t2.age
	end,
	-- 条件运算符 ==
	__eq = function(t1, t2)
		return t1.age == t2.age
	end,
	-- 小于
	__lt = function(t1, t2)
		return t1.age < t2.age
	end,
	-- 小于等于
	__le = function(t1, t2)
		return t1.age <= t2.age
	end,
	-- ~= > >= 需要自己取反
	-- 拼接..
	__concat = function(t1, t2)
		return t1.age .. t2.age
	end,
}
myTable4 ={
	age = 3
}
-- 设置元表函数 第一个参数：子表 / 第二个参数：元表 
setmetatable(myTable4,meta4)
myTable5 = {
	age = 2
}
setmetatable(myTable5,meta4)

print(myTable4 + myTable5)
print(myTable4 - myTable5)
print(myTable4 * myTable5)
print(myTable4 / myTable5)
print(myTable4 % myTable5)
print(myTable4 ^ myTable5)
-- 如果用条件运算符来比较两个对象 这两个对象的元表必须一致才能准确调用方法
print(myTable4 == myTable5)
print(myTable4 < myTable5)    -- 改成大于相当于是换了个位置然后重载
print(myTable4 <= myTable5)
print(myTable4 .. myTable5)

--------------------------------------------------------------------------
--- __index
--- __newIndex

print("\n//--------------------  特定操作__index和__newIndex")

meta6 = {
	__index = {
		age = 1,
		temp = 2
	}

}
myTable6 = {}
setmetatable(myTable6,meta6)
print(myTable6.age)
print(myTable6.temp)

meta7 = {}
meta7.__newIndex={age =2}
myTable7 = {}

setmetatable(myTable7,meta7)

print(myTable7.age)






