print("\n//--------------------  字典声明")
-- 字典是键值对
a={["name"] = "wenruo",["age"]= 16,["1"]=5}

print(a["name"],a["age"],a["1"])

-- 可以类似 .成员变量得到值
print(a.name,a.age)

-- 不可以a.1 不可以数字 只能通过a.["1"]
-- print(a.1)


-- 修改
a.name = "wank"
print(a["name"])

-- 新增
a.sex = "女"
print(a["sex"])


-- 删除 让它等于空
a.sex = nil
print("del:",a["sex"])
a.sex = "男"


print("\n//--------------------  字典遍历")
for k,v in pairs(a) do
	print(k..":"..v)
end

for k,v in pairs(a) do
	print(k.."///"..a[k])
end
print("\n-----只遍历值")
for _,v in pairs(a) do
	print(v)
end






print("\n\n\n\n\n\n")

