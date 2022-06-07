def read_file():
    """ 读取文件 """
    file_name = 'test.txt'
    # 使用绝对路径
    file_path = "/Users/wankcn/Desktop/PythonCode/python-project/file/test.txt"

    # 打开文件
    # f = open(file_name, encoding="utf-8")
    with open(file_name, encoding="utf-8") as f:
        # 读文件内容
        # rest = f.read()
        # 读取指定的几个内容
        rest = f.read(8)  # 读取8个字符
        print(rest)
        print(f.read(8))  # 再接着读取8个字符

        print("-------------------------------")
        # # 随机读取
        # f.seek(20)
        # print(f.read(5))    # 解决英文字符
        print("-------------------------------")
        # 按行读取
        temp = f.readline()
        print(temp)
        print("-------------------------------")
        temp_all = f.readlines()  # 读取全部内容存放进列表当中
        print(temp_all)
        # 关闭文件
        # f.close()


if __name__ == '__main__':
    read_file()
