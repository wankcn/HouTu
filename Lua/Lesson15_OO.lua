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
	obj.base = self                   -- [用于多态] 定义一个base属性等于表
	setmetatable(obj,self)            -- 谁调用，元表就是谁
end

Object:SubClass("Person")
print(Person)
print(Person.name)

local per = Person:New()              -- Person中没有new方法，其实调用的是Object的new方法
print("per.id:",per.id)               -- 从Person中取值，娶不到继续Person的元表Object中取

-- /////////////////////////////////// [ 多态 ] ///////////////////////////////////

Object:SubClass("GO")                 -- 继承object
GO.posX = 0
GO.posY = 1

function GO:Move()
	self.posY = self.posY + 1
	self.posX = self.posX + 1
	print("posX: ".. self.posX,"posY: " .. self.posY)
end

GO:SubClass("Player")                 -- 继承GO

function Player:Move()
	print("Player 重写的方法！")
--	self.base:Move()                  -- 冒号默认传第一个参数是self，相当于把基类传进去 相当于GO

	self.base.Move(self)              -- 用.调用传入self,不传self相当于通过元表修改的父类中的值
	                                     -- self 是调用者本身 保留父类方法需要用.来调用

end

local p1 = Player:New()
p1:Move()                             -- 这里打印 1，2

-- 不同对象使用的成员变量是相同的 
local p2 = Player:New()
p2:Move()                             -- 这里打印 2，3







