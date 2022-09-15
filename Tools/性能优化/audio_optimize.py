# Author: 文若 
# CreateDate: 2022/9/15

"""
Audio_Optimize 优化工具
"""

import os
import os.path
from shutil import copyfile

# Unity工程目录，注意后面有个"/"
ProjectDir = "/Users/wankcn/Desktop/Suntail_Village_Optimization/"
# 文本文件目录 需要拷贝性能报告到文本里 我这里命名为audio.txt
TextPath = ProjectDir + "Assets/WRHelper/OtherTxt/audio_compressedInMemory "   
# 源文件备份目录
BackUpDir = ProjectDir + "BackUp/"

# 测试文件
TestFile = "Assets/Suntail Village/Audio/Enviroment/Items/Item_Food_Large_2.wav"


def read_file(src_path):
    """全文读取"""
    # if os.path.isfile(src_path) and os.path.splitext(src_path)[-1].lower() == '.txt':
    if os.path.isfile(src_path):
        with open(src_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            # 需要去掉"\n"
            for i in range(len(lines)):
                lines[i] = lines[i].rstrip()
        return lines
    else:
        return None


def read_file2(src_path):
    """行读取"""
    lines = []
    if os.path.isfile(src_path):
        with open(src_path, 'r', encoding='utf-8') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                lines.append(line.strip())  # 必要步骤
        return lines
    else:
        return None


def get_audiofile_data(full_src_path):
    """获取的文件内容"""
    # 内容存入字典 {name:[索引,前半段,后半段]} 用：分割
    dic = {}
    files = read_file(full_src_path)
    for i in range(len(files)):
        strs = files[i].split(':')
        key = strs[0].strip()
        dic[key] = [i, strs[0], strs[1]]
    return dic


def copy_file(source_path):
    if not os.path.exists(BackUpDir):
        os.makedirs(BackUpDir)
        print(">> 指定的备份目录不存在，创建完成 >>")

    # 拷贝一份源meta文件到新目录中
    new_file_name = source_path.split('/')[-1]
    new_path = BackUpDir + new_file_name

    if not os.path.exists(new_path):
        print(">>【备份完成】 {0}".format(new_path))
        copyfile(source_path, new_path)
    else:
        print(">>【文件已存在】终止操作！！地址为: {1}".format(new_file_name, new_path))


def write_file(file_name, data):
    with open(file_name, "w", encoding="utf-8") as f:
        for k, v in data.items():
            f.write(v[1] + ':' + v[2] + "\n")
    print(">>【写入完成】{0}".format(file_name))


def opt_force_to_mono(data):
    """对文本内容进行处理 代码还可以再优化"""
    rate = data['sampleRateOverride'][2]
    # 修改音频采样率
    if int(rate) >= 22050:
        data['sampleRateOverride'][2] = " 22050"
        data['sampleRateSetting'][2] = " 2"

    # 勾选ForeToMono
    data['forceToMono'][2] = " 1"
    return data


def opt_compressed_in_memory(data):
    data['loadType'][2] = " 1"
    return data


def opt_streaming(data):
    data['loadType'][2] = " 2"
    return data


def opt_file(file_name):
    # 拼接目录，修改AudioClip.meta
    full_src_path = os.path.join(ProjectDir, file_name + ".meta")

    # 文件备份
    copy_file(full_src_path)

    # 数据结构
    dic = get_audiofile_data(full_src_path)

    # 修改数据
    # data = opt_force_to_mono(dic)
    # data = opt_compressed_in_memory(dic)
    data = opt_streaming(dic)

    # 写入数据
    write_file(full_src_path, data)


def opt(path):
    files = read_file(path)
    for f in files:
        opt_file(f)


if __name__ == '__main__':
    opt(TextPath)
