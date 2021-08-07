# Author: WenRuo
# CreateDate: 2021/8/4
import os


class TidyRes(object):

    def __init__(self, res, dep):
        """
        :param res:  需要备份的文件目录
        :param dep: 备份后的目录
        """
        self.res = res
        self.dep = dep

    @staticmethod
    def make_folders(folder):
        folder = os.path.exists(folder)
        if not folder:
            print(">>开始创建目录【{0}】".format(folder))
            os.makedirs(folder)
        else:
            print("文件夹已存在")

    def read_txt(self, path):
        name = path.split("/")
        name_list = []
        print(">> 开始读取文件: {0}".format(name[-1]))
        # 文件存在且为txt
        if os.path.exists(path) and os.path.splitext(path)[-1].lower() == '.txt':
            with open(path, 'r', encoding='utf-8')as f_src:
                lines = f_src.readlines()
                for line in lines:
                    temp = line.split("/")[-1]
                    # print(temp)
                    if "PanelModule" in temp:
                        temp = temp.replace(" ", "").split("(")[0]
                        self.make_dirs(temp)

        else:
            print("非法文件！文件读取失败！")
        for i in name_list:
            print(i)

    def make_dirs(self, folder_name):
        res_name = self.res + "/" + folder_name
        os.makedirs(res_name)
        dep_name = self.dep + "/" + folder_name
        os.makedirs(dep_name)
        os.makedirs(dep_name + "/Images")
        os.makedirs(dep_name + "/Anims")


if __name__ == '__main__':
    res_path = "/Users/wankcn/Desktop/Test/Res"
    dep_path = "/Users/wankcn/Desktop/Test/ResDep"
    image_path = res_path + "/Images"
    anims_path = res_path + "Anims"
    txt_path = "/Users/wankcn/Desktop/活动out.txt"

    tidy = TidyRes(res_path, dep_path)
    tidy.read_txt(txt_path)
    print(os.getcwdb())
