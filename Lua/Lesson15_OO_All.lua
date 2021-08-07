--- 面向对象的实现
--- 万物之父 所有对象的基类

Object = {}

function Object:New()
	local obj = {}
	self.__index = self
	setmetatable(obj,self)
	return obj
end

function Object:SubClass(className)
	_G[className] = {}
	local obj = _G[className]
	obj.base = self
	self.__index = self	
	setmetatable(obj,self)

end	