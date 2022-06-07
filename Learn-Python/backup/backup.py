import os
import os.path


class FileBackup(object):
    """文本文件备份"""

    def __init__(self, src, dist):
        """
        构造方法
        :param src:  需要备份的文件目录
        :param dist: 备份后的目录
        """
        self.src = src
        self.dist = dist

    def read_files(self):
        """
        读取src目录下的所有文件
        :return:
        """
        ls = os.listdir(self.src)
        print(ls)  # 查看一下当前目录所有的文件
        for l in ls:
            # 循环处理每一个文件
            self.backup_file(l)

    def backup_file(self, file_name):
        """
        处理备份
        :param file_name: 文件/文件夹的名称
        :return:
        """

        # 1、判断dist目录是否存在，如果不存在，创建目录
        if not os.path.exists(self.dist):
            os.makedirs(self.dist)
            print("指定的目录不存在，创建完成")
        # 2、判断文件是否为我们要备份
        # 得到的是文件名 拼接文件的完整路径
        full_src_path = os.path.join(self.src, file_name)
        full_dist_path = os.path.join(self.dist, file_name)
        # 首先判断是否为文件夹，然后借助文件后缀名判断
        if os.path.isfile(full_src_path) and os.path.splitext(full_src_path)[-1].lower() == '.txt':
            # print(full_src_path)  # 打印看一下要备份的文件完整目录
            with open(full_dist_path, 'w', encoding='utf-8')as f_dist, \
                    open(full_src_path, 'r', encoding='utf-8')as f_src:
                print(">>开始备份【{0}】".format(file_name))
                # 3、读取文件内容
                while True:
                    rest = f_src.read(100)
                    if not rest:
                        break
                    # 4、把读取到的内容写入新的文件中
                    f_dist.write(rest)
                f_dist.flush()  # 把剩余没写进去的全部写出去
                print(">>【{0}】备份完成".format(file_name))

        else:
            print("文件类型不符合要求，跳过>>")


if __name__ == '__main__':
    # # 要备份的文件目录地址
    # src_path = '/Users/wankcn/Desktop/PythonCode/python-project/src'
    # # 备份后的目录地址
    # dist_path = '/Users/wankcn/Desktop/PythonCode/python-project/dist'

    # 当前代码的目录名称
    base_path = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(base_path, 'src')  # 目录拼接
    dist_path = os.path.join(base_path, 'dist')
    print(src_path)
    print(dist_path)
    bak = FileBackup(src_path, dist_path)
    bak.read_files()


