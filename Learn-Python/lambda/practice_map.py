def use_map(data):
    # 使用result接收map实现各个元素的5次方功能
    result = map(lambda n: n ** 5, data)
    return result


if __name__ == '__main__':
    data = (2, 4, 6, 8, 10, 12)
    # 调用use_map函数传入data，使用result接收
    result = use_map(data)
    print(tuple(result))
