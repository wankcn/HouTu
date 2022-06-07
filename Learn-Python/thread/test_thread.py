import threading
import time


def loop():
    """新的线程执行代码"""

    n = 0
    while n < 5:
        now_thread = threading.current_thread()
        print("正在执行的线程名称:{}".format(now_thread.name))
        time.sleep(1)  # 假如延时
        n += 1


def use_thread():
    """使用线程"""
    # 当前正在执行的线程 current_thread 获取当前正在执行线程的名称
    now_thread = threading.current_thread()
    print("正在执行的线程名称:{}".format(now_thread.name))
    # target 要执行的函数   name名称
    t = threading.Thread(target=loop, name="loop_thread")

    # 启动线程
    t.start()
    # 挂起线程
    t.join()


if __name__ == '__main__':
    use_thread()
