# 定义一个队列
# 两个协程进行通信
# 其中一个往队列中写入数据
# 另一个从队列中删除数据
import asyncio
import random


async def add(store, name):
    """
    写入数据到队列
    :param store: 队列的对象
    """
    for i in range(5):
        # 往队列中添加数字
        num = "{}--{}".format(name, i)

        # 随机休息1-3秒
        await asyncio.sleep(random.randint(1, 3))
        # put得到的是一个协程的对象 先休息在添加
        await store.put(i)
        print("{2}写入数字{0},队列的大小{1}".format(i, store.qsize(), name))


async def reduce(store):
    """
    从队列中删除数据
    :param store: 队列的对象
    """
    for i in range(10):
        result = await store.get()
        print("删除的对象{0},队列此时大小{1}".format(result, store.qsize()))


if __name__ == '__main__':
    # 准备一个队列
    store = asyncio.Queue(maxsize=5)
    # 得到三个协程对象
    a1 = add(store, "a1")
    a2 = add(store, "a2")
    r1 = reduce(store)

    # 添加到事件队列
    loop = asyncio.get_event_loop()
    # 通过gather收集三个对象
    loop.run_until_complete(asyncio.gather(a1, a2, r1))
    # 关掉loop
    loop.close()
