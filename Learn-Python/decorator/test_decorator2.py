"""
不带参数的装饰器
装饰器 返回函数的函数
      可以写多个
"""


def log(func):
    """记录函数执行的日志"""

    def wrapper():
        print("装饰器1 start...")
        func()
        print("装饰器1 end.")

    return wrapper


def log_in(func):
    """记录函数执行的日志"""

    def wrapper():
        print("装饰器2 start...")
        func()
        print("装饰器2 end.")

    return wrapper


@log
@log_in
def hello():
    """简单功能模拟"""
    print("hello world")


if __name__ == '__main__':
    hello()
