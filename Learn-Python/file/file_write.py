from datetime import datetime
import random


def write_file():
    """写入文件"""
    file_name = "write_test.txt"
    # 打开文件以写入的方式
    f = open(file_name, "w")
    # 写入一行内容
    f.write("hello\nworld")
    f.close()


def writelines_file():
    """写入多行"""
    file_name = "writelines.txt"
    # 准备写入的列表
    l = ["第1行", '\n', "第2行", "第3行", "第4行", ]
    with open(file_name, "w") as f:
        f.writelines(l)


def write_user_log():
    """记录用户日志"""
    # 记录时间+id随机数
    temp = "用户：{0}-访问时间：{1}\n".format(random.randint(1000, 9999), datetime.now())
    file_name = "write_user_log.txt"
    with open(file_name, "a")as f:
        f.write(temp)


def read_write():
    """先读再写"""
    file_name = "read_write.txt"
    with open(file_name, "r+")as f:
        read_temp = f.read()
        # 如果存在1 就写一行，不存在写bbb，存在写aaa
        if '1' in read_temp:
            f.write("aaa")

        else:
            f.write("bbb")
        f.write('\n')


if __name__ == '__main__':
    # write_file()
    # writelines_file()
    # write_user_log()
    read_write()
