"""
    实现进程间通信
"""
import time
import random
from multiprocessing import Process, Queue, current_process


class WriteProcess(Process):
    """写的进程"""

    def __init__(self, q, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.q = q

    def run(self):
        """实现进程的业务逻辑"""
        # 要写的内容
        ls = [
            "第1行内容",
            "第2行内容",
            "第3行内容",
            "第4行内容"
        ]
        for line in ls:
            print("写入内容：{0}--{1}".format(line, current_process().name))
            self.q.put(line)
            # 每写入一次，休息1～5秒
            time.sleep(random.randint(1, 3))


class ReadProcess(Process):
    """读取内容的进程"""

    def __init__(self, q, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.q = q

    def run(self):
        # 写入的时候随机休息 这里一直读，有可能还没写就读了，所以作死循环的操作
        while True:
            content = self.q.get()
            print("读取到的内容:{0}--{1}".format(content, current_process().name))


if __name__ == '__main__':
    # 通过Queue共享数据
    q = Queue()
    t_wirte = WriteProcess(q)
    # 写入内容的进程
    t_wirte.start()
    # 读取进程启动
    t_read = ReadProcess(q)
    t_read.start()
    t_wirte.join()
    # t_read.join()

    # 因为读的进程是死循环，无法等待结束，只能强制终止
    t_read.terminate()
