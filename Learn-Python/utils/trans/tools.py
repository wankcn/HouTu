import random
from datetime import datetime


def get_trans_id(date=None):
    """
    根据所传入的时间得到一个唯一的交易流水id
    :param date_time: 日期
    :return:交易流水的字符串
    """
    # 如果没有传入时间，则使用系统当前的时间
    if date is None:
        date = datetime.now()
    # 怎样保证字符串唯一
    # 日期+时间+毫秒+随机数（6位随机数）
    return date.strftime("%y%m%H%M%S%f") + str(random.randint(100000, 999999))
