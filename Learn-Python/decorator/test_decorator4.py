from functools import wraps


def log(name=None):
    """记录函数执行的日志"""

    def decorator(func):
        @wraps(func)  # 内部提供的装饰器 对以前写好的函数使用装饰器之后的信息不会发生改变
        def wrapper(*args, **kwargs):  # 传参使用魔法方法传入
            """装饰器内部的函数"""
            # 内部装饰器对原有的函数名称文档信息发生了改变
            print("{0} start...".format(name))
            print("---wrapper:{0}".format(func.__doc__))
            print("---wrapper:{0}".format(func.__name__))
            temp = func(*args, **kwargs)  # 用临时变量保存结果返回 add函数有返回
            print("{0} end.".format(name))
            return temp

        # wrapper.__doc__ = func.__doc__
        # wrapper.__name__ = func.__name__
        return wrapper

    return decorator


@log('you')  # 这里需要传参数 不传默认None
def hello():
    """简单功能模拟"""
    print("hello world")


if __name__ == '__main__':
    print('doc:{0}'.format(hello.__doc__))
    print('doc:{0}'.format(hello.__name__))
    hello()
