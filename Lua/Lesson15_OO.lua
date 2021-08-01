---
--- 面向对象 类 都是基于表table 类似静态类
--- 元表
---
--------------------------------------------------------------------------

-- /////////////////////////////////// [ 封装 ] ///////////////////////////////////

Object = {
	id = 1,
	name = "wenruo",
	age = 21,

}

function Object:Test()               -- 谁调用，谁就是self
	print("测试方法",self.id)
end

function Object:New()                -- 冒号，会自动将调用这个函数的对象作为第一个参数														 
	local obj = {}                   -- 对象就是变量，本质上是一张表
	self.__index = self              -- self,代表默认传入的第一个参数
	setmetatable(obj,self)           -- __index当找自己的索引找不到时，去找元表里的内容
	return obj                       -- 需要返回一个新的对象。
end

local temp = Object:New()            -- 本质上是创建一张空表，访问属性没有时候访问父级的
print(temp)
print(temp.id)
print(temp.age)
temp:Test()   -- 此时打印的是Object的id
temp.id = 2   -- 通过Object:new()得到的是一张空表，这一句相当于声明一个新的属性
temp:Test()   -- 此时打印新的id 2

-- /////////////////////////////////// [ 继承 ] ///////////////////////////////////
--- 创建一个用于继承的方法
function Object:SubClass(className)
	_G[className] = {}
	local obj = _G[className]
	self.__index = self
	setmetatable(obj,self)            -- 谁调用，元表就是谁
end

Object:SubClass("Person")
print(Person)
print(Person.name)

local per = Person:New()              -- Person中没有new方法，其实调用的是Object的new方法
print("per.id:",per.id)               -- 从Person中取值，娶不到继续Person的元表Object中取

-- /////////////////////////////////// [ 多态 ] ///////////////////////////////////


