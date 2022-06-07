"""
    简单猜数游戏
    每猜测一次将结果写入创建的日志
    生成文件名record.txt
"""
import random
import sys
from datetime import datetime


def display():
    """展示游戏开始界面"""
    guide_word = "欢迎进入数字猜猜猜游戏"
    return "{0} {1} {2}".format('*' * 20, guide_word, '*' * 20)


def input_num():
    """输入区间的范围"""
    start = input("数字区间起始值：")
    end = input("数字区间终止值：")
    return [start, end]


def type_conversion(list_str):
    """
    str类型转换为int型的函数
    :param list_str: 包含str的列表
    :return: 包含int元素的list_int
    """
    # 将原列表类型转后存入新的列表
    list_int = []
    for i in list_str:
        i = int(i)
        list_int.append(i)
    return list_int


def num_equal(num_list):
    """判断输入的区间是否值相等"""
    if num_list[0] == num_list[1]:  # 如果值相等，重新输入新的区间
        print("您输入的区间数字相同！！请重新启动程序")
        return sys.exit()
    else:
        return 1


def determine_type(x):
    """
    确定猜测数字的类型
    :param x: 输入的数字
    :return:
    """
    if x.isdigit() is True:
        return int(x)
    else:
        return x


def whether_list(number, num_list):
    if num_list[0] <= number <= num_list[-1]:
        # print("输入的数字在区间范围内")
        return 0
    else:
        print("对不起您输入的数字未在指定区间!!!")
        return 1


def create_rand(num_list):
    """
    产生随机数
    :param num_list: 数字区间
    :return:产生的随机数
    """
    rand = random.randint(num_list[0], num_list[-1])
    # print("产生的随机数:{}".format(rand))
    return rand


def determine_size(enter_num, get_rand):
    if enter_num < get_rand:
        print("*************")
        print("Lower than the answer")
    elif enter_num == get_rand:
        print("*************")
        return 0
    elif enter_num > get_rand:
        print("*************")
        print("Higher than the answer")


def write_log(count, enter_num):
    """ 写入日志"""
    file_name = "record.txt"
    now_time = datetime.now()
    with open(file_name, "a+", encoding="utf-8") as f:
        f.write("{}：第{}次您猜测的数字为：{}\n".format(now_time, count, enter_num))


if __name__ == '__main__':
    # 展示信息
    print(display())
    # 获取区间
    list_temp = input_num()
    print("所产生的随机数字区间为：{}".format(list_temp))  # 按照如图效果显示str

    # 接受类型转换后的区间值
    new_list = type_conversion(list_temp)
    # print("类型转换后的区间：{}".format(new_list))

    # 判断区间的值是否相等
    num_equal(new_list)
    # 产生随机数
    rand = create_rand(new_list)
    i = 1
    while True:
        guess_num = input("请继续输入您猜测的数字：")

        # 接受符合数值类型结果
        num = determine_type(guess_num)
        # print(num)

        # 查看数字是否在区间里
        tag = whether_list(num, new_list)
        # 如果失误输入了不在区间里，重新输入不算在猜测次数里
        if tag == 1:
            continue
        # 判断输入数字与随机数的大小
        temp = determine_size(num, rand)
        # 记录日志
        write_log(i, num)
        if temp == 0:
            print("恭喜您！只用了{}次就赢得了游戏".format(i))
            break
        i += 1
