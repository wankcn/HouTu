import asyncio


async def do_sth(x):
    """定义协程函数"""
    print("等待中：{}".format(x))
    await asyncio.sleep(x)  # 有一个等待的过程


# 判断是否为协程函数
print(asyncio.iscoroutinefunction(do_sth))  # 括号内是函数名
# 拿到函数对象
coroutine = do_sth(5)
# 得到事件循环队列
loop = asyncio.get_event_loop()
# 加到事件循环队列 注册任务
task = loop.create_task(coroutine)
print(task)
# 等待协程任务执行结束 拿到结果
loop.run_until_complete(task)
print(task)
