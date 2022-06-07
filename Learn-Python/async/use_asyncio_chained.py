import asyncio


async def compute(x, y):
    # 这里不能用time.sleep休息，因为不能返回协程对象
    print("正在计算{0}+{1}的结果".format(x, y))
    await asyncio.sleep(1)
    return x + y


async def get_sum(x, y):
    # 在函数内耗时操作拿到结果用await
    result = await compute(x, y)
    print("{0}+{1}={2}".format(x, y, result))


# 拿到事件循环队列
loop = asyncio.get_event_loop()
loop.run_until_complete(get_sum(3, 5))

# # 注册任务
# task = loop.create_task(compute(3, 5))
# # 等待结束拿结果
# loop.run_until_complete(task)
