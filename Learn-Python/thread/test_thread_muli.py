import threading
import time

# 我的银行账户
balance = 0


def change_it(n):
    """改变我的账户余额"""
    global balance
    balance += n
    time.sleep(2)
    balance -= n
    time.sleep(1)
    print("-----N--{0};-------->{1}".format(n, balance))
    # 释放锁
    # my_lock.release()


class ChangeBalanceThread(threading.Thread):
    """改变银行余额的线程"""

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
    print("余额{}".format(balance))
