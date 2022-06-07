def pow_number(l):
    """
    根据给定的列表数据，计算里面每一项的立方
    :param l:  列表/元组 int类型
    :return: 原来列表中的每一项的立方
    """
    rest = []
    for x in l:
        rest.append(x ** 3)
    return rest


def f(n):
    return n ** 3


def use_map(l):
    """
    使用map函数计算
    :param l:  列表/元组 int类型
    :return: 原来列表中的每一项的立方
    """
    return map(f, l)


def use_map_lambda(l):
    """
    使用map函数计算/lambda表达式
    :param l:
    :return:
    """
    return map(lambda n: n ** 3, l)


if __name__ == '__main__':
    a = [1, 2, 3]
    temp = pow_number(a)
    print(temp)
    print("-----------------------------")
    temp1 = use_map(a)
    print(list(temp1))
    print("-----------------------------")
    temp2 = use_map_lambda(a)
    print(list(temp2))
