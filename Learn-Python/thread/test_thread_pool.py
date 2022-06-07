import threading
import time
from concurrent.futures.thread import ThreadPoolExecutor
from multiprocessing.dummy import Pool


def run(n):
    """线程要做的事情"""
    time.sleep(1)
    print(threading.current_thread().name, n)


def main():
    """使用传统的方法来做任务"""
    t1 = time.time()
    for n in range(100):
        run(n)
    print(time.time() - t1)


def use_thread_main():
    """使用线程优化任务"""
    ls = []
    t1 = time.time()
    for count in range(10):
        # 资源有限最多跑10个线程
        for i in range(10):
            t = threading.Thread(target=run, args=(i,))
            ls.append(t)
            t.start()
        for l in ls:
            l.join()
    print(time.time() - t1)


def use_pool_main():
    """使用线程池优化"""
    n_list = range(100)
    t1 = time.time()
    pool = Pool(10)
    pool.map(run, n_list)
    pool.close()
    pool.join()
    print(time.time() - t1)


def use_executor_main():
    """
        使用另一种线程池方法优化
        使用 ThreadPoolExecutor 来优化
    """
    n_list = range(100)
    t1 = time.time()
    with ThreadPoolExecutor(max_workers=10) as executor:  # 支持多大的池子
        # 批量加
        executor.map(run, n_list)
    print(time.time() - t1)


if __name__ == '__main__':
    # main()
    # use_thread_main()
    # use_pool_main()
    use_executor_main()
