# -*- encoding=utf-8 -*-

import time

from ThreadPool import task, pool


# 定义自己的任务
class SimpleTask(task.Task):
    def __init__(self, callable):
        super(SimpleTask, self).__init__(callable)

# 处理逻辑
def process():
    time.sleep(1)
    print('This is a SimpleTask callable function 1.')
    time.sleep(1)
    print('This is a SimpleTask callable function 2.')


def test():
    # 1. 初始化一个线程池
    test_pool = pool.ThreadPool()
    test_pool.start()
    # 2. 生成一系列的任务
    for i in range(10):
        simple_task = SimpleTask(process)
        # 3. 往线程池提交任务执行
        test_pool.put(simple_task)


def test_async_task():
    def async_process():
        num = 0
        for i in range(100):
            num += i
        return num

    # 1. 初始化一个线程池
    test_pool = pool.ThreadPool()
    test_pool.start()
    # 2. 生成一系列的任务
    for i in range(10):
        async_task = task.AsyncTask(func=async_process)
        test_pool.put(async_task)
        result = async_task.get_result()
        print('Get result: %d' % result)


# 测试是否可以正在的等待(wait)
def test_async_task2():
    def async_process():
        num = 0
        for i in range(100):
            num += i
        time.sleep(5)
        return num

    # 1. 初始化一个线程池
    test_pool = pool.ThreadPool()
    test_pool.start()
    # 2. 生成一系列的任务
    for i in range(1):
        async_task = task.AsyncTask(func=async_process)
        test_pool.put(async_task)
        print('get result in timestamp: %d' % time.time())
        result = async_task.get_result()
        print('Get result in timestamp: %d: %d' % (time.time(), result))


# 测试没有等待是否也可以正常获取结果
def test_async_task3():
    def async_process():
        num = 0
        for i in range(100):
            num += i
        return num

    # 1. 初始化一个线程池
    test_pool = pool.ThreadPool()
    test_pool.start()
    # 2. 生成一系列的任务
    for i in range(1):
        async_task = task.AsyncTask(func=async_process)
        test_pool.put(async_task)
        print('get result in timestamp: %d' % time.time())
        # time.sleep(5)
        # 转而去处理别的逻辑
        result = async_task.get_result()
        print('Get result in timestamp: %d: %d' % (time.time(), result))


if __name__ == '__main__':
    test()
    # test_async_task()
    # test_async_task2()
    # # test_async_task3()
