"""
    求0-50以内（包括50）的偶数
"""


def use_filter(data):
    # 使用result接收filter过滤偶数值的功能
    result = filter(lambda n: n % 2 == 0, data)
    return result


if __name__ == '__main__':
    # 使用data接收0-50的数值
    data = range(0, 51)
    # 调用use_filter函数传入data,使用result变量接收
    result = use_filter(data)
    print(list(result))
