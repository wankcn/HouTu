class PowNumber(object):
    """
    迭代器
    生成1，2，3，4，5...数字的平方
    当迭代完最后一个数据时，再调用next()或__next__()时，则会抛出StopIteration异常
    """
    value = 0  # 用类的属性临时保存值

    # 实现next方法是迭代器
    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration  # 停止
        return self.value ** 2  # 平方

    # 实现了__iter__()方法是可迭代的
    def __iter__(self):
        return self


if __name__ == '__main__':
    pow = PowNumber()
    # 1.调用迭代器里的__next__()方法
    # print(pow.__next__())
    # print(pow.__next__())
    # print(pow.__next__())
    # print(pow.__next__())

    # 2.使用python自带解释器迭代
    # print(next(pow))
    # print(next(pow))
    # print(next(pow))
    # print(next(pow))
    # 3.循环迭代器 循环的时候要限制迭代器的次数
    for i in pow:
        print(i)
