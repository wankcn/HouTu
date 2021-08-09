--- 自带库

-- /////////////////////////////////// [ 时间 ] ///////////////////////////////////

local time = os.time()
print("当前时间：",time)

-- 根据年月日转换时间
local time2 = os.time({year = 2021,month= 8, day = 8})
print(time2)


local nowTime = os.date("*t")

for k ,v in pairs(nowTime) do
	print(k,v)
end

print(os.date("%Y-%m-%d, %H:%M:%S",os.time()))

-- /////////////////////////////////// [ 数学运算 ] ///////////////////////////////////
-- math公共类
-- 绝对值
print("abs绝对值：",math.abs(-11))

-- 弧度转角度
print("弧度转角度：",math.deg(math.pi))

-- 三角函数 传弧度
print(math.cos(math.pi))

-- 向上取整，向下取整
print(math.floor(2.6))
print(math.ceil(2.6))

-- 最大值最小值
print(math.max(1,2))
print(math.min(4,5))

-- 把小数分成整数和小数
print(math.modf(3.4))
-- 幂运算
print(math.pow(2,5))

-- 随机数
-- 先设置随机数种子
math.randomseed(os.time())
print(math.random(100))

-- 平方根
print(math.sqrt(4))

-- /////////////////////////////////// [ 路径 ] ///////////////////////////////////
-- lua脚本加载路径 基本用不到
print(package.path)
package.path = package.path..";/usr/local/lib/lua/5.4"
print(package.path)













