
print("\n//--------------------  类和结构体")

-- lua中默认没有面向对象 需要自己实现
-- 成员变量，成员函数，各种属性

Student={
	
	age =1,      -- 年龄
	sex="男",    -- 性别
	Up = function()   
		-- lua中， 打印的age和Student表中的age没有任何关系 它是一个全局变量
		print(age)
		-- 如果使用过age 在表内部函数中，使用本身的属性和方法，一定指定是谁的
		print(Student.age)
		print("我成长")
	end,
	
	Learn = function(t)
		-- 第二种能够在函数内部 把自己作为参数传进来 在内部访问
		print(t.sex)
		print("好好学习")
	end
}
-- Lua中类的表现，更像是一个类中有很多的静态变量和函数
Student.Up()

-- 声明表之后，可以在外部声明表的变量和方法
Student.name = "wenruo"
Student.Speak = function() 
	print("说话") 
end
Student.Speak()

function Student.Eat()            -- 函数的第三种声明方式
	print("吃吃吃")
end
Student.Eat()

Student.Learn(Student)  -- 传入参数，打印的其实是自身的t.sex
Student:Learn()         -- 冒号的写法也是打印了相同的内容

-- Lua中点和冒号的区别   .调用有什么参数传什么参数
-- 使用冒号调用方法 会默认把调用者作为第一个参数传入方法中
-- 内部声明没法写冒号，一定是在外部

function Student : Speak2()
	-- lua中 有一个关键字 self 表示默认传入的第一个参数 
	print(self.name.."说话")
	
end

Student:Speak2()

print("\n//--------------------  表的公共操作")

tab = {{age=1,name="123"},{age = 2,name="456"}}
tab2 = {age =3,name = "789"}

-- 插入表
print("之前的长度"..#tab)
table.insert(tab,tab2)
print("之后的长度"..#tab)

print(tab[1].age)
print(tab[2].name)

-- 删除指定元素  传入表 移除表最后一个索引的内容
table.remove(tab)
print(#tab)
table.remove(tab,1)  -- 传入两个参数，第一个是要移除的表，第二个参数移除的内容的索引
print(tab[1].name)  


-- 排序 默认升序
t={1,5,4,6,8,7,9,2}
table.sort( t)
print("排序一下------")
for k,v in pairs(t) do
	print(v)
end 

-- 降序 添加规则
table.sort( t, function(a,b)
	if a>b then
		return true
	end
end )
print("打印看一下是否排序为降序")
for _,v in pairs(t) do
	print(v)
end 

-- 拼接元素 返回值为一个字符串 使用较少
t1 = {"111","222","333","444","555"}
str = table.concat( t1, "; ",1,2)
print(str)

print("\n\n\n\n\n")