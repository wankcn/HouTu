print("\n//--------------------  协程（协同程序）")

print("\n//--------------------  协程创建")
-- 第一种 常用方式
fun = function()
	print("这是一个create创建的协程函数")
end

fun2 = function()
	print("这是一个warp创建的协程函数")
end

-- 创建协程有返回值，需要声明一个变量存储它 类型是一个线程对象
-- 协程的本质是一个线程对象
co = coroutine.create(fun)
print(co,type(co))

-- 第二种创建方法 返回是一个函数
co2 = coroutine.wrap(fun2)
print(co2,type(co2))


print("\n//--------------------  协程运行")
-- 第一种方式，对应create()创建的协程
coroutine.resume(co)    -- 传入线程对象
-- 第二种方式
co2()                   -- 因为是一个函数，可以直接调用

print("\n//--------------------  协程挂起")
fun3 = function()
	local i = 1
	while true do
		print(i)
		i = i+1
		-- 协程挂起的函数
		coroutine.yield() 
	end
end

co3 = coroutine.create(fun3)
coroutine.resume(co3)	 -- 死循环只打印了一次i c#一直执行
coroutine.resume(co3)    -- 每重新启动一次协程，相当于在循环里跑了一次
-- lua中，脚本从上到下执行一次n，重启协程才继续执行一次
-- 当执行到协程挂起的时候，即暂停了。只有重启的时候才会重新从暂停的地方往下继续执行

print("第2种函数执行协程")
-- 另一种创建方式
co4 = coroutine.wrap(fun3)
co4()
co4()
co4()

-------------------------
-- yeild可以带返回值
print("----- yeild可以带返回值")
fun4 = function()
	local i = 1
	while true do
		print(i)
		i = i+1
		-- 协程挂起的函数
		coroutine.yield(i) -- yield可以有返回值
	end
end
co5 = coroutine.create(fun4)
-- 多个返回值接收，第一个是bool，协程是否启动成功 第二个是yield里面的返回值
isOK,tempI = coroutine.resume(co5)
print(isOK,tempI)
isOK,tempI = coroutine.resume(co5)
print(isOK,tempI)
isOK,tempI = coroutine.resume(co5)
print(isOK,tempI)
print("---使用Wrap返回")
co6 = coroutine.wrap(fun4)
-- 使用wrap方式的协程调用，有返回值，没有默认第一个返回值
print("返回值是："..co6())
print("返回值是："..co6())
print("返回值是："..co6())


print("\n//--------------------  协程状态")



