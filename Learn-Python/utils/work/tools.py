import os.path
import contants as f


def get_file_type(file_name):
    """
    根据文件的名称来判断文件的类型
    :param file_name:str文件名称
    :return:int 文件类型
    0 图片类型文件
    1 文档
    2 excel文档
    3 ppt文档
    -1 位置文件类型
    """
    # 默认文件是未知类型
    result = -1
    if not os.path.isfile(file_name):
        return f.FILE_TYPE_UNKNOWN

    path_name, ext = os.path.splitext(file_name)
    # 将后缀名统一为小写
    ext = ext.lower()
    # 图片类型文件
    if ext in ('.jpg', '.png', '.bmp', '.gif'):
        result = f.FILE_TYPE_IMG
    # word文档
    elif ext in ('.doc', '.docx'):
        result = f.FILE_TYPE_DOC
    # excel表格
    elif ext in ('.xls', '.xlsx'):
        result = f.FILE_TYPE_EXL
    # ppt文件
    elif ext in ('.ppt', '.pptx'):
        result = f.FILE_TYPE_PPT

    return result
