import random
import time
from multiprocessing import Process, RLock


class WirteProcess(Process):
    """写入文件"""

    def __init__(self, file_name, num, lock, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 文件的名称
        self.file_name = file_name
        self.num = num
        # 锁对象
        self.lock = lock

    # def run(self):
    #     """写入文件的主要业务逻辑"""
    #     try:
    #         # 添加锁
    #         self.lock.acquire()
    #         print("locked")
    #         # 测试Rlock
    #         # 重复锁定 用lock产生死锁
    #         self.lock.acquire()
    #         print("relocked")
    #         for i in range(5):
    #             content = "现在是:{0}\n id:{1}--参数:{2}\n".format(
    #                 self.name,
    #                 self.pid,
    #                 self.num
    #             )
    #             with open(self.file_name, "a+", encoding="utf-8")as f:
    #                 f.write(content)
    #                 time.sleep(random.randint(1, 3))
    #                 print(content)
    #     finally:
    #         # 释放锁
    #         self.lock.release()

    ##########################################
    # 用with实现释放
    def run(self):
        """写入文件的主要业务逻辑"""

        # # 添加锁
        # self.lock.acquire()
        # print("locked")
        # # 测试Rlock
        # # 重复锁定 用lock产生死锁
        # self.lock.acquire()
        # print("relocked")
        with self.lock:
            for i in range(5):
                content = "现在是:{0}\n id:{1}--参数:{2}\n".format(
                    self.name,
                    self.pid,
                    self.num
                )
                with open(self.file_name, "a+", encoding="utf-8")as f:
                    f.write(content)
                    time.sleep(random.randint(1, 3))
                    print(content)

            # with不需要释放锁
            # self.lock.release()


if __name__ == '__main__':
    """开5条进程"""
    file_name = "test.txt"
    # 锁的对象
    # lock = Lock()
    lock = RLock()
    for x in range(5):
        p = WirteProcess(file_name, x, lock)
        p.start()
