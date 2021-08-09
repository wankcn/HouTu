--- 自带库

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