# python实现进程
import os
import time
from multiprocessing import Process


def do_sth(name):
    """
    进程要做的事情
    :param name: str 进程的名称
    """
    print("进程名称:{0}\nPID:{1}".format(name, os.getpid()))
    time.sleep(5)
    print("进程要做的事情")


class MyProcess(Process):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name  # 这里要写my_name  name已经在父类里用过了

    def run(self):
        print("MyProcess进程名称:{0}\nPID:{1}".format(self.name, os.getpid()))
        time.sleep(5)
        print("MyProcess进程要做的事情")


if __name__ == '__main__':
    # p = Process(target=do_sth, args=("my process",))
    # p.start()
    # p.join()
    p = MyProcess(name="my_process_class")
    p.start()
    p.join()
