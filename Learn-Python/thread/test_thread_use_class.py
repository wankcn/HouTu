import threading
import time


class LoopThread(threading.Thread):
    """ 自定以线程 """
    n = 0
    # run里线程要做的东西
    def run(self):
        while self.n < 5:
            print(self.n)
            now_thread = threading.current_thread()
            print("正在执行的线程名称:{}".format(now_thread.name))
            time.sleep(1)
            self.n += 1


if __name__ == '__main__':
    # 当前正在执行的线程
    now_thread = threading.current_thread()
    print("正在执行的线程名称:{}".format(now_thread.name))
    t = LoopThread(name="loop_thread")
    t.start()
    t.join()
