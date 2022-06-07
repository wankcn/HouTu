"""
    使用try...except捕获所有异常
"""


def test_div(num1, num2):
    """当除数为0的时候"""

    return num1 / num2


def test_file():
    """读取文件"""
    try:
        f = open('test.txt', 'r', encoding='utf-8')
        rest = f.read()
        print(rest)
    except:
        print(rest)
    finally:
        f.close()
        print('closed')


if __name__ == '__main__':
    # 异常捕获的过程
    try:
        temp = test_div(5, 0)  # 此时会报错
        print(temp)
    # except ZeroDivisionError:
    #     # 如果报了错会执行except里的代码
    #     print('报错了，除数不能为0')
    # except TypeError:
    #     print('报错了，请输入数字')
    except(ZeroDivisionError, TypeError) as e:  # 集中式处理
        print('Error!!!!')  # 有助于排查信息
        print(e)  # 不知道报什么错，把错误打印
    finally:
        print('最后必须执行')

    test_file()
