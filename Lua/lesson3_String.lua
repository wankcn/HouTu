print("\n//---------------------------------------------  String")
str = '单引号字符串'
str2= "双引号双引号"

print(str,str2)

-- 获取字符串长度 前面加#号 
print("\n//---------------------------------------------  字符串长度")
s = "asdfwEr"
print(#s)
-- 中文字符占3个长度
s1 = "文若"
print(#s1)


print("\n//---------------------------------------------  字符串多行打印")
-- lua支持转义字符
print("123\n123")
-- 使用[[]]
s =[[
中国加油
我辈自强
]]
print(s)

print("\n//---------------------------------------------  字符串拼接")
print("123".."456")
s=123 s2=456
print(s..s2)

print(string.format("小猫今年%d了",18))
-- %d 与数字拼接
-- %a 与任何字母拼接
-- %s 与字符拼接 等等

print("\n//---------------------------------------------  其他类型转字符串")
a = true
print(tostring(a))

print("\n//---------------------------------------------  字符转方法")
str = "asdFgHjkLsdHIJKLer"
-- 小写转大写
print(string.upper(str))
print(str)  -- 不会改变原有字符串
-- 大写转小写
print(string.lower(str))
-- 翻转字符串 
print(string.reverse(str))
-- 字符串索引查找
print(string.find(str,"dFgH"))  -- 开始到结束的索引
-- 截取字符串
print(string.sub(str,3))        -- 从3的位置开始截取
print(string.sub(str,3,6))      -- 截取3-6之间
-- 字符串重复
print(string.rep(str,2))        -- 重复两次
-- 字符串修改
print(string.gsub(str,"sd","***"))  -- 返回后面有一个修改次数

-- 字符转ASCII
x = string.byte("Lua",1)
print(x)                        -- 把第一个字符转换成ASCII
-- ASCII转字符串
print(string.char(x))           -- 转回L
 














print("\n\n\n\n\n")

