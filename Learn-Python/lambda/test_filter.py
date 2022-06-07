

# 和lambda实现同样的效果
def test(n):
    """判断给定的数字是不是奇数"""
    return n % 2 != 0


def use_filter(l):
    """
    获取指定列表/元组中的奇数
    :param l: list/tuple 要过滤的数据
    :return: 过滤好的奇数列表
    """
    # rest = filter(lambda n: n % 2 != 0, l)
    rest = filter(test, l)

    return rest


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    temp = use_filter(l)  # 得到的是一个filter对象
    print(temp)
    # 将对象强制转换成列表
    print(list(temp))
