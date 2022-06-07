"""
生成器是一种特殊的迭代器
"""


def pow():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


def pow_num():
    return (x * x for x in [1, 2, 3, 4, 5])


def pow_number():
    for x in [1, 2, 3, 4, 5]:
        yield x ** 2


if __name__ == '__main__':
    temp = pow()
    for i in temp:
        print(i)

    rest = pow_number()
    for i in rest:
        print(i)
