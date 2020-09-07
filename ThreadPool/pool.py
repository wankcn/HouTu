# -*- encoding=utf-8 -*-


import psutil
import threading

from ThreadPool.task import Task, AsyncTask
from ThreadPool.queue import ThreadSafeQueue


# 任务处理线程
class ProcessThread(threading.Thread):

    def __init__(self, task_queue, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        # 线程停止的标记
        self.dismiss_flag = threading.Event()
        # 任务队列（处理线程不断从队列取出元素处理）
        self.task_queue = task_queue
        self.args = args
        self.kwargs = kwargs

    def run(self):
        while True:
            # 判断线程是否被要求停止
            if self.dismiss_flag.is_set():
                break
            task = self.task_queue.pop()
            # 不是定义的任务对象
            if not isinstance(task, Task):
                continue
            # 执行task实际逻辑（是通过函数调用引进来的）
            result = task.callable(*task.args, **task.kwargs)
            # 判断当前执行任务是否为AsyncTask
            if isinstance(task, AsyncTask):
                task.set_result(result)

    def dismiss(self):
        self.dismiss_flag.set()

    def stop(self):
        self.dismiss()


# 线程池
class ThreadPool:

    def __init__(self, size=0):
        if not size:
            # 约定线程池的大小为CPU核数的两倍（最佳实践）
            size = psutil.cpu_count() * 2
        # 线程池
        self.pool = ThreadSafeQueue(size)
        # 任务队列
        self.task_queue = ThreadSafeQueue()

        for i in range(size):
            self.pool.put(ProcessThread(self.task_queue))

    # 启动线程池
    def start(self):
        for i in range(self.pool.size()):
            thread = self.pool.get(i)
            thread.start()

    # 停止线程池
    def join(self):
        for i in range(self.pool.size()):
            thread = self.pool.get(i)
            thread.stop()  # 发生停止标记
        # 清空线程池
        while self.pool.size():
            thread = self.pool.pop()  # 不为空pop出来
            thread.join()  # 等待线程真正的停止

    # 往线程池提交任务
    def put(self, item):
        if not isinstance(item, Task):
            raise TaskTypeErrorException()
        self.task_queue.put(item)

    # 批量提交
    def batch_put(self, item_list):
        # 先判断是否为列表
        if not isinstance(item_list, list):
            item_list = list(item_list)
        for item in item_list:
            self.put(item)

    def size(self):
        # 已经是线程安全的队列，不需要再次保护
        return self.pool.size()


class TaskTypeErrorException(Exception):
    pass
