"""
使用python的迭代器和生成器模拟python内置的range函数
"""


def use_range():
    """python内置的range函数"""
    for i in range(5, 10):
        print(i)


class IterRange(object):
    """使用迭代器来模拟range()函数"""

    def __init__(self, start, end):
        """通过构造函数传范围的值"""
        self.start = start - 1

        self.end = end

    def __next__(self):
        self.start += 1
        if self.start >= self.end:
            raise StopIteration
        return self.start

    def __iter__(self):
        return self


class GenRange(object):
    """使用生成器模拟range函数"""

    def __init__(self, start, end):
        """通过构造函数传范围的值"""
        self.start = start - 1
        self.end = end

    def get_num(self):
        """
        生成数
        遇到yield程序会暂停执行，直到下次被唤醒，在执行一次
        """
        while True:
            if self.start >= self.end - 1:
                break
            self.start += 1
            yield self.start


def get_num(start, end):
    """用函数的方式使用生成器实现range函数"""
    start -= 1
    while True:
        if start >= end - 1:
            break
        start += 1
        yield start


if __name__ == '__main__':
    # use_range()

    iter_num = IterRange(5, 10)
    # print(next(iter_num))
    # print(next(iter_num))
    # print(next(iter_num))
    # print(next(iter_num))
    # print(next(iter_num))
    # 生成一个列表
    l1 = list(iter_num)
    print(l1)
    print("-----------------")
    gen = GenRange(5, 10).get_num()
    print(gen)  # 返回一个对象
    print(list(gen))  # 强制转换成列表形式

    print("-----------------")
    gen_temp = get_num(5, 10)
    print(gen)  # 返回一个对象
    print(list(gen_temp))
