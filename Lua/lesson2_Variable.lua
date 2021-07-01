print("\n//---------------------------------------------  变量")

-- lua中的简单 变量类型
-- nil boolean number string
-- 复杂数据类型：函数 table userdata 协同程序（线程）

-- lua中的变量可以随便赋值
-- lua中所有的变量声明，会自动判断变量类型 类似var
a = nil  -- nil类似空
print(type(a),a) 

-- 所有的数值都是number
a = 1 
print(type(a),a) 

-- string 字符串声明是由于双引号或单引号声明 没有char
a = "123"
print(type(a),a) 

a  = true
print(type(a),a) 

-- 通过type()函数可以得到变量类型 type函数返回值是string
print(type(type(a)))

-- 没有赋值过的变量b   nil lua中使用没有声明过的变量 不会报错 默认nil
print(b)









print("\n\n\n\n\n")
