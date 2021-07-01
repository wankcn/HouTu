print("\n//--------------------  循环语句  --------------------//")

print("\n//--------------------  while语句")
num = 0
while num<5 do
	print(num)
	num= num+1
end


print("\n//--------------------  repeat...until循环 (do while)语句")
-- repeat ...until 条件（！条件是结束条件）
num=0
repeat 
	print(num)
	num=num+1

until num>=5 -- 结束条件


print("\n//--------------------  for语句")

for i =1, 5 do -- lua中默认
	print(i)
end

for i =1, 5, 2 do  -- 2是步长
	print(i)
end

for i =10, 5, -2 do  -- 2是步长
	print(i)
end






print("\n\n\n\n\n")