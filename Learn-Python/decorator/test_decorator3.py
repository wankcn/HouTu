"""
带参数的装饰器
在外边嵌套一层装饰器的参数可以用

有些函数带参数 定义内部装饰器的时候需要传进去
如果函数返回值，内部装饰器先临时保存结果，最后在返回
"""


def log(name=None):
    """记录函数执行的日志"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            print("{0} start...".format(name))
            temp = func(*args, **kwargs)  #用临时变量保存结果返回 add函数有返回
            print("{0} end.".format(name))
            return temp

        return wrapper

    return decorator


@log('you')  # 这里需要传参数 不传默认None
def hello():
    """简单功能模拟"""
    print("hello world")


@log('from add')
def add(a, b, *args, **kwargs):
    return a + b


if __name__ == '__main__':
    hello()
    rest = add(5, 6, k=3, v=4)
    print(rest)
