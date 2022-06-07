from functools import reduce


def get_sum(l):
    """
    根据给定的列表，求里面各个数字的总和
    :param l: list/tuple
    :return: 列表所以项的和
    """
    sum = 0
    for i in l:
        sum += i
    return sum


def use_py(l):
    """ 使用内置函sum数进行求和"""
    return sum(l)


def f(m, n):
    """求两数的和"""
    return m + n


def use_reduce(l):
    """
    使用reduce进行求和
    :param l:
    :return:
    """
    return reduce(f, l)


def use_lambda(l):
    """
    使用lambda表达式
    """
    return reduce(lambda m, n: m + n, l)


if __name__ == '__main__':
    list1 = [1, 2, 4, 6, 7, 8, 9]
    temp = get_sum(list1)
    print(temp)
    print("-" * 10, "分割线", "-" * 10)
    temp1 = use_py(list1)
    print(temp1)
    print("-" * 10, "分割线", "-" * 10)
    temp2 = use_reduce(list1)
    print(temp2)
    print("-" * 10, "分割线", "-" * 10)
    temp3 = use_lambda(list1)
    print(temp3)  # 返回的是int型 不是对象
