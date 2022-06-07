import threading

# 声明全局的锁 在一个线程里不能再锁，会造成死锁
my_lock = threading.Lock()
# 第二种类型的锁 在一个线程里可以锁自己,可以进行重复锁定
your_lock = threading.RLock()
# 我的银行账户
balance = 0


def change_it(n):
    """改变我的账户余额"""
    global balance
    with your_lock:
        balance += n
        balance -= n
        print("------------->{}".format(n))

    # try:
    #     # 添加锁
    #     my_lock.acquire()
    #     # 资源已经被锁住了,不能重复锁定
    #     # my_lock.acquire()  # 重复锁定造成四锁
    #     balance += n
    #     balance -= n
    #     print("------------->{}".format(n))
    # # 释放锁
    # finally:
    #     my_lock.release()


class ChangeBalanceThread(threading.Thread):
    """改变银行余额的现金"""

    def __init__(self, num, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.num = num

    def run(self):
        for i in range(1000):
            change_it(self.num)


if __name__ == '__main__':
    t1 = ChangeBalanceThread(5)
    t2 = ChangeBalanceThread(8)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    # 打印余额
    print("最后的余额{}".format(balance))
