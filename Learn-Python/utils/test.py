from datetime import datetime

from trans.tools import get_trans_id
# from work.tools import get_file_type
import work

def test_trans_tool():
    """
    测试trans下tool模块
    """
    id1 = get_trans_id()
    print(id1)
    date = datetime(2015, 10, 2, 12, 30, 45)
    id2 = get_trans_id(date)
    print(id2)


def test_work_tool():
    """测试work模块"""
    file_name = "/Users/wankcn/Desktop/Screen.png"
    rest = work.tools.get_file_type(file_name)
    # rest = get_file_type(file_name)
    print(rest)


if __name__ == '__main__':
    test_trans_tool()
    test_work_tool()
